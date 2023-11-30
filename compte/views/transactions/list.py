from typing import Any
from django.views.generic import ListView

# from report.forms import ReportModelForm
from compte.models import Transaction, Compte
from compte.filters import TransactionFilter
from report.models import Report




class TransactionListView(ListView):
    model = Transaction
    model_name = "transaction"
    name = "transactions_list"
    template_name = "compte/list_transaction.html"
    context_object_name = "transactions"

    def get_queryset(self):
        self.queryset = super().get_queryset()

        filters = TransactionFilter(
            self.request.GET,queryset=self.queryset, request=self.request,
        )
        filters.form.fields["report"].queryset = Report.objects.all()
        filters.form.fields["partie"].queryset = Compte.objects.all()
        filters.form.fields["contrepartie"].queryset = Compte.objects.all()

        self.queryset = filters.qs
        self.filters = filters.form

        return self.queryset

    def get_context_data(self, **kwargs):
        kwargs = super(TransactionListView, self).get_context_data(**kwargs)
        kwargs.update({
            "components":{
                "filters": self.filters
            }
        })
        return kwargs
    
    def get(self, request, *args, **kwargs):
        return super(TransactionListView, self).get(request, *args, **kwargs)
