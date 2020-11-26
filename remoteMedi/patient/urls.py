from django.urls import path
from .views import description
from .views import view_description

urlpatterns = [
    path('description/', description),
    path('description/all', view_description),

]
