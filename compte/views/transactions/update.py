from django.shortcuts import reverse
from django.views.generic.edit import UpdateView

from compte.forms import TransactionModelForm
from compte.models import Transaction


class TransactionUpdateView(UpdateView):
    form_class = TransactionModelForm
    model = Transaction
    model_name = "compte"
    name = "comptes_update"

    # title = "Create Compte"
    template_name = "compte/create_transaction.html"

    def get_success_url(self):
        return reverse("compte:transactions_list")
    
    def get_context_data(self, **kwargs):
        context =  super(TransactionUpdateView,self).get_context_data(**kwargs)
        
        context.update(
            {
                "title": "Update Transaction", 
            }
        )
        return context
