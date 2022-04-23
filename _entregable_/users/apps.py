from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "_entregable_.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import _entregable_.users.signals  # noqa F401
        except ImportError:
            pass
