from django.shortcuts import render
from django.shortcuts import redirect

from userapp.models import Regidb
from userapp.models import Contactdb
from userapp.models import Messagedb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def user(request):
    return render(request,'user.html')
def about(request):
    return render(request, 'about.html')
def gallery(request):
    data = Regidb.objects.filter(status=1,active=0)
    return render(request,'gallery.html',{'data':data})
def bride(request):
    data = Regidb.objects.filter(gender='female',active=0)
    return render(request,'bride.html',{'data':data})
def groom(request):
    data=Regidb.objects.filter(gender='male',active=0)
    return render(request,'groom.html',{'data':data})

def myprofile(request):
    userid = request.session.get('userid')
    obj= Regidb.objects.filter(id=userid)
    return render(request,'myprofile.html',{'obj':obj})
    
def contact(request):
    return render(request, 'contact.html')
def getregi(request):
    if request.method == 'POST':
        xyz_a=request.FILES['xyz']
        username_x=request.POST.get('uname')
        email_x=request.POST.get('email')
        password_x=request.POST.get('upassword')
        age_x=request.POST.get('age')
        gender_x=request.POST.get('gender')
        phonenumber_x=request.POST.get('phonenumber')
        weight_x=request.POST.get('weight')
        profession_x=request.POST.get('profession')
        category_x=request.POST.get('category')
        address_x=request.POST.get('address')
        data=Regidb(uname=username_x,email=email_x,upassword=password_x,age=age_x,gender=gender_x, phonenumber=phonenumber_x,weight=weight_x,profession=profession_x,category=category_x,address=address_x,xyz=xyz_a,status=0,active=0)
        data.save()
    return redirect('loginuser')
def loginuser(request):
        return render(request, 'login1.html') 
def userlogin1(request):
    username_x=request.POST.get('uname')
    password_x=request.POST.get('upassword')
    if Regidb.objects.filter(uname=username_x,upassword=password_x,status=1).exists():
        data=Regidb.objects.filter(uname=username_x,upassword=password_x,status=1).values('email','address','age','gender','phonenumber','weight','profession','category','id').first()
        request.session['email']=data['email']
        request.session['address']=data['address']
        request.session['age']=data['age']
        request.session['gender']=data['gender']
        request.session['phonenumber']=data['phonenumber']
        request.session['weight']=data['weight']
        request.session['profession']=data['profession']
        request.session['category']=data['category']
        request.session['userid']=data['id']
        request.session['username_x']=username_x
        request.session['password_x']=password_x
        if 'userid' in request.session:
            Regidb.objects.filter(uname=username_x,upassword=password_x,status=1).update(active=1)
        
            
        return redirect('user')
    else:
        return render(request, 'login1.html',{'msg':'Invalid User Credentials'})
def getcontact(request):
    if request.method == 'POST':
        msg_a=request.POST.get('message')
        cname_a=request.POST.get('cname')
        cemail_a=request.POST.get('cemail')
        subject_a=request.POST.get('subject')
        data=Contactdb(message=msg_a,cname=cname_a,cemail=cemail_a,subject=subject_a)
        data.save()
    return redirect('contact')
def edit(request,id):
    obj = Regidb.objects.filter(id=id)
    return render(request, 'edit.html',{'obj':obj})
def update(request,id):
    if request.method == 'POST':
        username_c=request.POST.get('uname')
        email_c=request.POST.get('email')
        password_c=request.POST.get('upassword')
        age_c=request.POST.get('age')
        gender_c=request.POST.get('gender')
        phonenumber_c=request.POST.get('phonenumber')
        weight_c=request.POST.get('weight')
        profession_c=request.POST.get('profession')
        category_c=request.POST.get('category')
        address_c=request.POST.get('address')
        
        try:
            xyz_c=request.FILES['xyz']
            fs = FileSystemStorage() 
            file = fs.save(xyz_c.name, xyz_c)
        except MultiValueDictKeyError:
            file=Regidb.objects.get(id=id).xyz  
    Regidb.objects.filter(id=id).update(uname=username_c,email=email_c,upassword=password_c,age=age_c,gender=gender_c,phonenumber=phonenumber_c,weight=weight_c,profession=profession_c,category=category_c,address=address_c,xyz=file)
    return redirect('myprofile')
def userlogout(request):
    userid = request.session.get('userid')
    Regidb.objects.filter(id=userid,status=1).update(active=0)
    del request.session['username_x']
    del request.session['email']
    del request.session['userid']
    del request.session['age']
    del request.session['gender']
    del request.session['phonenumber']
    del request.session['weight']
    del request.session['profession']
    del request.session['category']
    del request.session['password_x']
    return redirect('user')
def view(request,id):
    obj = Regidb.objects.filter(id=id)
    return render(request,'view_profile.html',{'obj':obj})
def getmsg(request):
    if request.method == 'POST':
        msg_c=request.POST.get('msg')
        id_a=request.session.get('userid')
        id_c=request.POST.get('mid')
        data=Messagedb(msg=msg_c,userid=Regidb.objects.get(id=id_a),mid=id_c)
        data.save()
    return redirect('msgtableview')
def msgtableview(request):
    userid = request.session.get('userid')
    obj= Messagedb.objects.filter(userid=userid)
    return render(request,'msg_tableview.html',{'obj':obj})





