from django.db import models
from loan.models import Loan


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    loan = models.OneToOneField(Loan, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
