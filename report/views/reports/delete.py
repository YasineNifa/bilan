from django.shortcuts import reverse
from django.views.generic.edit import DeleteView

from report.forms import ReportModelForm, ConfirmDeleteForm
from report.models import Report


class ReportDeleteView(DeleteView):
    # form_class = ConfirmDeleteForm
    model = Report
    model_name = "report"
    name = "reports_delete"

    title = "Create Report"
    template_name = "report/delete.html"

    def get_success_url(self):
        return reverse("report:index")