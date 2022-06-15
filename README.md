# What is this?

A small Telegram userbot (a program that acts under the name of an existing regular user account,
and not a ["Telegram bot"](https://core.telegram.org/bots)
(though nothing stops you from running it under a bot account
(aside form maybe having to make the bot an admin on the channel)))
that counts the number of subscribers of a channel and members of its discussion group,
and then finds their sum, difference, and intersection.

# How to run it?

0. You will need python (probably 3.10+ because I've used some fancy type annotations).
And [dependencies](requirements.txt) installed.
(Hint: use [venv](https://docs.python.org/3/library/venv.html))
1. You will need a [Telegram `api_id` & `api_hash`](https://core.telegram.org/api/obtaining_api_id).
And a willingness to potentially sacrifice your Telegram account because I've heard numerous stories
of users receiving unfair bans from Telegram for using userbots even without any malicious intent.
Alternatively, you can try running this under a bot account.
In that case you will have to go though the hassle of promoting the bot to an admin,
so that it can fetch the member list.
2. Copy the `config.example.py` to `config.py`.
Replace example values with your `api_id` and `api_hash`.
Set the id or the @username of the channel in question.
3. Launch the userbot with `python -m userbot` or `python userbot.py`.
4. On the first launch you will need to log in.
