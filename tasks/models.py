from django.db import models
from autoslug import AutoSlugField
from articles.models import Article
from machines.models import BasketDeburring, ParameterDeburring

class ThermalDeburring(models.Model):
    article = models.OneToOneField(Article, primary_key=True, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='article')
    basket_deburring = models.ForeignKey(BasketDeburring,on_delete=models.CASCADE,blank=True,null=True)
    parameter_deburring = models.ForeignKey(ParameterDeburring,on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.article.code

    class Meta:
        ordering = ['article__code']
