from django.db import models
from user.models import User
    
class Animal(models.Model):
    animal_id = models.IntegerField(primary_key=True)                               # 동물 고유 id
    name = models.CharField(max_length=50)                                          # 동물 이름
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)         # 주인 id
    category = models.CharField(max_length=50)                                      # 카테고리 
    species = models.CharField(max_length=50)                                       # 상위 종류
    subspecies = models.CharField(max_length=50, null=True)                         # 하위 종류
    profile_photo = models.ImageField(upload_to='profile_photo/', null=True)        # 프로필 사진
    birthday = models.DateField(null=True)                                          # 탄생일
    memorialday = models.DateField()                                                # 제삿날
    introduce = models.TextField(null=True)                                         # 소개글
    pub_date = models.DateTimeField(null=True)                                      # 등록시간


class csCenter(models.Model):
    cs_id = models.IntegerField(primary_key=True)  
    title=models.CharField(max_length=100)                  #제목
    text=models.TextField()                                 #내용
    register_date=models.DateField                          #작성날짜
    writer=models.CharField(max_length=50)                  #작성자

