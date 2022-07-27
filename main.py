import asyncio

from amiyabot import AmiyaBot, Message, Chain

bot = AmiyaBot(appid='102018850', token='rrCvFLmWDQ9LRrxbZLxEaFCqQM6sDl3r',private=True)


@bot.on_message(keywords='/hello')
async def _(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')


asyncio.run(bot.start())
