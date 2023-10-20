from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

# Create your views here.
from .models import FeeHead,Due,Installment,Invoice,Transaction,Payment
from .serializers import FeeHeadSerializers,DueSerializers,InstallmentSerializers,InvoiceSerializers,TransactionSerializers,PaymentSerializers


class LamdaHandler(APIView):
    renderer_classes = [JSONRenderer]  # Set the accepted renderer to JSONRenderer

    def get(self, request):
        defaulters = Due.objects.filter(start_date__lt=timezone.now())  
        defaulter_list = [due.student.name for due in defaulters]
        respone = {
            "defaulters_list": defaulter_list
        }
        return Response(respone, status=status.HTTP_200_OK)
        # return Response(data)

class DueListCreateView(generics.ListCreateAPIView):
    queryset = Due.objects.all()
    serializer_class = DueSerializers

class InstallmentListCreateView(generics.ListCreateAPIView):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializers

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers

class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializers

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializers
