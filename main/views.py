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


def animal_category(request, category):
    today = DateFormat(datetime.now()).format('md')
    month=today[1] if today[0]=='0' else today[:2]
    month = month.rjust(2, '0')
    day=today[2:]

    animals = Animal.objects.filter(category = category)

    today_stars = Animal.objects.filter(
        category = category,
        memorialday__month = month,
        memorialday__day = day
    )

    paginator = Paginator(animals, 16)
    page = request.GET.get('page')
    animals = paginator.get_page(page)

    return render(request, 'animal_category.html', {'animals':animals, 'category': category,'empty_num':4-len(animals)%4,
    "month":month, 'day': day, 'today_stars':today_stars, 'today_stars_num': len(today_stars) })
    

def registration(request, category):
    return render(request, "registration.html", {'category': category})


def registered(request, category):
    newAnimal = Animal()

    temp_id = Animal.objects.count()
    newAnimal.animal_id = temp_id +1 if temp_id != 0 else 1
    newAnimal.category = category
    newAnimal.name = request.POST['animalName']
    newAnimal.species = request.POST['animalType']
    newAnimal.subspecies = request.POST['animalSubType']
    newAnimal.birthday = request.POST['animalBirthDay']
    newAnimal.memorialday = request.POST['animalMemorialDay']
    newAnimal.profile_photo = request.FILES.get('animalImg', None)
    newAnimal.introduce = request.POST['animalInfo']
    newAnimal.pub_date = datetime.now()
    newAnimal.save()
    
    return redirect(category)


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

def csCenter(request):
    return render(request, "csCenter.html")    

def q_and_a(request):
    return render(request, "q_and_a.html")    

def aboutUs(request):
    return render(request, "aboutUs.html")