"""imports."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
