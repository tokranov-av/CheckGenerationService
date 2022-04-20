from rest_framework.views import APIView
from rest_framework.response import Response
from pprint import pprint


class OrdersAPIView(APIView):
    def post(self, request, format=None):
        pprint(request.data)
        return Response(
            {'ok': 'Чеки успешно созданы'}, status=200
        )
