from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from treatment.models import Description
from django.conf import settings
from rest_framework.response import Response
from django.core import serializers
from .serializers import PatientSerializer
import json
import requests
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
    Authorization = request.headers.get('Authorization')

    descriptions_str =  "담당 의사 : " + str(descriptions.doctor)
    descriptions_str += "\n환자 성명 : " + str(descriptions.patient)
    descriptions_str += "\n증상 : " + str(descriptions.patient_say)
    descriptions_str += "\n진단 내용 : " + str(descriptions.doctor_say)
 

    post = {
        "object_type" : "text",
        "text" : descriptions_str,
        "link" : {
            "web_url" : "https://mrkevinna.github.io", 
            "mobile_web_url" : "https://mrkevinna.github.io"
            },
        "button_title" : "Check it out!"
    }

    
    data = {
        "template_object" : json.dumps(post)
    }
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization':Authorization
        }
    send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    result = requests.post(url=send_url, headers = headers, data = data)

    return Response(result)