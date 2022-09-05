from aiogram.types import InlineKeyboardButton
from asgiref.sync import sync_to_async
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.db.models import Q
#from words.models import Subscription, User, Promocode
#import MESSAGES
from logger import log
from django.utils import timezone
dj_now = timezone.now

