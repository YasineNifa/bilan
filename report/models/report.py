from autoslug import AutoSlugField
# from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.timezone import now

from report.apps import ReportConfig, NAME_MAX_LENGTH, TAG_MAX_LENGTH


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


# class TaggedModel(models.Model):
#     tags = ArrayField(
#         models.CharField(max_length=TAG_MAX_LENGTH, blank=True),
#         blank=True,
#         null=True,
#     )

#     class Meta:
#         abstract = True

class SimpleModel(SluggedModel, DatedModel):
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

class ActivatableModel(models.Model):
    activated = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def is_activated(self):
        return bool(self.activated)


class ArchivableModel(models.Model):
    archived = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True

    @property
    def is_archived(self):
        return bool(self.archived)


class Report(SimpleModel, ActivatableModel, ArchivableModel):
    class Meta:
        ordering = ["name"]
        verbose_name = "Report"
        verbose_name_plural = "Reports"

        app_label = ReportConfig.name


    def __str__(self):
        return self.name
