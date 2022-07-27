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

bot.prefix_keywords = ['cbot', 'c-bot']

@bot.on_message(keywords='/hello')
async def hello(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')

@bot.on_message(keywords='/help')
async def help(data: Message):
    
    return Chain(data,at=False).text(
'''欢迎使用c-bot，你可以使用cbot或c-bot+/指令名使用\n
/hello:打招呼\n
/help:查看帮助\n
/me:查看自己信息\n
/luck:生成0~100随机数\n
''')

@bot.on_message(keywords='/me')
async def me(data: Message):
    nickname = data.nickname
    user_id = data.user_id
    joined_at = data.joined_at[0:10]
    avatar = data.avatar
    return Chain(data).text(f'你好，{nickname}，你的id为{user_id}，你加入频道的时间是{joined_at}，你的头像为：').image(target='',url=avatar)

@bot.on_message(keywords='/luck')
async def luck(data: Message):
    return Chain(data).text(f'你的当前运势：{randint(0,100)}')

asyncio.run(bot.start())
