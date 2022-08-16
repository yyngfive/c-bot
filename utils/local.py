from datetime import datetime
import pytz
from utils import config


def today(fmt = '%Y-%m-%d') -> str:
    conf = config.read_config('./config/config.yml')
    timezone = conf.timezone
    local_date = datetime.now(pytz.timezone(timezone))
    return local_date.strftime(fmt)
