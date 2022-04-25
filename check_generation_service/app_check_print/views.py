import os
import requests
import json
from check_generation_service.settings import MEDIA_ROOT

url_new_checks = 'http://127.0.0.1:8000/new_checks/'
url_check = 'http://127.0.0.1:8000/check/'
api_key = 'key01'
data = {
    'api_key': api_key
}
headers = {'Content-Type': 'application/json'}

response = requests.get(url_new_checks, data=json.dumps(data), headers=headers)
data = response.json()

if data.get('checks'):
    id = data.get('checks')[0].get('id')
    data = {
        'api_key': api_key,
        'check_id': id
    }
    response = requests.get(
        url_check, data=json.dumps(data), headers=headers, stream=True
    )
    with open(os.path.join(MEDIA_ROOT, 'printing', 'file.pdf'), 'wb') as file:
        file.write(response.content)
