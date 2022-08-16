import asyncio
from random import randint
import database.database as db
from amiyabot import AmiyaBot, Message, Chain
from utils import local, config

config_bot = config.read_config('./config/config.yml')
config_func = config.read_config('./config/functions.yml')

appid = config_bot.login.appid
token = config_bot.login.token
bot = AmiyaBot(appid=appid, token=token, private=True)
bot.prefix_keywords = config_bot.prefix


@bot.on_message(keywords=config_func.hello.key)
async def hello(data: Message):
    return Chain(data).text(f'hello, {data.nickname}')


@bot.on_message(keywords=config_func.help.key)
async def help(data: Message):

    help_info = [f'欢迎使用c-bot，你可以使用{"或".join(config_bot.prefix)}+/指令名使用']
    for fun in config_func.values():
        if type(fun.key) is list:
            help_info.append('或'.join(fun.key) + ': ' + fun.desc)
        else:
            help_info.append(fun.key + ': ' + fun.desc)

    return Chain(data, at=False).text('\n'.join(help_info))


@bot.on_message(keywords=config_func.me.key)
async def me(data: Message):
    nickname = data.nickname
    user_id = data.user_id
    joined_at = data.joined_at[0:10]
    avatar = data.avatar
    return Chain(data).text(f'你好，{nickname}，你的id为{user_id}，你加入频道的时间是{joined_at}，你的头像为：').image(target='', url=avatar)


@bot.on_message(keywords=config_func.luck.key)
async def luck(data: Message):
    return Chain(data).text(f'你的当前运势：{randint(0,100)}')


@bot.on_message(keywords=config_func.morning.key)
async def morning(data: Message):
    morning, created = db.Morning.get_or_create(user=str(data.user_id))

    if str(morning.checkin_date) == local.today():
        return Chain(data).text(f'重复签到！已累计签到{morning.checkin}天')
    else:
        morning.checkin = morning.checkin + 1
        morning.checkin_date = local.today()
        morning.save()
        return Chain(data).text(f'签到成功！已累计签到{morning.checkin}天')
        

try:
    asyncio.run(bot.start())
except KeyboardInterrupt:
    print('c-bot已退出')
