from django.contrib import admin
from .models import Class, Book, Review

# Register your models here.
admin.site.register(Class)
admin.site.register(Book)
admin.site.register(Review)