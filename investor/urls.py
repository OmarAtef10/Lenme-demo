from rest_framework import routers

from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.InvestorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addOffer/<str:investorName>/', views.addOffer, name='add-offer')
]
