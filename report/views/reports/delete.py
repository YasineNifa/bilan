from django.shortcuts import reverse
from django.views.generic.edit import DeleteView

from report.models import Report


class ReportDeleteView(DeleteView):
    model = Report
    model_name = "report"
    name = "reports_delete"

    template_name = "report/delete.html"

    def get_success_url(self):
        return reverse("report:index")