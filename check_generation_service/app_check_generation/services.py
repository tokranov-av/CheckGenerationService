import django_rq


def create_checks(order):
    """Функция создания pdf-файлов чеков для кухни и для клиента."""
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
