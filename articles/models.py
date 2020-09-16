from django.db import models

class Article(models.Model):
    code=models.SlugField(max_length=50,unique=True)
    title=models.CharField(max_length=200,blank=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.code
