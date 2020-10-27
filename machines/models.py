from django.db import models
from autoslug import AutoSlugField

class Machine(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')

#ThermalDeburrer machine

class BasketDeburring(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='baskets', blank=True)
    def __str__(self):
        return self.title

class ParameterDeburring(models.Model):
    title = models.CharField(max_length=50,unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ThermalDeburrer(Machine):
    basket_deburring = models.ManyToManyField(BasketDeburring,blank=True)
    parameter_deburring = models.ManyToManyField(ParameterDeburring,blank=True)

    def __str__(self):
        return self.name
