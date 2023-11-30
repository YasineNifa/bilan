from django.urls import path

from compte.apps import CompteConfig
from compte.views import comptes, transactions

app_name = CompteConfig.name
urlpatterns = [
    path("", comptes.CompteListView.as_view(), name="index"),
    # Comptes
    path("create/",comptes.CompteCreateView.as_view(),name="comptes_create"),
    path('<int:pk>/update/', comptes.CompteUpdateView.as_view(),name='comptes_update'),
    path('<int:pk>/delete/', comptes.CompteDeleteView.as_view(), name='comptes_delete'),
    path('<int:pk>/', comptes.CompteDetailView.as_view(), name='comptes_detail'),
    # Transactions
    path("transaction/",transactions.TransactionListView.as_view(),name="transactions_list"),
    path("transaction/create/",transactions.TransactionCreateView.as_view(),name="transactions_create"),
    path('transaction/<int:pk>/update/', transactions.TransactionUpdateView.as_view(),name='transactions_update'),
    path('transaction/<int:pk>/delete/', transactions.TransactionDeleteView.as_view(), name='transactions_delete'),
    # path('transaction/<int:pk>/', comptes.CompteDetailView.as_view(), name='comptes_detail'),

]