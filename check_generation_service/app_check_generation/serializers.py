from rest_framework import serializers
from django.core.exceptions import ValidationError


def validate_bank_cart_number(bank_cart_number):
    """Проверка правильности ввода номера банковской карты."""
    if not bank_cart_number.isdigit():
        raise ValidationError('Номер карты должен состоять из 8 цифр')


class PaymentSerializer(serializers.Serializer):
    """Сериализатор для приема запроса оплаты."""
    id = serializers.IntegerField(min_value=1)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    items = serializers.ListField()

