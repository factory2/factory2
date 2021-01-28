from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Article(models.Model):
    code=models.SlugField(max_length=50, unique=True)
    title=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    image1=models.ImageField(upload_to='articles', blank=True, null=True)
    image2=models.ImageField(upload_to='articles', blank=True, null=True)
    image3=models.ImageField(upload_to='articles', blank=True, null=True) 
    image4=models.ImageField(upload_to='articles', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    for_thermal_deburring = models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
    class Meta:
        ordering = ['code']


class Pallet(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        date_time = self.created_date.strftime("%d/%m/%Y, %H:%M:%S")
        return date_time + ", " + self.article.code

    class Meta:
        ordering = ['-created_date']
