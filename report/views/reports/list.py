from django.shortcuts import reverse, render
from django.views.generic import ListView

from report.forms import ReportModelForm
from report.models import Report




class ReportListView(ListView):
    model = Report
    model_name = "report"
    name = "reports_list"
    template_name = "report/list.html"
    context_object_name = "reports"

    def get_queryset(self):
        print("get_queryset")
        return Report.objects.all()
    
    # Add more context
    def get_context_data(self, **kwargs):
        context =  super(ReportListView,self).get_context_data(**kwargs)
        
        # TODO add archived__isnull=True, activated__isnull=False filters
        queryset = Report.objects.filter()
        context.update(
            {
                "reports": queryset
            }
        )
        return context
    
    def get(self, request, *args, **kwargs):
        return super(ReportListView, self).get(request, *args, **kwargs)
