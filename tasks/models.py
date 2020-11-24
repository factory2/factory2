from django.db import models
from autoslug import AutoSlugField
from articles.models import Article
from machines.models import BasketDeburring, ParameterDeburring

class ThermalDeburring(models.Model):
    code = models.OneToOneField(Article, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='code')
    basket_deburring = models.ForeignKey(BasketDeburring,on_delete=models.CASCADE,blank=True,null=True)
    parameter_deburring = models.ForeignKey(ParameterDeburring,on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    done_article = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.slug
