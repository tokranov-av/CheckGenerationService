from django.test import TestCase, override_settings
from django.urls import reverse
import tempfile
import shutil
from rest_framework.test import APIClient
from ..models import Printer, Check
from django_rq import get_worker
from django.core.files.uploadedfile import SimpleUploadedFile
MEDIA_ROOT = tempfile.mkdtemp()


@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class ViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_file = SimpleUploadedFile(
            'file_1.jpg', content=b'', content_type='application/pdf')
        printer = Printer.objects.create(
            name='Test printer 1',
            api_key='key01',
            check_type='kitchen',
            point_id=1
        )
        Printer.objects.create(
            name='Test printer 2',
            api_key='key02',
            check_type='client',
            point_id=1
        )
        Check.objects.create(
            printer=printer,
            type='kitchen',
            order='888',
            status='rendered',
            pdf_file=test_file
        )

    def test_create_checks(self):
        self.client = APIClient()
        data = {
            "id": "123456",
            "price": "780",
            "items": [
                {
                    "name": "Вкусная пицца",
                    "quantity": "2",
                    "unit_price": "250"
                },
                {
                    "name": "Не менее вкусные роллы",
                    "quantity": "1",
                    "unit_price": "280"
                }
            ],
            "address": "г. Уфа, ул. Ленина, д. 42",
            "client": {
                "name": "Иван",
                "phone": "9173332222"
            },
            "point_id": "1"
        }
        self.assertTrue(Check.objects.all().count() == 1)
        response = self.client.post(
            reverse('create_checks'), data=data, format='json'
        )
        get_worker().work(burst=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Check.objects.all().count() == 3)

    def test_new_checks(self):
        response = self.client.get('/new_checks/?api_key=key01')
        self.assertEqual(response.status_code, 200)

    def test_check(self):
        response = self.client.get('/check/?api_key=key01&check_id=1')
        self.assertEqual(response.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(MEDIA_ROOT)
        super().tearDownClass()
