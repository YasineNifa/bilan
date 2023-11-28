from django.shortcuts import reverse
from django.views.generic.edit import DeleteView

from compte.forms import ConfirmDeleteForm
from compte.models import Compte


class CompteDeleteView(DeleteView):
    form_class = ConfirmDeleteForm
    model = Compte
    model_name = "compte"
    name = "comptes_delete"

    template_name = "compte/delete.html"

    def get_success_url(self):
        return reverse("compte:index")