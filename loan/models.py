from django.db import models
from investor.models import Investor

# Create your models here.

STATUS = {
    ("OPEN", "OPEN"),
    ("FUNDED", "FUNDED"),
    ("COMPLETED", "COMPLETED")
}


class Loan(models.Model):
    amount = models.PositiveIntegerField()
    status = models.CharField(choices=STATUS, default="OPEN", max_length=50)
    investor = models.ForeignKey(Investor, on_delete=models.PROTECT, null=True, blank=True)
    total_amount = models.PositiveIntegerField(default=0)
    loan_period = models.PositiveIntegerField(default=1)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"loan amount {self.amount}"
