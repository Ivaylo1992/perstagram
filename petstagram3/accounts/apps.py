from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'petstagram3.accounts'

    def ready(self):
        from petstagram3.accounts import signals