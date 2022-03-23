from atexit import register
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
        
    path('', home, name="home"),
    path('honor/',honor, name="honor"),
    # path('honorRegister1/',honorRegister1, name="honorRegister1"),
    # path('honorRegister2/',honorRegister2, name="honorRegister2"),
    # path('honorRegistered/<str:animal_id>/',honorRegistered, name="honorRegistered"),
    path('free/', free, name="free"),
    path('freeRegistration', freeRegistration, name="freeRegistration"),
    path('freeRegistered', freeRegistered, name="freeRegistered"),
    
    # path('freeRegister1/',freeRegister1, name="freeRegister1"),
    # path('freeRegister2/',freeRegister2, name="freeRegister2"),
    # path('freeRegistered/<str:animal_id>',freeRegistered, name="freeRegistered"),
    path('aboutUs/',aboutUs, name="aboutUs"),
    path('searchMap/',searchMap,name="searchMap"),
    path('searchResult/',searchResult, name='searchResult'),
    
    # path('mypage/<int:animal_id>',mypage,name="mypage"),
    
    # path('mypageDiary/<int:animal_id>',mypageDiary,name="mypageDiary"),
    # path('mypageDiaryCreate/',mypageDiaryCreate,name="mypageDiaryCreate"),
    
    # path('mypagePhoto/<int:animal_id>',mypagePhoto,name="mypagePhoto"),
    # path('mypagePhotoCreate/',mypagePhotoCreate,name="mypagePhotoCreate"),
    
    # path('mypageVisitorBook/<int:animal_id>',mypageVisitorBook,name="mypageVisitorBook"),
    # path('mypageVisitorBookCreate/',mypageVisitorBookCreate,name="mypageVisitorBookCreate"),
    
    
    # path('mypageOption/<int:animal_id>',mypageOption,name="mypageOption"),
    # path('mypageUpdate/<int:animal_id>',mypageUpdate,name="mypageUpdate"),
    
    
    # path('enroll/',enroll, name="enroll"),
    # path('enroll2/',enroll2, name="enroll2"),
    # path('enrolled/<str:animal_id>',enrolled, name="enrolled"),
    # path('caaard/', caaard, name="caaard"),
    path('csCenter/', csCenter, name="csCenter"),
    path('q_and_a/', q_and_a, name="q_and_a"),
    path('idFind/', idFind, name="idFind"),
    # path('pwFind/', pwFind, name="pwFind"),
    path('normal/',normal, name="normal"),
    # path('animal_delete/<int:animal_id>',delete,name="delete"),
]