from django.db import models

# Create your models here.

class FeeHead(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    frequency_months = models.PositiveIntegerField()

class Due(models.Model):
    fee_head = models.ForeignKey(FeeHead, on_delete=models.CASCADE)
    start_date = models.DateField()

class Installment(models.Model):
    dues = models.ManyToManyField(Due)
    due_date = models.DateField()

class Payment(models.Model):
    due = models.ForeignKey(Due, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

class Invoice(models.Model):
    dues = models.ManyToManyField(Due)
    status = models.CharField(max_length=20)

class Transaction(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

