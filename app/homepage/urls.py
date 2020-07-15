from django.urls import path, include
from homepage.views import homepage

urlpatterns = [
    path('', homepage, name='homepage')
]
