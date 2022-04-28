from django.shortcuts import render
from django.shortcuts import redirect
from adminapp.models import Catdb
from userapp.models import Regidb
from userapp.models import Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    ucount=Regidb.objects.all().count()
    ucount1=Contactdb.objects.all().count()
    ucount2=Catdb.objects.all().count()
   
    return render(request, 'index.html',{'ucount':ucount,'ucount1':ucount1,'ucount2':ucount2})
    return render(request,'index.html')
def addcat(request):
    return render(request, 'add_cat.html')
def getcat(request):
    if request.method == 'POST':
        img_a=request.FILES['img']
        name_a=request.POST.get('name')
        descrip_a=request.POST.get('description')
        data=Catdb(name=name_a,description=descrip_a,img=img_a)
        data.save()
    return redirect('addcat')
def viewcat(request):
    obj = Catdb.objects.all()
    return render(request,'view_cat.html',{'obj':obj})

def adlogin(request):
    return render(request, 'adlogin.html')
def getadlogin(request):
    username_a=request.POST.get('username')
    password_a=request.POST.get('password')
    print(username_a)
    print(password_a)
    if User.objects.filter(username__contains=username_a).exists():
        user=authenticate(username=username_a,password=password_a)
        if user is not None:
            login(request,user)
            request.session['username'] = username_a
            request.session['password'] = password_a
            print(user)
            return redirect('index')
        else:
            return redirect('adlogin')
    else:
        return redirect('adlogin')
def viewreg(request):
    obj=Regidb.objects.filter(status=0)
    return render(request,'view_reg.html',{'obj':obj})
def accept(request,id):
    obj = Regidb.objects.filter(id=id).update(status=1)
    return redirect('viewreg')
def decline(request,id):
    Regidb.objects.get(id=id).delete()
    return redirect('viewreg')
def contact_view(request):
    obj=Contactdb.objects.all()
    return render(request,'contact_view.html',{'obj':obj})



