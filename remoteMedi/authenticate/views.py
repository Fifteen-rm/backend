from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import redirect
import requests
from django.conf import settings
import json

# Create your views here.

@api_view(['POST'])
def login(request):
    response = requests.post(url = settings.AUTH_SERVER_LOGIN, data=request.body, headers = {"content-type": "application/json"} )
    return Response(json.loads(response.content), status=response.status_code)

@api_view(['GET'])
def authenticate(request):
    response = requests.get(url = settings.AUTH_SERVER_AUTHENTICATE, headers = request.headers)    
    return Response(status=response.status_code)

@api_view(['DELETE'])
def logout(request):
    response = requests.delete(url = settings.AUTH_SERVER_LOGOUT, data = request.body, headers = {"content-type": "application/json"} )    
    return Response(json.loads(response.content), status=response.status_code)


@api_view(['POST'])
def token(request):
    response = requests.post(url = settings.AUTH_SERVER_TOKEN, data = request.body, headers = {"content-type": "application/json"} )    
    return Response(json.loads(response.content), status=response.status_code)

@api_view(['GET'])
def kakaologin(request):
    client_id = settings.KAKAO_API
    redirect_uri = f"{settings.HOST}/authenticate/kakao/auth"
    print(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")
    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")

def kakaoauth(request):
    code = request.GET['code']
    client_id = settings.KAKAO_API
    redirect_uri = f"{settings.HOST}/authenticate/kakao/auth"
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    client_secret = settings.KAKAO_SECRET

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
    access_token_request_uri += "&client_secret=" + client_secret

    try:
        token_request = requests.get(access_token_request_uri)
    except Exception as e:
        return JsonResponse({"message" : "failed"}, status=500)
    
    token_json = token_request.json()
    res = JsonResponse({"message" : "ok", "token" : token_json}, status=200)

    res.set_cookie('access_token', token_json['access_token'])
    res.set_cookie('refresh_token',token_json['refresh_token'])
    
    return res; 
    
    
@api_view(['POST'])
def kakaologout(request):
    Authorization = json.loads(request.body)

    logout_url = "https://kapi.kakao.com/v1/user/logout"

    logout_id = requests.post(url=logout_url, headers = Authorization)

    return Response(json.loads(logout_id.content) , status=logout_id.status_code)


@api_view(['GET'])
def redirect_test(request):
    return redirect("https://www.naver.com")

@api_view(['POST'])
def kakaosendmsg(request):
    client_id = settings.KAKAO_API
    Authorization = request.headers.get('Authorization')
    print(Authorization)
    
    print("============raw body========")
    print(request.body)

    print("============load body==========")
    print(json.loads(request.body))

    print("=============load -> dump body")
    print(type(json.dumps(json.loads(request.body))))
    data = {
        "template_object" : json.dumps(json.loads(request.body))
    }
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization':Authorization
        }
    send_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    result = requests.post(url=send_url, headers = headers, data = data)

    return Response(result)
