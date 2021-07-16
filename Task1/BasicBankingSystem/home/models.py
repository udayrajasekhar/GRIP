from django.db import models
from django.utils import timezone
# Create your models here.

class Accounts(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    dateOfBirth = models.DateField()
    balance = models.IntegerField()
    accountNumber = models.CharField(max_length = 5,default=' ')
    def __str__(self):
        return self.firstName+" "+self.lastName

class Transaction(models.Model):
    TransactionId = models.CharField(max_length=10)
    FromAccNo = models.CharField(max_length=5)
    ToAccNo = models.CharField(max_length=5)
    Amount = models.IntegerField()
    dateTime = models.DateField(default=timezone.now)
    def __str__(self):
        return self.TransactionId

