from django.urls import path
from .views import login
from .views import createroom
from .views import joinroom

urlpatterns = [
    path('login/', login),
    path('api/createroom', createroom),
    path('api/joinroom', joinroom),
]
