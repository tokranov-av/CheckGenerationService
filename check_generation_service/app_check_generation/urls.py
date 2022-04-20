from django.urls import path
from .views import OrdersAPIView

urlpatterns = [
    path('create_checks/', OrdersAPIView.as_view(), name='create_checks'),
    # path('new_checks/', OrdersAPIView.as_view(), name='new_checks'),
    # path('check/', OrdersAPIView.as_view(), name='check'),
]
