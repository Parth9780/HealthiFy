from django.db import models

# Create your models here.
class Register_Form(models.Model):
    Name = models.CharField(max_length=30)
    Mobile = models.BigIntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.Name # TODO

class Appointment(models.Model):
    Name = models.CharField(max_length=30)
    Mobile = models.BigIntegerField()
    Email = models.EmailField()
    Date = models.DateField()
    Area = models.CharField(max_length=200)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Postal_Code = models.IntegerField()
    
    def __str__(self) -> str:
        return self.Name # TODO
    
class ContactUs(models.Model):
    Name = models.CharField(max_length=30)
    Phone = models.BigIntegerField()
    Email = models.EmailField()
    Message = models.TextField()
    
    def __str__(self) -> str:
        return self.Name # TODO

class AdminLogin(models.Model):
    UserName = models.CharField(max_length=150)
    Email = models.EmailField()
    Password = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.UserName # TODO