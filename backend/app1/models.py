from django.db import models

# Create your models here.
class Login(models.Model):
    id = models.CharField(max_length=30,primary_key=True)
    pw = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.id
