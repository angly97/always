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
    newAnimal.owner_id = request.user
    newAnimal.save()
    
    return redirect('../animal_category/'+category)  

def letterBox(request):
    animals = Animal.objects.filter(owner_id = request.user.id)

    nomal_animals = [animal for animal in animals if animal.category == 'nomal']
    free_animals = [animal for animal in animals if animal.category == 'free']
    honor_animals = [animal for animal in animals if animal.category == 'honor']

    page = request.GET.get('page')
    paginator = Paginator(animals, 16)
    animals = paginator.get_page(page)
    
    normal_paginator = Paginator(nomal_animals, 16)
    nomal_animals = normal_paginator.get_page(page)
    
    free_paginator = Paginator(free_animals, 16)
    free_animals = free_paginator.get_page(page)

    honor_paginator = Paginator(honor_animals, 16)
    honor_animals = honor_paginator.get_page(page)

    return render(request, 'letterBox.html', {'animals':animals, 'nomal_animals':nomal_animals, 'free_animals': free_animals, 'honor_animals':honor_animals ,
    'empty_num':4-len(animals)%4, 'normal_empty_num':4-len(nomal_animals)%4 , 'free_empty_num':4-len(free_animals)%4, 'honor_empty_num':4-len(honor_animals)%4 })

def animalPage(request, animal_id):
    animal = get_object_or_404(Animal, animal_id=animal_id)
    messages = Message.objects.filter(animal_id = animal_id).all()
    return render(request, "animal_page.html",{'animal':animal, 'messages': messages})

def deleteAnimal(request, animal_id):
    animal = get_object_or_404(Animal, pk = animal_id)
    animal.delete()
    return redirect('letterBox')

def send(request, animal_id):
    newMessage = Message()

    temp_id = Message.objects.count()
    newMessage.message_id = temp_id +1 if temp_id != 0 else 1
    newMessage.writer = request.user
    newMessage.animal = Animal.objects.get(animal_id = animal_id)
    newMessage.content = request.POST['content']
    newMessage.pub_date = datetime.now()
    newMessage.save()
    
    return redirect('../animal_page/'+str(animal_id))

def deleteMessage(request, animal_id, message_id):
    message = get_object_or_404(Message, pk = message_id)
    message.delete()
    return redirect('../../animal_page/'+str(animal_id))

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