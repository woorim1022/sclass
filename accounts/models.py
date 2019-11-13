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
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"\d{3}-\d{3,4}-\d{4}",
                message='010-1234-5678 형식으로 입력하세요.',
            )
        ]
    )

class Scrap(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    my_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Recommend(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)