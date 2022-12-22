from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OfferSerializer
from .models import Offer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('id')
    serializer_class = OfferSerializer


