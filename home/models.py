from django.db import models

# Create your models here.


class Film(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="pic")
    star=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    language=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    genre=models.CharField(max_length=100) 
    dimensional= models.CharField(max_length=100)       
    time=models.CharField(max_length=100)



class Seat(models.Model):
    sro=models.ForeignKey(Film,related_name="film",on_delete=models.CASCADE)
    total=models.CharField(max_length=100)
    available=models.CharField(max_length=100)
    price=models.IntegerField()