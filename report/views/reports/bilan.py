from django.shortcuts import reverse
from django.views.generic import DetailView

from report.models import Report


class ReportBilanView(DetailView):
    model = Report
    model_name = "report"
    name = "reports_bilan"

    template_name = "report/bilan.html"
    context_object_name = "report"
