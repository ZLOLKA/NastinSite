from django.db import models


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Maker(Category):
    experience = models.DecimalField(blank=True)


class Material(Category):
    pass


class Product(models.Model):
    
    category = models.ForeignKey(Category, models.CASCADE)
    maker = models.ForeignKey(Maker, models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
