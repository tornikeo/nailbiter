from django.urls import path, include
from image_classifier.views import get_image_classification

urlpatterns = [
    path('image_classifier', get_image_classification, name='image_classifier')
]
