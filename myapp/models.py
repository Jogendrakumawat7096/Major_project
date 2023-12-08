from django.db import models

# Create your models here
class Signup(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.PositiveBigIntegerField()
    address =models.TextField()
    password = models.CharField(max_length=150)

    
    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.PositiveBigIntegerField()
    address = models.TextField()
    password = models.CharField(max_length=150)
    image = models.ImageField(upload_to='user_images/')
    user_type=models.CharField(max_length=100,default="buyer")
    

    def __str__(self):
        return self.name
