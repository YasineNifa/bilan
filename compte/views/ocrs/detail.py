from django.views.generic import DetailView
import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO

from compte.models import Ocr




class OcrDetailView(DetailView):
    model = Ocr
    model_name = "ocr"
    name = "ocrs_detail"

    template_name = "compte/detail_ocr.html"
    context_object_name = "ocr"



    def get(self, request, *args, **kwargs):
        ocr_obj = self.get_object()
        
        # img = np.array(Image.open(ocr_obj.ocr_img))
        # image = Image.open(ocr_obj.ocr_img)
        # response = requests.get("https://i.postimg.cc/sDLf7gpp/IMG-5483.jpg")
        # image = Image.open(BytesIO(response.content))


        with open(ocr_obj.ocr_img.path, 'rb') as image_file:
            # Read the image file as bytes
            image_bytes = image_file.read()

        # Create a BytesIO object and write the image bytes to it
        image_bytes_io = BytesIO(image_bytes)

        image = Image.open(image_bytes_io)
        try:
            image.filter(ImageFilter.SHARPEN)
        except ValueError:
            print("Got an image that failed to sharpen")
            pass
        text= pytesseract.image_to_string(image, lang="eng")
        print("Text retrieved : ", text)



        return super(OcrDetailView, self).get(request, *args, **kwargs)