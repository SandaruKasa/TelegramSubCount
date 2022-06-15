#!/usr/bin/env python3
import asyncio
import logging
import os

from pyrogram import Client, enums, types

import config

client = Client(
    name="SubCount",
    api_id=config.api_id,
    api_hash=config.api_hash,
)

MemberInfo = dict[int, types.User]


async def get_members(chat_id) -> MemberInfo:
    result: MemberInfo = {}
    async for member in client.get_chat_members(chat_id):
        user: types.User = member.user
        result[user.id] = user
    return result


def full_name(user: types.User) -> str:
    result: str = user.first_name
    if user.last_name:
        result += " "
        result += user.last_name
    return result


def print_members(where: str, members: MemberInfo) -> None:
    print(f"Total members in {where}: {len(members)}")
    humans: int = 0
    bots: int = 0
    for member in members.values():
        if member.is_bot:
            marker = "*"
            bots += 1
        else:
            marker = "-"
            humans += 1
        print(f"{marker} {full_name(member)}")
    print(f"Humans: {humans}")
    print(f"Bots: {bots}")


def intersection(a: dict, b: dict):
    return {k: a[k] for k in a if k in b}


def difference(a: dict, b: dict):
    return {k: a[k] for k in a if k not in b}


async def main():
    await client.start()

    channel_info: types.Chat = await client.get_chat(config.channel)
    assert (
        channel_info.type == enums.chat_type.ChatType.CHANNEL
    ), "The provided chat is not a channel"
    channel_members: MemberInfo = await get_members(channel_info.id)

    print_members(f'the channel "{channel_info.title}"', channel_members)
    print()

    chat_info: types.Chat | None = channel_info.linked_chat
    if chat_info is None:
        print(f"The channel has no linked chat.")
    else:
        chat_members: MemberInfo = await get_members(chat_info.id)
        print_members(f'the linked chat "{chat_info.title}"', chat_members)
        print()
        print_members(
            where=f"the channel and the linked chat combined",
            members=channel_members | chat_members,
        )
        print()
        print_members(
            where=f"both the channel and the linked chat (intersection)",
            members=intersection(channel_members, chat_members),
        )
        print()
        print_members(
            where=f"the channel but not the linked chat",
            members=difference(channel_members, chat_members),
        )
        print()
        print_members(
            where=f"the linked chat but not the channel",
            members=difference(chat_members, channel_members),
        )


if __name__ == "__main__":
    logging.basicConfig(
        handlers=[
            logging.StreamHandler(),
        ],
        level=os.getenv("LOGLEVEL", logging.getLevelName(logging.WARN)).upper(),
        format="[%(asctime)s.%(msecs)03d] [%(name)s] [%(levelname)s]: %(message)s",
        datefmt=r"%Y-%m-%dT%H-%M-%S",
    )
    asyncio.run(main())
