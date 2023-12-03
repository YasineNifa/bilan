from django.views.generic import DetailView

from compte.models import Ocr


class OcrDetailView(DetailView):
    model = Ocr
    model_name = "ocr"
    name = "ocrs_detail"

    template_name = "compte/detail_ocr.html"
    context_object_name = "ocr"
