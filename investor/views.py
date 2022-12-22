from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view

from offer.models import Offer
from .serializers import InvestorSerializer
from .models import Investor
from loan.models import Loan


# Create your views here.

class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all().order_by('id')
    serializer_class = InvestorSerializer


@csrf_exempt
@api_view(['POST'])
def addOffer(request, investorName):
    investor = Investor.objects.get(name=investorName)
    loan_id = request.data['loan_id']
    loan = Loan.objects.get(pk=loan_id)
    if loan.amount+3 > investor.balance:
        return JsonResponse({"Forbidden": "Insufficient balance"})
    else:
        interest = request.data['interest']
        try:
            offer = Offer(investor=investor, interest_rate=interest, loan=loan)
            offer.save()
            return JsonResponse({"Success": "Offer Added!"})
        except:
            return JsonResponse({"Error": "Offer Already Exits!"})
