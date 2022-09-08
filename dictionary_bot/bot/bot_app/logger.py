import logging
logfile = 'bot.log'

from .bot import dp
from . import commands, random

log = logging.getLogger("my_log")
log.setLevel(level = logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter('%(asctime)s : [%(levelname)s] : %(message)s')
FH.setFormatter(basic_formater)
log.addHandler(FH)
