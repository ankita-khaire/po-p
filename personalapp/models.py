from django.db import models

# Create your models here.
class Note(models.Model):
    content =models.CharField(max_length=300)
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


    

