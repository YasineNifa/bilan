from decimal import Decimal

from django.db import models
from django.db.models import CASCADE

from compte.apps import CompteConfig

class Transaction(models.Model):
    description = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, null=True)
    partie = models.ForeignKey("compte.Compte", related_name="partie_transactions", on_delete=CASCADE)
    contrepartie = models.ForeignKey("compte.Compte", related_name="contrepartie_transactions", on_delete=CASCADE)
    montant = models.DecimalField(
        default=Decimal(0),
        max_digits=20,
        decimal_places=4,
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

        app_label = CompteConfig.name

    def __str__(self):
        return self.description