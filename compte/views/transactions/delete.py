from django.shortcuts import reverse
from django.views.generic.edit import DeleteView

from compte.models import Transaction


class TransactionDeleteView(DeleteView):
    model = Transaction
    model_name = "transaction"
    name = "transactions_delete"

    template_name = "compte/delete_transaction.html"

    def get_success_url(self):
        return reverse("compte:transactions_list")