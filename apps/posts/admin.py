from django.contrib import admin
from .models import (
    CategoryModel,
    PostModel,
    SeriesModel,
    SeriesPostModel,
)


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(SeriesModel)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(SeriesPostModel)
class SeriesPostAdmin(admin.ModelAdmin):
    pass
