import graphene
from graphene_django import DjangoObjectType
from blog.models import Category, Post

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "slug", "name",)

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "slug", "title", "body", "pub_date", "categories",)

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_posts(root, info):
        # We can easily optimize query count in the resolve method
        return Post.objects.prefetch_related("categories").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
