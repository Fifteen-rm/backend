from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import hashlib 
from rest_framework import status


# Create your views here.


@api_view(['POST'])
def login(request):
    # authServer로 요청 보내기!

    # Serialize로 리턴 데이터 만들기

    # 리턴
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def createroom(request):
    res = json.loads(request.body)
    print(res['identity'])
    
    enc = hashlib.md5()
    enc.update(res['identity'].encode('utf-8'))
    encText = enc.hexdigest()
    print(encText)

    
    """
    #대충 DB관련 중복검사 및 insert 
    #
    #
    #
    """ 
    
    return Response(status=status.HTTP_200_OK)
    
@api_view(['POST'])
def joinroom(request):
    res = json.loads(request.body)
    print(res['identity'])    
    
    
    """
    #대충 DB관련 데이터 검사 select
    #
    #
    #
    """        
    roomnumber = 123
    return Response(roomnumber,status=status.HTTP_200_OK)
    
