from django.db import models
from loan.models import Loan


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    loan = models.OneToOneField(Loan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Installemnts(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    loan_month = models.PositiveIntegerField()
    pay_day = models.DateField()

    def __str__(self):
        return f"{self.loan_month} for {self.loan}"
