from django import forms
from django.conf import settings

from compte.models import Transaction



class TransactionModelForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = (
            "description",
            "date",
            "partie",
            "contrepartie",
            "montant",
            "report",
        )

        widgets = {
            "date": forms.DateInput(format=settings.ISO_DATE_FORMAT),
        }
