import json

from dateutil import parser
from datetime import datetime
import requests

from django.views.generic import DetailView

from compte.models import Ocr, Compte, Transaction




class OcrDetailView(DetailView):
    model = Ocr
    model_name = "ocr"
    name = "ocrs_detail"

    template_name = "compte/detail_ocr.html"
    context_object_name = "ocr"
    object = None


    def remove_extra_spaces(self,input_string):
        """
        Remove unnecessary white spaces from a string.
        
        Parameters:
        - input_string (str): The input string with unnecessary white spaces.
        
        Returns:
        - str: The input string with extra white spaces removed.
        """
        words = input_string.split()
        result_string = ' '.join(words)

        return result_string
    
    def is_valid_date(self, date_string):
        try:
            parser.parse(date_string)
            return True
        except ValueError:
            return False
    
    def typecast(self, input_string, d):
        if self.is_valid_date(input_string) and not d["date"]:
            print("input_string : ", input_string)
            try:
                d["date"] = datetime.strptime(input_string, "%d/%m/%Y").date()
            except Exception:
                d["date"] = input_string
        elif Compte.objects.filter(name=input_string).count() and not d["partie"]:
            d["partie"] = Compte.objects.get(name=input_string)
        elif Compte.objects.filter(name=input_string).count() and not d["contrepartie"]:
            d["contrepartie"] = Compte.objects.get(name=input_string)
        else:
            try:
                montant = float(input_string)
                d["montant"] = montant
            except:
                d["description"] = input_string

        return d


    def extract_text(self):
        ocr_obj = self.get_object()
        ## =====================================================
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzViNjgzNzctYmVmOS00ODFmLWE1YmUtYmQ1ZGYzZjNiNzMxIiwidHlwZSI6ImFwaV90b2tlbiJ9.iZpAL6jDbYX74Qfo4e6zVNePdmu5F0h7qN-OHKFUOWA"}

        url = "https://api.edenai.run/v2/ocr/ocr"
        data = {
            "providers": "google",
            "language": "en",
            "fallback_providers": ""
        }
        files = {"file": open(ocr_obj.ocr_img.path, 'rb')}

        response = requests.post(url, data=data, files=files, headers=headers)

        result = json.loads(response.text)
        extracted_text = result["google"]["text"]
        ## =====================================================

        # with open(ocr_obj.ocr_img.path, 'rb') as image_file:
        #     image_bytes = image_file.read()

        # image_bytes_io = BytesIO(image_bytes)

        # image = Image.open(image_bytes_io)
        # try:
        #     image.filter(ImageFilter.SHARPEN)
        # except ValueError:
        #     print("Got an image that failed to sharpen")
        #     pass
        # extracted_text= pytesseract.image_to_string(image, lang="eng")
        print("Text retrieved : ", extracted_text)
        ## =====================================================

        split_extracted_text = extracted_text.split(",")
        clean_text = map(self.remove_extra_spaces, split_extracted_text)
        print("clean_text : ", clean_text)
        keyList = ["date", "partie", "description", "contrepartie", "montant"]
        d = {}
        for key in keyList:
            d[key] = None

        for val in clean_text:
            self.typecast(val, d)

        return d
    

    def get_context_data(self, **kwargs):
        context = super(OcrDetailView, self).get_context_data(**kwargs)
        context['transaction'] = self.extract_text()
        return context


    def post(self, request, *args, **kwargs):
        ocr_obj = self.get_object()

        self.extracted_transactions = self.extract_text()
        instance = Transaction(
            date = self.extracted_transactions["date"],
            partie = self.extracted_transactions["partie"],
            description = self.extracted_transactions["description"],
            contrepartie = self.extracted_transactions["contrepartie"],
            montant = self.extracted_transactions["montant"],
            report = ocr_obj.report
        )
        instance.save()
        return self.get(request, *args, **kwargs)
