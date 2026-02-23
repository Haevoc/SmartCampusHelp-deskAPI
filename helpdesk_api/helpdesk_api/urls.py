from django.contrib import admin
from django.urls import path
from tickets.views import ticket_list, ticket_detail
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', ticket_list),
    path('tickets/<int:id>/', ticket_detail),
    path('api/token/', TokenObtainPairView.as_view()),
]
