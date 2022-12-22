from django.db import models


# Create your models here.
class Investor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.PositiveIntegerField(default=0)
