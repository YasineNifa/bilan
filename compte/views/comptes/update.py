from django.shortcuts import reverse
from django.views.generic.edit import UpdateView

from compte.forms import CompteModelForm
from compte.models import Compte


class CompteUpdateView(UpdateView):
    form_class = CompteModelForm
    model = Compte
    model_name = "compte"
    name = "comptes_update"

    # title = "Create Compte"
    template_name = "compte/create.html"

    def get_success_url(self):
        return reverse("compte:index")
    
    def get_context_data(self, **kwargs):
        context =  super(CompteUpdateView,self).get_context_data(**kwargs)
        
        context.update(
            {
                "title": "Update Compte", 
            }
        )
        return context
