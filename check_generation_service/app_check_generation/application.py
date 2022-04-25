import os
import requests
from check_generation_service.settings import MEDIA_ROOT


def get_check_id(api_key):
    """Функция получения id чека по параметру api_key."""
    url_new_checks = 'http://127.0.0.1:8000/new_checks/?api_key={0}'.format(
        api_key,
    )
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url_new_checks, headers=headers)
    return response.json()


def get_check_pdf(api_key, check_id):
    """Функция получения pdf-файла чека по id чека и по ключу api_key."""
    url_check = 'http://127.0.0.1:8000/check/?api_key={0}&check_id={1}'.format(
        api_key, check_id
    )
    headers = {'Content-Type': 'application/json'}
    response = requests.get(
        url_check, headers=headers, stream=True
    )
    with open(os.path.join(MEDIA_ROOT, 'printed', 'file.pdf'), 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    current_check_id = get_check_id(api_key='key01')
    if current_check_id.get('checks'):
        current_check_id = current_check_id.get('checks')[0].get('id')
        get_check_pdf(api_key='key01', check_id=current_check_id)
