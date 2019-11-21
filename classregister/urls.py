from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'classregister'

urlpatterns = [
    path('list/', views.class_list, name='list'),                                  #클래스리스트
    path('<int:class_id>/', views.detail, name='detail'),                          #클래스상세
    path('register/', views.register, name='register'),                            #클래스등록
    path('classupdate/<int:class_id>/', views.classupdate, name='classupdate'),    #클래스수정
    path('delete/<int:class_id>/', views.delete, name='delete'),                   #클래스삭제
    path('search/', views.search, name='search'),                                  #필터링결과
    path('scrap/<int:class_id>/', views.scrap, name='scrap'),  
    path('participate/<int:class_id>/', views.participate, name='participate'),                     #스크랩
    path('recommend/<int:class_id>/', views.recommend, name='recommend'),          #추천
    path('review/<int:review_id>/', views.delete_review, name='deletereview'),                   #리뷰
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)