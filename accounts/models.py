from django.db import models
from django.contrib.auth.models import AbstractUser
from classregister.models import Class
from storeregister.models import Store
from django.core.validators import RegexValidator
from django.conf import settings


# Create your models here.
class User(AbstractUser):
   seller = models.BooleanField(default=False)
   phone = models.CharField(
        null=True,
        blank=True,
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"\d{3}-\d{3,4}-\d{4}",
                message='010-1234-5678 형식으로 입력하세요.',
            )
        ]
    )
<<<<<<< HEAD
=======

    
>>>>>>> origin/woorim
