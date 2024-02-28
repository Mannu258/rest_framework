from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    father_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Cateogry(models.Model):
    Cateogry_name = models.CharField(max_length=100)
class Book(models.Model):
    cateogry = models.ForeignKey(Cateogry,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)