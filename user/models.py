from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_name = models.CharField(max_length=50)                    # 실명
    user_nickname = models.CharField(max_length=50, unique=True)   # 닉네임
    user_id = models.CharField(max_length=50, unique=True)         # 아이디
    user_password = models.CharField(max_length=50)                # 비밀번호
    user_phone_number = models.CharField(max_length=12)            # 전화번호
