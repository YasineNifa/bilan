from django.forms import ModelForm

from compte.models import Compte



class CompteModelForm(ModelForm):


    class Meta:
        model = Compte
        fields = (
            "name",
            "description",
            "code",
        )