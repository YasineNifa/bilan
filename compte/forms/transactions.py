from django.forms import ModelForm

from compte.models import Transaction



class TransactionModelForm(ModelForm):


    class Meta:
        model = Transaction
        fields = "__all__"