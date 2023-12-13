from django.db import models

import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import json
import requests

class Ocr(models.Model):
    name = models.CharField(max_length=50)
    ocr_img = models.ImageField(upload_to='images/')



    @property
    def extract_text(self):
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzViNjgzNzctYmVmOS00ODFmLWE1YmUtYmQ1ZGYzZjNiNzMxIiwidHlwZSI6ImFwaV90b2tlbiJ9.iZpAL6jDbYX74Qfo4e6zVNePdmu5F0h7qN-OHKFUOWA"}

        url = "https://api.edenai.run/v2/ocr/ocr"
        data = {
            "providers": "google",
            "language": "en",
            "fallback_providers": ""
        }
        files = {"file": open(self.ocr_img.path, 'rb')}

        response = requests.post(url, data=data, files=files, headers=headers)

        result = json.loads(response.text)
        return result["google"]["text"]