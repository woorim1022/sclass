from django.contrib import admin
from .models import User, Recommend, Scrap

# Register your models here.
admin.site.register(User)
admin.site.register(Recommend)
admin.site.register(Scrap)