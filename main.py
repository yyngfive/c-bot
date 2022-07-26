import botpy
from botpy.message import Message
from botpy import logging
from botpy.types.message import Embed, EmbedField
import random

_log = logging.get_logger()

class MyClient(botpy.Client):

    async def on_at_message_create(self, message: Message):
        if '/hello' in message.content or 'hello' in message.content:
            await message.reply(content=f"欢迎使用机器人 {self.robot.name}，你可以@我+help获取帮助")
            _log.info(f'{message.author.id}调用了/hello指令')
        elif 'help' in message.content:
            embed = Embed(title="帮助信息",
                          prompt="帮助详情",
                          fields=[
                            EmbedField(name='/hello: 查看欢迎消息'),
                            EmbedField(name='help: 查看帮助'),
                            EmbedField(name='info: 查看个人信息'),
                            EmbedField(name='luck: 0-100随机数')])
            await message.reply(content = f'欢迎使用 {self.robot.name} ,你可以使用@我+如下指令来使用')
            await self.api.post_message(message.channel_id,embed=embed)
            _log.info(f'{message.author.id}调用了help指令')
        elif 'info' in message.content:
            info = await self.api.get_guild_member(guild_id=message.guild_id,user_id=message.author.id)
            await message.reply(content=f'你是{info["user"]["username"]}，你加入频道的时间是{info["joined_at"]}')
            await self.api.post_message(message.channel_id,image=info['user']['avatar'],msg_id=message.id)
            _log.info(f'{message.author.id}查询了个人信息')
        elif 'luck' in message.content:
            luck = random.randint(0,100)
            await message.reply(content = f'<@!{message.author.id}>今日运势：{luck}')
        else:
            await message.reply(content = f'无此指令:{message.content}，请使用help查看帮助')
            _log.info(f'无效的指令:{message.content}')


    #async def on_message_create(self, message: Message):
        
    #    await self.api.post_message(channel_id=message.channel_id, content = f'你发送了 {message.content},真不戳！')

intents = botpy.Intents(public_guild_messages=True,
                        guild_messages = True) 
client = MyClient(intents=intents)
client.run(appid="102018850", token="rrCvFLmWDQ9LRrxbZLxEaFCqQM6sDl3r")