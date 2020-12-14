from django.contrib import admin
from .models import Article, Pallet
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ArticleResource(resources.ModelResource):

    class Meta:
        model = Article

class ArticleAdmin(ImportExportModelAdmin):
    resource_class = ArticleResource

admin.site.register(Article, ArticleAdmin)

admin.site.register(Pallet)
