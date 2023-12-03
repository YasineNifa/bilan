from django.urls import path

from report.apps import ReportConfig
from report.views import reports


app_name = ReportConfig.name
urlpatterns = [
    path("", reports.ReportListView.as_view(), name="index"),
    # Report
    path("create/",reports.ReportCreateView.as_view(),name="reports_create"),
    path('<int:pk>/update/', reports.ReportUpdateView.as_view(),name='reports_update'),
    path('<int:pk>/delete/', reports.ReportDeleteView.as_view(), name='reports_delete'),
    path('<int:pk>/', reports.ReportDetailView.as_view(), name='reports_detail'),
    path('<int:pk>/bilan', reports.ReportBilanView.as_view(), name='reports_bilan'),
]