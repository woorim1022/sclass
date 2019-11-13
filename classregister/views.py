from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'classregister/home.html')

def class_list(request):
    return render(request, 'classregister/class_list.html')

def detail(request, class_id):
    return render(request, 'classregister/class_detail.html')

def register(request):
    return render(request, 'classregister/class_register.html')

def classupdate(request, class_id):
    return render(request, 'classregister/class_edit.html')

def delete(request, class_id):
    return render(request, 'classregister/class_detail.html')

def result(request):
    return render(request, 'classregister/class_result.html')

def scrap(request, class_id):
    return render(request, 'classregister/class_detail.html')

def recommend(request, class_id):
    return render(request, 'classregister/class_detail.html')

def review(request, class_id):
    return render(request, 'classregister/class_detail.html')