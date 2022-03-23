from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import * 
from django.core.paginator import Paginator

def home(request):
    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    day=today[2:]
    
    today_stars = Animal.objects.filter(
        memorialday__month = month,
        memorialday__day = day
    )
    free_animals = Animal.objects.filter(
        category = "free"
    )
    honor_animals = Animal.objects.filter(
        category = "honor"
    )

    return render(request, "home.html",{"month":month, "day":day, 'today_stars': today_stars,
    'free_animals': free_animals, 'honor_animals': honor_animals, 'today_stars_num': len(today_stars),
    'free_animals_num':len(free_animals), 'honor_animals_num':len(honor_animals) })


def honor(request):
    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    month = month.rjust(2, '0')
    day=today[2:]

    # 카테고리가 honor인 동물들만 가져와 honor_animals에 저장
    honor_animals = Animal.objects.filter(
        category = "honor"
    )

    # 오늘 월/일에 죽은 동물들만 가져와 today_starts에 저장
    today_stars = Animal.objects.filter(
        category = "honor",
        memorialday__month = month,
        memorialday__day = day
    )
   
    # 한 페이지 당 16마리 동물 보이도록 페이지네이션
    paginator = Paginator(honor_animals, 16)
    page = request.GET.get('page')          # 몇번째 페이지인지 받아옴

    honor_animals = paginator.get_page(page)

    return render(request, "honor.html",{"month":month, "day":day, 'honor_animals': honor_animals,'empty_num':4-len(honor_animals)%4,
     'today_stars': today_stars, 'today_stars_num': len(today_stars)})


def free(request):
    # 오늘 월, 일 계산
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    month = month.rjust(2, '0')
    day=today[2:]

    # 카테고리가 free인 동물들만 가져와 free_animals에 저장
    free_animals = Animal.objects.filter(
        category = "free"
    )

    # 오늘 월/일에 죽은 동물들만 가져와 today_starts에 저장
    today_stars = Animal.objects.filter(
        category = "free",
        memorialday__month = month,
        memorialday__day = day
    )
   
    # 한 페이지 당 16마리 동물 보이도록 페이지네이션
    paginator = Paginator(free_animals, 16)
    page = request.GET.get('page')          # 몇번째 페이지인지 받아옴

    free_animals = paginator.get_page(page)

    return render(request, "free.html",{"month":month, "day":day, 'free_animals': free_animals,'empty_num':4-len(free_animals)%4,
     'today_stars': today_stars, 'today_stars_num': len(today_stars) })


def freeRegistration(request):
    return render(request, "freeRegistration.html")


def freeRegistered(request):
    newAnimal = Animal()

    temp_id = Animal.objects.count()
    newAnimal.animal_id = temp_id +1 if temp_id != 0 else 1
    newAnimal.category = 'free'
    newAnimal.name = request.POST['animalName']
    newAnimal.species = request.POST['animalType']
    newAnimal.subspecies = request.POST['animalSubType']
    newAnimal.birthday = request.POST['animalBirthDay']
    newAnimal.memorialday = request.POST['animalMemorialDay']
    newAnimal.profile_photo = request.FILES.get('animalImg', None)
    newAnimal.introduce = request.POST['animalInfo']
    newAnimal.pub_date = datetime.now()
    newAnimal.save()
    
    return redirect('free')


def aboutUs(request):
    return render(request, "aboutUs.html")

def searchMap(request):
    return render(request, "searchMap.html")

def searchResult(request):
    searchWord=request.POST['searchInput']
    
    if searchWord == "개": searchWord = "강아지"

    animals = Animal.objects.filter(
        Q(name__contains = searchWord)|
        Q(category__contains = searchWord)|
        Q(species__contains = searchWord)|
        Q(subspecies__contains = searchWord)|
        Q(birthday__contains = searchWord)|
        Q(memorialday__contains = searchWord)|
        Q(introduce__contains = searchWord)
    )
    return render(request, "searchResult.html",{"searchWord":searchWord, "animals":animals
    , "animals_num": len(animals), "empty_num":4-len(animals)%4 })


def normal(request):
    
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    month = month.rjust(2, '0')
    day=today[2:]

    normal_animals = Animal.objects.filter(category = "normal")

    today_stars = Animal.objects.filter(
        category = "normal",
        memorialday__month = month,
        memorialday__day = day
    )

    paginator = Paginator(normal_animals, 16)
    page = request.GET.get('page')
    normal_animals = paginator.get_page(page)

    return render(request, "normal.html",{'normal_animals':normal_animals,'empty_num':4-len(normal_animals)%4,
    "month":month, 'day': day, 'today_stars':today_stars, 'today_stars_num': len(today_stars) })
    

def csCenter(request):
    return render(request, "csCenter.html")    


def q_and_a(request):
    return render(request, "q_and_a.html")    

def idFind(request):
    return render(request, "idFind.html")    
