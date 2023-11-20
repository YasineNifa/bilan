from django.urls import reverse_lazy

from django.views.generic import TemplateView

class IndexView(TemplateView):
    model = None
    template_name = "report/list.html"
    namespace = "report"
    model_name = ""
    title = "Report"
    view_name = "index"
