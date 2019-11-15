from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Store
from .forms import StoreForm

# Create your views here.

##리스트 보여주기 (list)
def store_list(request):
    stores = Store.objects               
    return render(request, 'storeregister/store_list.html', {'stores' : stores})

##상세페이지 (R)
def detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'storeregister/store_detail.html', {'store':store})

##스토어 등록 (C)
#@login_required
def register(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')

    else : 
        form=StoreForm()
        return render(request, 'storeregister/store_register.html', {'form':form})


##스토어 수정(U)
#@login_required
def storeupdate(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    if request.method=='POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            store = form.save(commit=False)
            store.save()
            return redirect('detail', store_id=store.pk)    
    else:
        form = StoreForm(instance=store)
        return render(request, 'storeregister/store_edit.html', {'form':form})


##스토어 삭제(D)
#@login_required
def delete(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    return redirect('list')



def result(request) : 
    store_object = Store.objects
    query = request.GET.get('query','')
    if query:
        store_object = store_object.filter(region=query)
        return render(request,'storeregister/store_result.html',{'result':store_object} )