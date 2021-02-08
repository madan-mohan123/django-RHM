from django.db import models

class House(models.Model):
    
    Rooms=models.CharField(max_length=100)
    AcRooms=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Room_Type=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Cost=models.CharField(max_length=100)
    Owner_Id=models.CharField(max_length=100)
    Status=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    Offer=models.BooleanField(default=False)

class Owner(models.Model):
    username=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')

class Tenant(models.Model):
    username=models.CharField(max_length=100)
    Email=models.CharField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics') 
    Members=models.IntegerField()   
    Purpose=models.CharField(max_length=100)
    Joining_date=models.DateField()
    Leave_date=models.DateField()
    Address=models.CharField(max_length=100)
