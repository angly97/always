from django.urls import path
from .views import *

urlpatterns = [        
    path('login/', login_view, name = "login"),
    path('logout/', logout_view, name= "logout"),
    path('signUp/', signUp, name="signUp"),
    path('idFind/', idFind, name="idFind"),
    path('pwFind/', pwFind, name="pwFind"),
]