from django.urls import path
from.import views
urlpatterns=[
    path('',views.user,name='user'),
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('contact',views.contact,name='contact'),
    path('getregi',views.getregi,name='getregi'),
    path('loginuser',views.loginuser,name='loginuser'),
    path('userlogin1',views.userlogin1,name='userlogin1'),
    path('getcontact',views.getcontact,name='getcontact'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('userlogout',views.userlogout,name='userlogout'),
    path('view/<int:id>/',views.view,name='view'),
    path('getmsg',views.getmsg,name='getmsg'),
    path('msgtableview',views.msgtableview,name='msgtableview'),
    path('bride',views.bride,name='bride'),
    path('groom',views.groom,name='groom')
   
    
]