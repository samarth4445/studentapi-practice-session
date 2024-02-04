from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=10)
    class_name = models.CharField(max_length=5)
    batch_name = models.CharField(max_length=3)
