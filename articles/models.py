from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from departments.models import Department
from zamak.models import Zamak

class Article(models.Model):
    code=models.SlugField(max_length=50, unique=True)
    title=models.CharField(max_length=200, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    weight = models.PositiveIntegerField(default=1)
    zamak = models.ForeignKey(Zamak, on_delete = models.CASCADE, blank=True, null=True)
    image1=models.ImageField(upload_to='articles', blank=True, null=True)
    image2=models.ImageField(upload_to='articles', blank=True, null=True)
    image3=models.ImageField(upload_to='articles', blank=True, null=True)
    image4=models.ImageField(upload_to='articles', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    for_thermal_deburring = models.BooleanField(default=False)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ['code']


class Pallet(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    quantity_thermal_deburred_no_ok = models.PositiveIntegerField(default=0)
    quantity_thermal_deburred = models.PositiveIntegerField(default=1)
    weight = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    weight_thermal_deburred_no_ok = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    weight_thermal_deburred = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    thermal_deburred_date = models.DateTimeField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete = models.CASCADE, blank=True, null=True)
    employee = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)
    employee_thermal_deburring = models.ForeignKey(User, on_delete = models.CASCADE, related_name='pallet_thermal_deburred', blank=True, null=True)
    thermal_deburred = models.BooleanField(default=False)

    def __str__(self):
        date_time = self.created_date.strftime("%d/%m/%Y, %H:%M:%S")
        return date_time + ", " + self.article.code

    class Meta:
        ordering = ['-created_date']
