from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from treatment.models import Description
from treatment.models import WaitingRoom
from django.conf import settings
from rest_framework.response import Response
from django.core import serializers
from .serializers import PatientSerializer, DescriptionSerializer
import json
import requests
import logging
import hashlib
# Create your views here.


logger = logging.getLogger(__name__)


@api_view(['POST'])
def description(request):
    
    res = json.loads(request.body) # Patient 로 이름
    # Authorization에 토큰을 넣어주세요  Bearer manm_8uKTUNVw-b_1aTRkZZsbLE_OVox4J_Y8Ao9dJcAAAF10YgdEw 요롷게
    Authorization = request.headers.get('Authorization')

    #인증 실패시
    #res = JsonResponse({"message" : "Authorization fail"}, status=401)
    
    try:
        descriptions = Description.objects.all().order_by('-created_at').first()
    
    except:
        res = JsonResponse({"message" : "can't write"}, status=400)
        return res
    descriptions_str =  "담당 의사 : " + str(descriptions.doctor.name)
    descriptions_str += "\n환자  성명 : " + str(descriptions.patient.name)
    descriptions_str += "\n증상 : " + str(descriptions.patient_say)
    descriptions_str += "\n진단 내용 : " + str(descriptions.doctor_say)
    logger.info(descriptions_str)
    logger.error(descriptions_str)


 

    post = {
        "object_type" : "text",
        "text" : descriptions_str,
        "link" : {
            "web_url" : "https://mrkevinna.github.io", 
            "mobile_web_url" : "https://mrkevinna.github.io"
            },
        "button_title" : "진료기록 바로가기"
    }

    
    data = {
        "template_object" : json.dumps(post)
    }
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': Authorization
        }
    send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    result = requests.post(url=send_url, headers = headers, data = data)
    
    enc = hashlib.md5()
    enc.update(res['Patient'].encode('utf-8'))
    encText = enc.hexdigest()


    WaitingRoom.objects.filter(room_number=encText).delete()

    return Response(result)



    
@api_view(['GET'])
def view_description(request):
    
    Authorization = request.headers.get('Authorization')

    #인증 실패시
    #res = JsonResponse({"message" : "Authorization fail"}, status=401)
    
    try:
        descriptions = Description.objects.all().order_by('-created_at')
    except:
        return JsonResponse(status = 404)


    ser = DescriptionSerializer(data=descriptions, many=True)
    ser.is_valid()
    

    return JsonResponse(ser.data,status=200, safe=False)
