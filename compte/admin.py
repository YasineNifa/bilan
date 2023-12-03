from django.contrib import admin
from .models import Compte, Transaction, Ocr

# Register your models here.
admin.site.register(Compte)
admin.site.register(Ocr)
admin.site.register(Transaction)
