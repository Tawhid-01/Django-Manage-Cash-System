from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    
    def __str__(self):
        return self.username
    
class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE,related_name='profile')
    full_name = models.CharField(max_length=100, null=True)
    occupation = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='media/profile', null=True)

    def __str__(self):
        return self.full_name or 'none'
    


class AddCashModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    amount = models.IntegerField()
    source = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class ExpendCashModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    amount = models.IntegerField()
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username