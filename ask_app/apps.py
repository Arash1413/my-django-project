from django.apps import AppConfig


class AskAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ask_app'

    def ready(self):
        import ask_app.signall 