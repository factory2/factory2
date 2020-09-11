from django.db import models

class Basket(models.Model):
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.title

class Parameter(models.Model):
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField(blank=True)

    def __str__(delf):
        return self.title

class Article(models.Model):
    code=models.CharField(max_length=200,unique=True)
    title=models.CharField(max_length=200,blank=True)
    description=models.TextField(blank=True)
    basket=models.ForeignKey(Basket,on_delete=models.CASCADE,blank=True,null=True)
    parameter=models.ForeignKey(Parameter,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.code
