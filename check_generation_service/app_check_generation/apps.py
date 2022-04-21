from django.apps import AppConfig


class AppCheckGenerationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_check_generation'
    verbose_name = 'Сервис генерации чеков'
