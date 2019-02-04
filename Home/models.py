from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Maker(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True)

    def __str__(self):
        return self.name


class Material(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    
    category = models.ForeignKey(Category, models.CASCADE)
    maker = models.ForeignKey(Maker, models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
