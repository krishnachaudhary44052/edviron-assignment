from rest_framework import serializers
from .models import FeeHead,Due,Installment,Invoice,Payment,Transaction

class FeeHeadSerializers(serializers.ModelSerializer):

    class Meta:
        model = FeeHead
        fields = '__all__'

class DueSerializers(serializers.ModelSerializer):

    class Meta:
        model = Due
        fields = '__all__'

class InstallmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Installment
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'

class TransactionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'

