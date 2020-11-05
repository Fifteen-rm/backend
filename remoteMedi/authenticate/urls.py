from django.urls import path
from .views import kakaologin
from .views import kakaoauth
from .views import kakaologout
from .views import redirect_test
from .views import login

urlpatterns = [
    path('kakao/auth', kakaoauth),
    path('kakao/login/', kakaologin),
    path('kakao/logout/', kakaologout),
    path('redirect/test/', redirect_test),
    path('login/', login),
]
