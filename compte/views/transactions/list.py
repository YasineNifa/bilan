from django.views.generic import ListView

# from report.forms import ReportModelForm
from compte.models import Transaction




class TransactionListView(ListView):
    model = Transaction
    model_name = "transaction"
    name = "transactions_list"
    template_name = "compte/list_transaction.html"
    context_object_name = "transactions"

    def get_queryset(self):
        return Transaction.objects.all()
    
    # Add more context
    def get_context_data(self, **kwargs):
        context =  super(TransactionListView,self).get_context_data(**kwargs)
        
        # TODO add archived__isnull=True, activated__isnull=False filters
        queryset = Transaction.objects.filter()
        context.update(
            {
                "comptes": queryset
            }
        )
        return context
    
    def get(self, request, *args, **kwargs):
        return super(TransactionListView, self).get(request, *args, **kwargs)
