from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('accountbase/', views.accountbase, name='accountbase'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('profile_show/', views.profile_show, name='profile_show'),
    path('signup_complete/', views.signup_complete, name="signup_complete"),
    path('mypage/', views.mypage, name='mypage'),
    path('my_scrap/', views.my_scrap, name='my_scrap'),
    path('my_review/', views.my_review, name='my_review'),
    path('my_recommend/', views.my_recommend, name='my_recommend'),
    path('my_consult/', views.my_consult, name='my_consult'),
    path('my_store/', views.my_store, name='my_store'),
    path('my_class/', views.my_class, name='my_class'),
    path('my_student/', views.my_student, name='my_student'),
]