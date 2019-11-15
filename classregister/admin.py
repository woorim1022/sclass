from django.contrib import admin
from .models import Class, Book, Review, Scrap

# Register your models here.
admin.site.register(Class)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Scrap)