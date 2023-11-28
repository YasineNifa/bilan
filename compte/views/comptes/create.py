from django.shortcuts import reverse
from django.views.generic.edit import CreateView

# from report.forms import ReportModelForm
from compte.models import Compte


class CompteCreateView(CreateView):
    # form_class = ReportModelForm
    model = Compte
    model_name = "compte"
    name = "comptes_create"

    template_name = "compte/create.html"

    def get_success_url(self):
        return reverse("compte:index")
    
    def get_context_data(self, **kwargs):
        context =  super(CompteCreateView,self).get_context_data(**kwargs)
        
        context.update(
            {
                "title": "New Compte", 
            }
        )
        return context