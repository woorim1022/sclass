from django.db import models
from django.conf import settings
from storeregister.models import Store

# Create your models here.
class Class(models.Model):
    CATEGORY = (
      ('요리', '요리'),
        ('수공예', '수공예'),
        ('꽃', '꽃'),
        ('미술', '미술'),
        ('음악', '음악'),
        ('미용', '미용'),
        ('운동', '운동'),
        ('커피/차', '커피/차'),
    )
    owner_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    class_title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    describe = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField()
    category = models.CharField(max_length=10, choices=CATEGORY) # 미정
    current_number = models.IntegerField()
    max_number = models.IntegerField()
    img1 = models.ImageField(null=True,blank=True)
    img2 = models.ImageField(null=True,blank=True)
    img3 = models.ImageField(null=True,blank=True)
    img4 = models.ImageField(null=True,blank=True)
    img5 = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.class_title

class Scrap(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    my_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    rate = models.IntegerField(default=5)
    content = models.TextField(max_length=500, blank=True)