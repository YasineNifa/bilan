from django.shortcuts import reverse
from django.views.generic.edit import CreateView

from compte.forms import TransactionModelForm
from compte.models import Transaction


class TransactionCreateView(CreateView):
    form_class = TransactionModelForm
    model = Transaction
    model_name = "transaction"
    name = "transactions_create"

    template_name = "compte/create_transaction.html"

    def get_success_url(self):
        return reverse("compte:index")
    
    def get_context_data(self, **kwargs):
        context =  super(TransactionCreateView,self).get_context_data(**kwargs)
        
        context.update(
            {
                "title": "New Transaction",
            }
        )
        return context