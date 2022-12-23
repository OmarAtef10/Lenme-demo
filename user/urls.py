from rest_framework import routers

from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('addLoan/<str:userName>/', views.postLoan, name="post-loan"),
    path('allOffers/<str:userName>/', views.getOffers, name="get-offer"),
    path('acceptOffer/<str:userName>/<int:offerId>/', views.acceptOffer, name="accept-offer"),
    path('payMonth/<str:userName>/<int:month>/', views.pay_month_installment, name="pay-month"),
    path('payAll/<str:userName>/', views.pay_all_installment, name="pay-all"),
]
