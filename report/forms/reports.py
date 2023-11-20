from django.forms import ModelForm

from report.models import Report



class ReportModelForm(ModelForm):


    class Meta:
        model = Report
        fields = (
            "name",
            "description",
        )