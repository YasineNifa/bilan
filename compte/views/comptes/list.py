from django.views.generic import ListView

# from report.forms import ReportModelForm
from compte.models import Compte




class CompteListView(ListView):
    model = Compte
    model_name = "compte"
    name = "comptes_list"
    template_name = "compte/list.html"
    context_object_name = "comptes"

    def get_queryset(self):
        return Compte.objects.all()
    
    # Add more context
    def get_context_data(self, **kwargs):
        context =  super(CompteListView,self).get_context_data(**kwargs)
        
        # TODO add archived__isnull=True, activated__isnull=False filters
        queryset = Compte.objects.filter()
        context.update(
            {
                "comptes": queryset
            }
        )
        return context
    
    def get(self, request, *args, **kwargs):
        return super(CompteListView, self).get(request, *args, **kwargs)
