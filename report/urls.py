from django.urls import path

from report.apps import ReportConfig
from report.views import IndexView, reports


app_name = ReportConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    # Report
    path("create/",reports.ReportCreateView.as_view(),name="reports_create"),
    
]