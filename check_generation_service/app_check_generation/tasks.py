import json
import requests
import base64
from django.template.loader import render_to_string
import os
import django

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'check_generation_service.settings'
)
django.setup()

url = 'http://127.0.0.1:55002/'

context = {
    "id": 123456,
    "price": 780,
    "items": [
        {
            "name": "Вкусная пицца",
            "quantity": 2,
            "unit_price": 250
        },
        {
            "name": "Не менее вкусные роллы",
            "quantity": 1,
            "unit_price": 280
        }
    ],
    "address": "г. Уфа, ул. Ленина, д. 42",
    "client": {
        "name": "Иван",
        "phone": 9173332222
    },
    "point_id": 1
}

html = render_to_string('client_check.html', context=context)
html = base64.b64encode(bytes(html, 'utf-8'))
data = {
    'contents': str(html)[2:-1],
}
headers = {
    'Content-Type': 'application/json',
}
response = requests.post(url, data=json.dumps(data), headers=headers)

with open('file.pdf', 'wb') as f:
    f.write(response.content)
