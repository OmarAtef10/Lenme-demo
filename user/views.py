from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view

from offer.models import Offer
from .serializers import UserSerializer
from .models import User
from loan.models import Loan
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


@csrf_exempt
@api_view(['POST'])
def postLoan(request, userName):
    user = User.objects.get(name=userName)
    if user.loan != None:
        return JsonResponse({"Error": "You Already have an active loan"})
    else:
        amount = request.data['amount']
        loan_period = request.data['loan_period']
        print(amount)
        loan = Loan(amount=amount, loan_period=loan_period)
        loan.save()
        user.loan = loan
        user.save()
        return JsonResponse({"Success": "Loan Request Added Successfully"})


@api_view(['get'])
def getOffers(request, userName):
    user = User.objects.get(name=userName)
    print(user.loan)
    offers = list(Offer.objects.filter(loan=user.loan))
    res = {"Offers": []}
    for offer in offers:
        temp = {"ID": offer.id, "investor": offer.investor.name, "Interest": offer.interest_rate}
        res["Offers"].append(temp)
    return JsonResponse(res)


@csrf_exempt
@api_view(['GET'])
def acceptOffer(request, userName, offerId):
    user = User.objects.get(name=userName)
    offer = Offer.objects.get(pk=offerId)
    if offer.loan != user.loan:
        return JsonResponse({"Error": "Invalid Offer"})
    if user.loan.status == "FUNDED":
        return JsonResponse({"Error": "Loan Already Funded!"})
    else:
        loan = user.loan
        loan.total_amount = loan.amount + ((loan.amount * ((offer.interest_rate/100))) * loan.loan_period/12) + 3
        loan.return_date = datetime.now() + relativedelta(months=+loan.loan_period)
        loan.status = "FUNDED"
        loan.investor = offer.investor
        loan.save()
        investor = offer.investor
        investor.balance -= (loan.amount + 3)
        investor.save()
        return JsonResponse({"Success": "Offer Accepted!"})

#TODO installments!!