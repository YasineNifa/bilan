from django.urls import path

from compte.apps import CompteConfig
from compte.views import comptes

app_name = CompteConfig.name
urlpatterns = [
    path("", comptes.CompteListView.as_view(), name="index"),
    # Report
    path("create/",comptes.CompteCreateView.as_view(),name="comptes_create"),
    path('<int:pk>/update/', comptes.CompteUpdateView.as_view(),name='comptes_update'),
    path('<int:pk>/delete/', comptes.CompteDeleteView.as_view(), name='comptes_delete'),
    path('<int:pk>/', comptes.CompteDetailView.as_view(), name='comptes_detail'),
]