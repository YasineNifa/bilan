from django.shortcuts import reverse
from compte.forms import OcrModelForm

from django.views.generic.edit import CreateView

from compte.forms import OcrModelForm
from compte.models import Ocr

# Create your views here.


class OcrUploadView(CreateView):
    form_class = OcrModelForm
    model = Ocr
    model_name = "ocr"
    name = "ocrs_upload"
    template_name = "compte/ocr_upload.html"

    def get_success_url(self):
        return reverse('compte:ocrs_images')
    
