from django.db import models
from django.conf import settings

# Create your models here.
class Store(models.Model):
    REGION_CHOICES = (
      ('GN', '강남구'),
      ('SC', '서초구'),
      ('YS', '용산구'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_title = models.CharField(max_length=100)
    region = models.CharField(max_length=200, choices=REGION_CHOICES)
    address = models.TextField()
    detailaddr = models.TextField(max_length=200)
    homepage = models.URLField(max_length=200)
    photo = models.ImageField(null=True,blank=True, upload_to='store/')
    describe = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #가게추천
    #recommend_user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Recommend')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
      return self.store_title

class Recommend(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
