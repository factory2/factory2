from django.contrib import admin


from .models import Article, Parameter, Basket

admin.site.register(Article)
admin.site.register(Parameter)
admin.site.register(Basket)
