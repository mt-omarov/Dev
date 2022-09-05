from django.core.management.base import BaseCommand
import bot

class Command(BaseCommand):
    help = 'start telegram bot'

    def handle(self, *args, **options):
        bot.bot_start()