from amiyabot.database import *

db = connect_database('cbot.sqlite') 

class BotBaseModel(ModelClass):
    class Meta:
        database = db

@table
class Morning(BotBaseModel):
    user = CharField()
    checkin = IntegerField(default=0)
