from django.shortcuts import reverse
from django.views.generic.edit import CreateView

from report.forms import ReportModelForm
from report.models import Report


class ReportCreateView(CreateView):
    form_class = ReportModelForm
    model = Report
    model_name = "report"
    name = "reports_create"

    title = "Create Report"
    template_name = "report/create.html"

    def get_success_url(self):
        return reverse("report:index")