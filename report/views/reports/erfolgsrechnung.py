from django.shortcuts import reverse
from django.views.generic import DetailView

from report.models import Report


class ReportErfolgsrechnungView(DetailView):
    model = Report
    model_name = "report"
    name = "reports_erfolgsrechnung"

    template_name = "report/erfolgsrechnung.html"
    context_object_name = "report"
