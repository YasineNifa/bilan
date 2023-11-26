from django.shortcuts import reverse
from django.views.generic import ListView

from report.forms import ReportModelForm
from report.models import Report




class ReportListView(ListView):
    model = Report
    model_name = "report"
    name = "reports_list"
    template_name = "report/list.html"

    def get_queryset(self):
        return Report.objects.all()