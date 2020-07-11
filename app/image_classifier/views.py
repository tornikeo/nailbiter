from django.shortcuts import render
from django.http import JsonResponse
from .model.serving import predict
import json
# Create your views here.
# Request is of format 
# {
#  "image":[[]]
# }

SERVER_URL = 'http://localhost:8501/v1/models/model:predict'

def get_image_classification(request):
    prediction = predict([
        json.loads(request.GET['instances'])
    ])

    return JsonResponse(prediction)