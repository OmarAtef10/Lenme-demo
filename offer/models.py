from django.db import models
from investor.models import Investor
from loan.models import Loan


# Create your models here.
class Offer(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    interest_rate = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('investor', 'loan',)

    def __str__(self):
        return f"Offer from {self.investor.name} on loan {self.loan.id}"
