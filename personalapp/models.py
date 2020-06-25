from django.db import models

# Create your models here.
class Note(models.Model):
    content =models.CharField(max_length=300)
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

class Account(models.Model):
    email=models.EmailField(max_length = 254) 
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)

    def __str__(self):
        return self.email

    





    

