from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.store_list, name='list'),                   #가게리스트
    path('<int:store_id>', views.detail, name='detail'),                        #가게상세
    path('register/', views.register, name='register'),                         #가게등록 
    path('storeupdate/<int:store_id>', views.storeupdate, name='storeupate'),   #가게수정
    path('delete/<int:store_id>', views.delete, name='delete'),                 #가게삭제
    path('scrap/<int:class_id>', views.scrap, name='scrap'),                    #스크랩
]