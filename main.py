import asyncio
from random import randint
import yaml
import database.database as db
from amiyabot import AmiyaBot, Message, Chain
from munch import DefaultMunch
import utils

with open('./config/config.yml', encoding='utf-8') as f:
    config = yaml.safe_load(f)
    config_bot = DefaultMunch.fromDict(config)
appid = config_bot.login.appid
token = config_bot.login.token
bot = AmiyaBot(appid=appid, token=token, private=True)
bot.prefix_keywords = config_bot.prefix


@bot.on_message(keywords='/hello')
async def hello(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')


@bot.on_message(keywords='/help')
async def help(data: Message):

    return Chain(data, at=False).text(
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
    return Chain(data).text(f'你好，{nickname}，你的id为{user_id}，你加入频道的时间是{joined_at}，你的头像为：').image(target='', url=avatar)


@bot.on_message(keywords='/luck')
async def luck(data: Message):
    return Chain(data).text(f'你的当前运势：{randint(0,100)}')


@bot.on_message(keywords='/morning')
async def morning(data: Message):
    morning, created = db.Morning.get_or_create(user=str(data.user_id))
    morning.checkin = morning.checkin + 1
    morning.save()
    return Chain(data).text(f'签到成功！已累计签到{morning.checkin}天')

try:
    asyncio.run(bot.start())
except KeyboardInterrupt:
    ...
