import json
import requests
import base64
from django.template.loader import render_to_string
import os
import django
from django_rq import job
from .models import Check
from check_generation_service.settings import MEDIA_ROOT

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'check_generation_service.settings'
)
django.setup()


@job
def pdf_generation(order_data=None, check_type=None):
    """Функция генерации pdf-файла чека."""
    url = 'http://172.17.0.1:55000/'
    # url = 'http://127.0.0.1:55000/'
    pdf_file_name = 'file.pdf'
    order_id = order_data.get('id')

    if order_data and check_type == 'kitchen_check':
        pdf_file_name = '{0}_kitchen.pdf'.format(order_id)
        html = render_to_string('kitchen_check.html', context=order_data)
        current_check = Check.objects.filter(
            order=order_data, type='kitchen')
    elif order_data and check_type == 'client_check':
        pdf_file_name = '{0}_client.pdf'.format(order_id)
        html = render_to_string('client_check.html', context=order_data)
        current_check = Check.objects.filter(
            order=order_data, type='client')
    else:
        html, current_check = None, None

    if html:
        html = base64.b64encode(bytes(html, 'utf-8'))
        data = json.dumps(
            {'contents': str(html)[2:-1]}
        )
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)

        with open(os.path.join(MEDIA_ROOT, 'pdf', pdf_file_name), 'wb') as f:
            f.write(response.content)

        current_check.update(
            pdf_file=os.path.join('pdf', pdf_file_name), status='rendered'
        )
