from django.contrib import admin


from .models import Article, Parameter, Basket, ThermalDeburring

admin.site.register(Article)
admin.site.register(Parameter)
admin.site.register(Basket)
admin.site.register(ThermalDeburring)
