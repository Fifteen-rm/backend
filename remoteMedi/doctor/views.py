from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from treatment.models import Description
from .models import Doctor
from patient.models import Patient
import json
# Create your views here.

@api_view(['POST'])
def description(request):
    
    Authorization = request.headers.get('Authorization')
    body = json.loads(request.body)

    print("Autorization : ",Authorization)
    print("body : ", body)

    patient = body['patient']
    doctor = body['doctor']

    print(Doctor.objects.get(name=doctor))


    #인증 실패시
    #res = JsonResponse({"message" : "Authorization fail"}, status=401)

    try:
        descriptions = Description(doctor = Doctor.objects.get(name=doctor), patient = Patient.objects.get(name=patient),
                             patient_say = body['patient_say'], doctor_say = body['doctor_say'])
        descriptions.save()
        res = JsonResponse({"message" : "ok"}, status=201)
    except:
        res = JsonResponse({"message" : "can't write"}, status=400)
    
    return res

