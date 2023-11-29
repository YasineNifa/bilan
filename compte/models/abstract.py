from autoslug import AutoSlugField
from django.db import models

from report.apps import NAME_MAX_LENGTH



class DatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class NamedModel(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)

    class Meta:
        abstract = True


class SluggedModel(NamedModel):
    slug = AutoSlugField(
        always_update=True, populate_from="name", max_length=NAME_MAX_LENGTH
    )

    class Meta:
        abstract = True

class SimpleModel(SluggedModel, DatedModel):
    description = models.TextField(blank=True)

    class Meta:
        abstract = True