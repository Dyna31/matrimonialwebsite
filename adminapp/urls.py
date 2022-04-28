from django.urls import path
from.import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('addcat',views.addcat,name='addcat'),
    path('getcat',views.getcat,name='getcat'),
    path('viewcat',views.viewcat,name='viewcat'),
    path('adlogin',views.adlogin,name='adlogin'),
    path('getadlogin',views.getadlogin,name='getadlogin'),
    path('viewreg',views.viewreg,name='viewreg'),
    path('accept/<int:id>/',views.accept,name='accept'),
    path('decline/<int:id>/',views.decline, name='decline'),
    path('contact_view',views.contact_view,name='contact_view')
]