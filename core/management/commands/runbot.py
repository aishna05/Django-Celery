from django.core.management.base import BaseCommand
from ...telegram import TelegramUser

class Command(BaseCommand):
    help = 'Runs the Telegram bot'

    def handle(self, *args, **kwargs):
        TelegramUser()
