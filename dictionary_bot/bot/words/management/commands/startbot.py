from django.core.management.base import BaseCommand
from bot_app.bot import bot_start


class Command(BaseCommand):
    help = 'start telegram bot'

    def handle(self, *args, **options):
        bot_start()