from django.db import models

from compte.models.abstract import SimpleModel
from compte.apps import CompteConfig

class Compte(SimpleModel):
    code = models.PositiveIntegerField()

    class Meta:
        ordering = ["code"]
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"

        app_label = CompteConfig.name

    def __str__(self):
        return self.name
