from django.db import models

# Create your models here.

class Color(models.Model):
    color_name = models.CharField(max_length=50)

    def __str__(self):
        return self.color_name

class People(models.Model):
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color',null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    