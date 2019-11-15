from django.contrib import admin
from django.urls import path
from . import views

app_name = 'classregister'

urlpatterns = [
    path('list/', views.class_list, name='list'),                                  #클래스리스트
    path('<int:class_id>/', views.detail, name='detail'),                          #클래스상세
    path('register/', views.register, name='register'),                            #클래스등록
    path('classupdate/<int:class_id>/', views.classupdate, name='classupdate'),    #클래스수정
    path('delete/<int:class_id>/', views.delete, name='delete'),                   #클래스삭제
    path('search/', views.search, name='search'),                                  #필터링결과
    path('scrap/<int:class_id>/', views.scrap, name='scrap'),                      #스크랩
    path('recommend/<int:class_id>/', views.recommend, name='recommend'),          #추천
    path('review/<int:class_id>/', views.review, name='review'),                   #리뷰
]