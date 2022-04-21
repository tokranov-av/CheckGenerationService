from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MySerializer


class OrdersAPIView(APIView):
    def post(self, request, format=None):
        data = MySerializer(data=request.data)
        data.is_valid(raise_exception=True)
        client = dict(data.data['client'])
        return Response(
            {'ok': 'Чеки успешно созданы'}, status=200
        )
