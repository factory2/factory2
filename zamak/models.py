from django.db import models
from autoslug import AutoSlugField

class Zamak(models.Model):
    title=models.CharField(max_length=20)
    slug = AutoSlugField(populate_from='title')
    description=models.TextField(blank=True)
    image1=models.ImageField(upload_to='zamak',blank=True)
    image2=models.ImageField(upload_to='zamak',blank=True)
    image3=models.ImageField(upload_to='zamak',blank=True)
    image4=models.ImageField(upload_to='zamak',blank=True)

    def __str__(self):
        return self.title
