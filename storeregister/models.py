from django.db import models

# Create your models here.
class Store(models.Model):
    REGION_CHOICES = (
		('GN', '강남구'),
        ('SC', '서초구'),
        ('YS', '용산구'),
    )
    store_title = models.CharField(max_length=100)
    region = models.CharField(max_length=200, choices=REGION_CHOICES)
    address = models.TextField()
    detailaddr = models.TextField(max_length=200)
    homepage = models.URLField(max_length=200)
    #photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    describe = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

