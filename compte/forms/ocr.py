
# forms.py
from django import forms
from compte.models import Ocr
 
 
class OcrModelForm(forms.ModelForm):
 
    class Meta:
        model = Ocr
        fields = ['name', 'ocr_img']
