from django.db import models

import json
import requests

from dateutil import parser
from datetime import datetime
from django.db.models import CASCADE
from compte.apps import CompteConfig

class Ocr(models.Model):
    name = models.CharField(max_length=50)
    ocr_img = models.ImageField(upload_to='images/')
    report = models.ForeignKey("report.Report", related_name="ocr_images", on_delete=CASCADE)


    class Meta:
        ordering = ["name"]
        verbose_name = "ocr_image"
        verbose_name_plural = "ocr_images"

        app_label = CompteConfig.name

    def __str__(self):
        return self.name