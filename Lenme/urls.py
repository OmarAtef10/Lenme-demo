from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('user/', include('user.urls')),
    path('investor/', include('investor.urls')),
    path('loans/', include('loan.urls')),
    path('offers/', include('offer.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'swagger/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='swagger',
    ),

]
