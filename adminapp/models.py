from django.db import models

# Create your models here.
class Catdb(models.Model):
    img=models.ImageField(upload_to='media', null=True,blank=False)
    name=models.CharField(max_length=100,null=True,blank=False)
    description=models.CharField(max_length=500,null=True,blank=False)
