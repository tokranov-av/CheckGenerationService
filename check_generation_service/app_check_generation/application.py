import os
import requests
import json
from check_generation_service.settings import MEDIA_ROOT

current_api_key = 'key01'


def get_check_id(api_key):
    """Функция получения id чека по параметру api_key."""
    url_new_checks = 'http://127.0.0.1:8000/new_checks/'
    data = {'api_key': api_key}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url_new_checks, data=json.dumps(data), headers=headers)
    return response.json()


def get_check_pdf(api_key, check_id):
    """Функция получения pdf-файла чека по id чека и по ключу api_key."""
    url_check = 'http://127.0.0.1:8000/check/'
    data = {'api_key': api_key, 'check_id': check_id}
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url_check, data=json.dumps(data), headers=headers, stream=True
    )
    with open(os.path.join(MEDIA_ROOT, 'printing', 'file.pdf'), 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    current_check_id = get_check_id(api_key='key01')
    if current_check_id.get('checks'):
        current_check_id = current_check_id.get('checks')[0].get('id')
        get_check_pdf(api_key='key01', check_id=current_check_id)
