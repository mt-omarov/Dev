# логирование можно сделать в init, поэтому этот файл пока не нужон

import logging

logfile = 'bot.log'

log = logging.getLogger("my_log")
log.setLevel(logging.INFO)
FH = logging.FileHandler(logfile)
basic_formater = logging.Formatter("%(asctime)s : [%(levelname)s] : %(message)s")
FH.setFormatter(basic_formater)
log.addHandler(FH)