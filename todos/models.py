from django.db import models

# Create your models here.
class Todo(models.Model):
    tittle= models.CharField(max_length=100)
    create_at= models.DateField(auto_now_add=True)
    deadline= models.DateField(null= False, blank= False)
    finished_at= models.DateField(null=True, blank= True)
    