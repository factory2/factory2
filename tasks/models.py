from django.db import models
from autoslug import AutoSlugField
from articles.models import Article, Pallet
from machines.models import BasketDeburring, ParameterDeburring
from django.utils import timezone
from django.contrib.auth.models import User

class ThermalDeburring(models.Model):
    article = models.OneToOneField(Article, primary_key=True, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='article')
    basket_deburring = models.ForeignKey(BasketDeburring, on_delete=models.CASCADE, blank=True, null=True)
    parameter_deburring = models.ForeignKey(ParameterDeburring, on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.article.code

    class Meta:
        ordering = ['article__code']

class PalletThermalDeburred(models.Model):
    pallet = models.OneToOneField(Pallet, primary_key=True, on_delete=models.CASCADE)
    thermal_deburred_date = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        date_time = self.thermal_deburred_date.strftime("%d/%m/%Y, %H:%M:%S")
        return date_time + ", " + self.pallet.article.code
