from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LoanSerializer
from .models import Loan


# Create your views here.

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by('id')
    serializer_class = LoanSerializer
