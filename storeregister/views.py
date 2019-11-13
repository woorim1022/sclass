from django.shortcuts import render
# Create your views here.
def store_list(request):                     
    return render(request, 'storeregister/store_list.html')

def detail(request, store_id):
    return render(request, 'storeregister/store_detail.html')

def register(request):
    return render(request, 'storeregister/store_register.html')

def storeupdate(request, store_id):
    return render(request, 'storeregister/store_edit.html')

def delete(request, store_id):
    return render(request, 'storeregister/store_list.html')

def scrap(request, store_id):
    return render(request, 'storeregister/store_detail.html')



