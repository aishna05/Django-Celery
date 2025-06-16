import requests
from .models import TelegramUser

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"

def process_updates():
    response = requests.get(URL + "getUpdates").json()
    for result in response['result']:
        msg = result.get('message', {})
        text = msg.get('text', '')
        user = msg.get('from', {})
        if text == "/start":
            TelegramUser.objects.get_or_create(
                username=user.get('username'),
                telegram_id=user.get('id')
            )
