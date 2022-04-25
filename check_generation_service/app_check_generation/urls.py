from django.urls import path
from .views import OrdersAPIView, ChecksAPIView, CheckAPIView

urlpatterns = [
    path('create_checks/', OrdersAPIView.as_view(), name='create_checks'),
    path('new_checks/', ChecksAPIView.as_view(),
         name='new_checks'),
    path('check/', CheckAPIView.as_view(), name='check'),
]
