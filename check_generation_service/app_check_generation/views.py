from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Check, Printer
import django_rq
from django.db import transaction


class OrdersAPIView(APIView):
    @classmethod
    def post(cls, request, format=None):
        order = OrderSerializer(data=request.data)
        order.is_valid(raise_exception=True)
        order = order.data
        checks = Check.objects.filter(order=order)
        if checks:
            return Response(
                {'error': 'Чеки для данного заказа были ранее созданы'}
            )
        printers = Printer.objects.filter(point_id=order['point_id'])
        kitchen_printer = printers.filter(check_type='kitchen').first()
        client_printer = printers.filter(check_type='client').first()
        if not (kitchen_printer and client_printer):
            return Response(
                {'error': 'На данной точке принтеры отсутствуют'}
            )
        with transaction.atomic():
            kitchen_check = Check.objects.create(
                printer=kitchen_printer,
                type='kitchen',
                order=order,
                status='new',
            )
            client_check = Check.objects.create(
                printer=client_printer,
                type='client',
                order=order,
                status='new'
            )

        if kitchen_check and client_check:
            queue_1 = django_rq.get_queue('default')
            queue_1.enqueue(
                'app_check_generation.tasks.pdf_generation',
                order_data=order,
                check_type='kitchen_check'
            )
            queue_2 = django_rq.get_queue('default')
            queue_2.enqueue(
                'app_check_generation.tasks.pdf_generation',
                order_data=order,
                check_type='client_check'
            )
            return Response(
                {'ok': 'Чеки успешно созданы'}, status=200
            )
        return Response(
            {'error': 'Возникла ошибка при создании чеков'}
        )
