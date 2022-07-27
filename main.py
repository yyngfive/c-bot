import botpy
from botpy.message import Message
from botpy import logging
from botpy.types.message import Embed, EmbedField
import random

_log = logging.get_logger()
#TODO: 改用装饰器替换if语句
#TODO: 更友好的log信息记录
#TODO: 改用配置文件顺便接入数据库
#TODO: 跑在树莓派上
#BUG: 解决多条指令之间的冲突
class MyClient(botpy.Client):

    async def on_message_create(self, message: Message):
        if '/hello' in message.content or 'hello' in message.content:
            await message.reply(content=f"欢迎使用机器人 {self.robot.name}，你可以/help获取帮助")
            _log.info(f'{message.author.id}调用了/hello指令')
        elif '/help' in message.content:
            embed = Embed(title="帮助信息",
                          prompt="帮助详情",
                          fields=[
                            EmbedField(name='hello: 查看欢迎消息'),
                            EmbedField(name='help: 查看帮助'),
                            EmbedField(name='info: 查看个人信息'),
                            EmbedField(name='luck: 0-100随机数'),
                            EmbedField(name='members: 查询频道成员（目前只支持前100人）')])
            await message.reply(content = f'欢迎使用 {self.robot.name} ,你可以使用/+如下指令来使用')
            await message.reply(embed=embed)
            _log.info(f'{message.author.id}调用了help指令')
        elif '/info' in message.content:
            info = await self.api.get_guild_member(guild_id=message.guild_id,user_id=message.author.id)
            await message.reply(content=f'你是{info["user"]["username"]}，你加入频道的时间是{info["joined_at"]}',image=info['user']['avatar'])
            _log.info(f'{message.author.id}查询了个人信息')
        elif '/luck' in message.content:
            luck = random.randint(0,100)
            await message.reply(content = f'<@!{message.author.id}>今日运势：{luck}')
        elif '/members' in message.content:
            members = await self.api.get_guild_members(message.guild_id,limit=100)
            names = []
            for member in members:
                names.append(member['user']['username'])
            await message.reply(content = '频道成员有: \n'+'\n'.join(names))
            _log.info(f'{message.author.id}查询了频道成员')
        else:
            pass
            #await message.reply(content = f'无此指令:{message.content}，请使用help查看帮助')
            #_log.info(f'无效的指令:{message.content}')


    #async def on_message_create(self, message: Message):
        
    #    await self.api.post_message(channel_id=message.channel_id, content = f'你发送了 {message.content},真不戳！')

intents = botpy.Intents(public_guild_messages=True,
                        guild_messages = True) 
client = MyClient(intents=intents)
client.run(appid="102018850", token="rrCvFLmWDQ9LRrxbZLxEaFCqQM6sDl3r")