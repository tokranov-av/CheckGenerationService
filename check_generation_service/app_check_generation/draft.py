import django_rq

context = {
        "id": 123456,
        "price": 780,
        "items": [
            {
                "name": "Вкусная пицца",
                "quantity": 2,
                "unit_price": 250
            },
            {
                "name": "Не менее вкусные роллы",
                "quantity": 1,
                "unit_price": 280
            }
        ],
        "address": "г. Уфа, ул. Ленина, д. 42",
        "client": {
            "name": "Иван",
            "phone": 9173332222
        },
        "point_id": 1
    }

if '__name__':
    queue = django_rq.get_queue('default')
    queue.enqueue('app_check_generation.tasks.pdf_generation', context)
