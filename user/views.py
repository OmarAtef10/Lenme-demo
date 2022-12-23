from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view

from offer.models import Offer
from .serializers import UserSerializer
from .models import User, Installemnts
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
        loan.total_amount = loan.amount + ((loan.amount * ((offer.interest_rate / 100))) * loan.loan_period / 12) + 3
        loan.return_date = datetime.now() + relativedelta(months=+loan.loan_period)
        loan.status = "FUNDED"
        loan.investor = offer.investor
        loan.save()
        investor = offer.investor
        investor.balance -= (loan.amount + 3)
        investor.save()
        addInstallments(loan)
        return JsonResponse({"Success": "Offer Accepted!"})


def addInstallments(loan):
    amount = loan.total_amount / loan.loan_period
    for i in range(1, loan.loan_period + 1):
        installment = Installemnts(loan=loan, amount=amount, loan_month=i,
                                   pay_day=datetime.now() + relativedelta(months=+loan.loan_period))
        installment.save()


@api_view(['GET'])
def pay_month_installment(request, userName, month):
    user = User.objects.get(name=userName)
    if user.loan == None:
        return JsonResponse({"Error": "User Doesn't Have Any Active Loans"})
    installments = list(Installemnts.objects.filter(loan=user.loan))
    if len(installments) == 0:
        loan = user.loan
        loan.status = "COMPLETED"
        loan.save()
        user.loan = None
        user.save()
        return JsonResponse({"Error": f"No installments Available and Loan Status is now COMPLETED"})
    for month_installment in installments:
        date = datetime.now() + relativedelta(months=+month_installment.loan_month)
        date = date.month
        if month == date:
            amount = month_installment.amount
            investor = user.loan.investor
            investor.balance += amount
            investor.save()
            month_installment.delete()
            installments.remove(month_installment)
            if len(installments) == 0:
                loan = user.loan
                loan.status = "COMPLETED"
                loan.save()
                user.loan = None
                user.save()
                return JsonResponse(
                    {"Success": f"Paid installment for month {month} with amount {amount} and Loan Status is now "
                                f"COMPLETED"})
            return JsonResponse({"Success": f"Paid installment for month {month} with amount {amount}"})
        return JsonResponse({"Error": "Month Not Found"})


@api_view(['GET'])
def pay_all_installment(request, userName):
    user = User.objects.get(name=userName)
    if user.loan == None:
        return JsonResponse({"Error": "User Doesn't Have Any Active Loans"})
    installments = list(Installemnts.objects.filter(loan=user.loan))
    if len(installments) == 0:
        loan = user.loan
        loan.status = "COMPLETED"
        loan.save()
        user.loan = None
        user.save()
        return JsonResponse({"Error": f"No installments Available and Loan Status is now COMPLETED"})
    else:
        amount = 0
        for installment in installments:
            amount += installment.amount
            installment.delete()
        loan = user.loan
        loan.status = 'COMPLETED'
        loan.save()
        investor = user.loan.investor
        investor.balance += amount
        investor.save()
        user.loan = None
        user.save()
        return JsonResponse({"Success": f"All Installments Paid Loan total value {amount} Status is COMPLETED"})
