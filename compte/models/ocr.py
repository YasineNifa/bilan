from django.db import models

import json
import requests

from dateutil import parser
from datetime import datetime

class Ocr(models.Model):
    name = models.CharField(max_length=50)
    ocr_img = models.ImageField(upload_to='images/')


    # def remove_extra_spaces(self,input_string):
    #     """
    #     Remove unnecessary white spaces from a string.
        
    #     Parameters:
    #     - input_string (str): The input string with unnecessary white spaces.
        
    #     Returns:
    #     - str: The input string with extra white spaces removed.
    #     """
    #     # Split the string into words, removing empty strings caused by multiple spaces
    #     words = input_string.split()

    #     # Join the words back together with a single space between them
    #     result_string = ' '.join(words)

    #     return result_string
    
    # def is_valid_date(self, date_string):
    #     try:
    #         parsed_date = parser.parse(date_string)
    #         return True
    #     except ValueError:
    #         return False
    
    # # def typecast(self, input_string):
    # #     if self.is_valid_date(input_string):
    # #         return datetime.strftime(input_string, "%Y-%m-%d")
    # #     elif Compte.objects.get(name=input_string).count():
    # #         return 


    @property
    def extract_text(self):
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzViNjgzNzctYmVmOS00ODFmLWE1YmUtYmQ1ZGYzZjNiNzMxIiwidHlwZSI6ImFwaV90b2tlbiJ9.iZpAL6jDbYX74Qfo4e6zVNePdmu5F0h7qN-OHKFUOWA"}

        # url = "https://api.edenai.run/v2/ocr/ocr"
        # data = {
        #     "providers": "google",
        #     "language": "en",
        #     "fallback_providers": ""
        # }
        files = {"file": open(self.ocr_img.path, 'rb')}

        # response = requests.post(url, data=data, files=files, headers=headers)

        # result = json.loads(response.text)
        # extracted_text = result["google"]["text"]
        # split_extracted_text = extracted_text.split(",")
        return None
