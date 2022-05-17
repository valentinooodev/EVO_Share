from django.db import models
from apps.models import BaseModel
from django.conf import settings
from ckeditor.fields import RichTextField


class CategoryModel(BaseModel):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category', default='category-default.jpg')
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        db_table = 'categories'


class SeriesModel(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='series_author')
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, default=1, related_name='series_category')
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='series', default='series-default.jpg')
    slug = models.SlugField(max_length=250)
    description = models.TextField(null=True)
    content = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Series'
        db_table = 'series'


class SeriesPostModel(BaseModel):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_published=True, series=None)

    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE, related_name='series')
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='series-posts', default='series-posts-default.jpg')
    description = models.TextField()
    index = models.IntegerField()
    slug = models.SlugField(max_length=250)
    content = RichTextField()
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Series Post'
        ordering = ('updated_at',)
        db_table = 'series_posts'


class PostModel(BaseModel):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_published=True, series=None)

    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, default=1, related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', default='posts-default.jpg')
    description = models.TextField(null=True)
    content = RichTextField()
    slug = models.SlugField(max_length=250)
    is_published = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0, editable=False)
    series = models.ForeignKey(SeriesModel, on_delete=models.CASCADE, related_name='posts', null=True, blank=True)
    series_index = models.IntegerField(null=True, blank=True)
    objects = models.Manager()
    post_objects = PostObjects()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ('-updated_at',)
        db_table = 'posts'