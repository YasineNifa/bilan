from django.forms import BooleanField, ValidationError, ModelForm
from compte.models import Compte

class ConfirmDeleteForm(ModelForm):
    confirm = BooleanField()

    class Meta:
        model = Compte
        exclude= '__all__'


    def clean(self):
        cleaned_data = super().clean()
        if "confirm" not in cleaned_data:
            raise ValidationError("You must confirm the delete.")
