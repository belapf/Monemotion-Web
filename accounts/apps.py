from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = "Úsuarios do Sistema"
    verbose_name_plural = "Úsuarios do Sistema"

    def ready(self):
        import accounts.signals
