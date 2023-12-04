from django.db import models

import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO

class Ocr(models.Model):
    name = models.CharField(max_length=50)
    ocr_img = models.ImageField(upload_to='images/')



    @property
    def extract_text(self):
        with open(self.ocr_img.path, 'rb') as image_file:
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
        return text