from django.db import models
from django.core.validators import RegexValidator
alphaneumeric= RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')


# Create your models here.
class Regidb(models.Model):
    xyz=models.ImageField(upload_to='media', null=True,blank=False)
    uname=models.CharField(max_length=100,null=True,blank=False)
    email=models.CharField(max_length=100,null=True,blank=False)
    upassword=models.CharField(max_length=100,null=True,blank=False)
    age =models.IntegerField(null=True,blank=False)
    gender=models.CharField(max_length=100, null=True,blank=False)
    phonenumber=models.IntegerField(null=True,blank=False)
    weight=models.IntegerField(null=True,blank=False,validators=[alphaneumeric])
    profession=models.CharField(max_length=100,null=True,blank=False)
    category=models.CharField(max_length=100,null=True,blank=False)
    address=models.CharField(max_length=100,null=True,blank=False)
    status=models.IntegerField(null=True,blank=False)
    active=models.IntegerField(null=True,blank=False)
class Contactdb(models.Model):
    message=models.CharField(max_length=500,null=True,blank=False)
    cname=models.CharField(max_length=100,null=True,blank=False)
    cemail=models.CharField(max_length=100,null=True,blank=False)
    subject=models.CharField(max_length=100,null=True,blank=False)
class Messagedb(models.Model):
    msg=models.CharField(max_length=500,null=True,blank=False)
    userid=models.ForeignKey(Regidb, on_delete=models.CASCADE,null=True,blank=False)
    mid=models.IntegerField(null=True,blank=False)



    

