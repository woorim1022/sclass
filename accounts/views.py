from django.shortcuts import render, redirect
from django.contrib import auth
from .models import User
from classregister.models import Scrap
from storeregister.models import Recommend
from .forms import UserForm
# Create your views here.

def accountbase(request):
    return render(request, 'accounts/accountbase.html')

def signup(request):
    #signup 버튼을 눌렀을 때 일어나야 하는 일
    if request.method == 'POST': #form으로 넘긴 값이 POST 이면
        if request.POST['password1'] == request.POST['password2']:  #비밀번호 두 개가 서로 일치하면
            try:
                user = User.objects.get(username=request.POST['username']) #POST 형식으로 가져온 username 과 일치하는 User 객체의 username을 가져와서 user 변수에 저장
                return render(request, 'accounts/signup.html', {'error':'이미 존재하는 아이디입니다'})
            except User.DoesNotExist:    #username과 일치하는 값을 가진 객체가 없어서 try 를 실행하지 못한 경우
                user = User.objects.create_user(    #User객체 새로 생성 POST로 가져온 username과 password1 필드에 저장
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)         #로그인 실행
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': '비밀번호가 일치하지 않습니다'})
    else: 
        return render(request, 'accounts/signup.html') 


def login(request):
    if request.method == 'POST':    #로그인 버튼을 눌렀을때 
        username = request.POST['username']    #username 저장
        password = request.POST['password']    #password 저장
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:    #사용자가 정보를 알맞게 입력한 경우
            auth.login(request, user)   #로그인 실행
            return redirect('home')     #홈으로 이동
        else:
            return render(request, 'accounts/login.html', {'error': '아이디나 비밀번호가 일치하지 않습니다'})
    else: 
        return render(request, 'accounts/login.html')

def signup_complete(request):
    return render(request, 'accounts/signup_complete.html') 
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def my_class(request):
    return render(request, 'accounts/my_class.html')

def my_consult(request):
    return render(request, 'accounts/my_consult.html')

def my_recommend(request):
    recommends = Recommend.objects.filter(user=request.user)
    return render(request, 'accounts/my_recommend.html', {'recommends': recommends})

def my_review(request):
    return render(request, 'accounts/my_review.html')
    
def my_scrap(request):
    scraps = Scrap.objects.filter(user=request.user)
    return render(request, 'accounts/my_scrap.html', {'scraps': scraps})
    #return render(request, 'accounts/my_scrap.html')

def my_store(request):
    return render(request, 'accounts/my_store.html') 

def my_student(request):
    return render(request, 'accounts/my_student.html') 

def my_enroll(request):
    return render(request, 'accounts/my_enroll.html') 

def profile_edit(request):
    return render(request, 'accounts/profile_edit.html') 

def profile_show(request):
    return render(request, 'accounts/profile_show.html') 

