from django.db import models
from autoslug import AutoSlugField

class Department(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', editable=True, unique_with='id')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
