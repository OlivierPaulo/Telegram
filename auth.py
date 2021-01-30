import os
import requests

token = os.environ.get('TELEGRAM_API_TOKEN')
print(token)
req = requests.get(f"https://api.telegram.org/bot{token}/getMe")

print(req.json())