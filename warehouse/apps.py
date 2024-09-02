"""
App configuration for the warehouse app.
"""

from django.apps import AppConfig


class WarehouseConfig(AppConfig):
    """
    Configuration for the warehouse app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "warehouse"
