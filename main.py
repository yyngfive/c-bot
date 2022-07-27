import asyncio
from random import randint
import yaml
from amiyabot import AmiyaBot, Message, Chain
# 此版本中日志功能可能存在中文编码问题，需在log.py手动添加utf-8
with open('./config.yml') as f:
    config = yaml.load(f, yaml.FullLoader)
appid = config['bot']['appid']
token = config['bot']['token']
bot = AmiyaBot(appid=appid, token=token,private=True)


@bot.on_message(keywords='/hello')
async def hello(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')

@bot.on_message(keywords='/help')
async def _(data: Message):
    return Chain(data).text(f'help, {data.nickname}')

asyncio.run(bot.start())
