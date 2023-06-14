from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employeetask(models.Model):
    
    name=models.CharField(max_length=50,verbose_name="Task name")
    CAT=((1,'Office'),(2,'Personal'))
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    status=models.BooleanField(default=True)
  
   
    
    def __str__(self):
        return self.name
    
