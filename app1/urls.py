from django.contrib import admin
from django.urls import path,include
from .views import LamdaHandler,DueListCreateView, InstallmentListCreateView, PaymentListCreateView, InvoiceListCreateView, TransactionListCreateView



urlpatterns = [
   path('', LamdaHandler.as_view()),
   path('dues/', DueListCreateView.as_view(), name='due-list-create'),
    path('installments/', InstallmentListCreateView.as_view(), name='installment-list-create'),
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
]