from django.apps import AppConfig


class BillingConfig(AppConfig):
    name = 'api.v1.billing'

    def ready(self):
        import api.v1.billing.signals.handlers
