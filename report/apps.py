from django.apps import AppConfig


class ReportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "report"


NAME_MAX_LENGTH = 200
TAG_MAX_LENGTH = 100