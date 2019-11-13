from django.shortcuts import render

# Create your views here.

def accountbase(request):
    return render(request, 'accounts/accountbase.html')

def login(request):
    return render(request, 'accounts/login.html')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def my_class(request):
    return render(request, 'accounts/my_class.html')

def my_consult(request):
    return render(request, 'accounts/my_consult.html')

def my_recommend(request):
    return render(request, 'accounts/my_recommend.html')

def my_review(request):
    return render(request, 'accounts/my_review.html')
    
def my_scrap(request):
    return render(request, 'accounts/my_scrap.html') 

def my_store(request):
    return render(request, 'accounts/my_store.html') 

def my_student(request):
    return render(request, 'accounts/my_student.html') 

def profile_edit(request):
    return render(request, 'accounts/profile_dedit.html') 

def profile_show(request):
    return render(request, 'accounts/profile_show.html') 

def signup(request):
    return render(request, 'accounts/signup.html') 

def signup_complete(request):
    return render(request, 'accounts/signup_complete.html') 

def logout(request):
    return render(request, 'accounts/signup.html')
    