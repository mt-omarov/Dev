from django.core.management.base import BaseCommand
from bot_app import start_config

class Command(BaseCommand):
    help = 'start telegram bot'

    def handle(self, *args, **options):
        start_config.start_creation()