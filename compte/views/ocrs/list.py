from django.views.generic import ListView

# from report.forms import ReportModelForm
from compte.models import Ocr





class OcrListView(ListView):
    model = Ocr
    model_name = "ocr"
    name = "ocrs_list"
    template_name = "compte/list_ocr.html"
    context_object_name = "ocrs"

    # def get_queryset(self):
    #     self.queryset = super().get_queryset()

    #     filters = OcrListView(
    #         self.request.GET,queryset=self.queryset, request=self.request,
    #     )
    #     filters.form.fields["report"].queryset = Report.objects.all()
    #     filters.form.fields["partie"].queryset = Compte.objects.all()
    #     filters.form.fields["contrepartie"].queryset = Compte.objects.all()

    #     self.queryset = filters.qs
    #     self.filters = filters.form

    #     return self.queryset

    # def get_context_data(self, **kwargs):
    #     kwargs = super(OcrListView, self).get_context_data(**kwargs)
    #     kwargs.update({
    #         "components":{
    #             "filters": self.filters
    #         }
    #     })
    #     return kwargs
    
    def get(self, request, *args, **kwargs):
        images = Ocr.objects.all()
        print("images : ", images)
        return super(OcrListView, self).get(request, *args, **kwargs)
