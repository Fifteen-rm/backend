from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from treatment.models import Description
import json
# Create your views here.

@api_view(['POST'])
def description(request):
    
    Authorization = request.headers.get('Authorization')

    #인증 실패시
    #res = JsonResponse({"message" : "Authorization fail"}, status=401)
    
    try:
        descriptions = Description.objects.all().order_by('-created_at')[0]

    except:
        res = JsonResponse({"message" : "can't write"}, status=400)
    
    return res
