from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def get_image_classification(request):
    return JsonResponse({
        'prediction':[.5, .5],
        'status':'ok'
    })