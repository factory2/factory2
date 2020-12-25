from django.db import models
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=100)
    slug = AutoSlugField(populate_from='name')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(_("Post title"), max_length=100)
    body = models.TextField(_("Post body"))
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='pub_date__month')

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

