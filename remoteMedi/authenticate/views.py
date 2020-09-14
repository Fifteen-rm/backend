from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    redirect_uri = "http://127.0.0.1:8000/authenticate/kakaoauth"

    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")
    

@api_view(['GET'])
def kakaoauth(request):
    code = request.GET['code']
    client_id = settings.KAKAO_API
    redirect_uri = "http://127.0.0.1:8000/authenticate/kakaoauth"
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    client_secret = settings.KAKAO_SECRET

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
    access_token_request_uri += "&client_secret=" + client_secret

    print(access_token_request_uri)
    token_request = requests.get(access_token_request_uri)

    #if token_request.status_code == 200:
    print(token_request.json())

    return Response(token_request.json())
    
    

@api_view(['POST'])
def kakaologout(request):
    client_id = settings.KAKAO_API
    Authorization = json.loads(request.body)

    print(Authorization)
    logout_url = "https://kapi.kakao.com/v1/user/logout"

    
    logout_id = requests.post(url=logout_url, headers = Authorization)
    print(json.loads(logout_id.content))
    return Response(json.loads(logout_id.content) , status = logout_id.status_code)

def kakaologin(request):
    client_id = settings.KAKAO_API
    redirect_uri = "http://127.0.0.1:8000/authenticate/kakaoauth"

    return redirect(f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code")
    

@api_view(['GET'])
def kakaoauth(request):
    code = request.GET['code']
    client_id = settings.KAKAO_API
    redirect_uri = "http://127.0.0.1:8000/authenticate/kakaoauth"
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"
    client_secret = settings.KAKAO_SECRET

    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code
    access_token_request_uri += "&client_secret=" + client_secret

    print(access_token_request_uri)
    token_request = requests.get(access_token_request_uri)

    #if token_request.status_code == 200:
    print(token_request.json())

    return Response(token_request.json())
    
    

@api_view(['POST'])
def kakaologout(request):
    client_id = settings.KAKAO_API
    Authorization = json.loads(request.body)

    print(Authorization)
    logout_url = "https://kapi.kakao.com/v1/user/logout"

    
    logout_id = requests.post(url=logout_url, headers = Authorization)
    print(json.loads(logout_id.content))
    return Response(json.loads(logout_id.content) , status = logout_id.status_code)
