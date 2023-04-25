from django.apps import AppConfig


class UserregistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userregistration'
    def ready(self):
        import userregistration.signals