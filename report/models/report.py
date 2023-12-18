from autoslug import AutoSlugField
# from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Q, Sum

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


    

class Report(SimpleModel):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Report"
        verbose_name_plural = "Reports"

        app_label = ReportConfig.name


    def __str__(self):
        return self.name
    
    @property
    def get_einkomme(self):
        filterList = [1, 2]
        query = Q()
        for number in filterList:
            query = query | Q(partie__code__startswith=number)
        return self.transactions.filter(query)
    
    @property
    def get_ausgabe(self):
        filterList = [1, 2]
        query = Q()
        for number in filterList:
            query = query | Q(contrepartie__code__startswith=number)
        return self.transactions.filter(query)
    
    @property
    def get_bilanz(self):
        einkomme_total = self.get_einkomme.aggregate(Sum('montant'))
        ausgabe_total = self.get_ausgabe.aggregate(Sum('montant'))
        print("einkomme_total : ", einkomme_total["montant__sum"], ausgabe_total["montant__sum"])
        if einkomme_total["montant__sum"] and ausgabe_total["montant__sum"]:
            return einkomme_total["montant__sum"] - ausgabe_total["montant__sum"]
        else:
            return einkomme_total["montant__sum"] or ausgabe_total["montant__sum"]
    
    @property
    def get_cat_3(self):
        filterList = [3]
        query = Q()
        for number in filterList:
            query = query | Q(contrepartie__code__startswith=number)
        return self.transactions.filter(query)
    
    @property
    def get_cat_4_5_6(self):
        filterList = [4,5,6]
        query = Q()
        for number in filterList:
            query = query | Q(partie__code__startswith=number)
        return self.transactions.filter(query)
    
    @property
    def get_erfolgsrechnung(self):
        cat_3_total = self.get_cat_3.aggregate(Sum('montant'))
        cat_4_5_6_total = self.get_cat_4_5_6.aggregate(Sum('montant'))

        if not cat_3_total["montant__sum"]:
            cat_3_total["montant__sum"]= 0
        if not cat_4_5_6_total["montant__sum"]:
            cat_4_5_6_total["montant__sum"] = 0

        return cat_3_total["montant__sum"] - cat_4_5_6_total["montant__sum"]

