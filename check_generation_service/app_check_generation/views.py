from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MySerializer
from pprint import pprint
from .models import Check, Printer


class OrdersAPIView(APIView):

    def post(self, request, format=None):
        order = MySerializer(data=request.data)
        order.is_valid(raise_exception=True)
        pprint(order.data)
        order = order.data
        checks = Check.objects.filter(order=order)
        if checks:
            Response(
                {'error': 'Чеки для данного заказа были ранее созданы'}
            )
        printers = Printer.objects.filter(point_id=order['point_id'])
        if not printers:
            Response(
                {'error': 'На данной точке принтеры отсутствуют'}
            )

        return Response(
            {'ok': 'Чеки успешно созданы'}, status=200
        )
