from django.views.generic import DetailView

from compte.models import Compte


class CompteDetailView(DetailView):
    model = Compte
    model_name = "compte"
    name = "comptes_detail"

    template_name = "compte/detail.html"
    context_object_name = "compte"
