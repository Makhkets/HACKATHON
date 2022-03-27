from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'api.v1.users'

    def ready(self):
        import api.v1.users.signals.handlers
