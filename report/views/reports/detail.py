from django.shortcuts import reverse
from django.views.generic import DetailView

from report.models import Report


class ReportDetailView(DetailView):
    model = Report
    model_name = "report"
    name = "reports_detail"

    template_name = "report/detail.html"
    context_object_name = "report"
