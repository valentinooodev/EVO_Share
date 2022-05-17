from django.urls import path
from .views import (
    home,
    post_detail,
)


app_name = 'posts'

urlpatterns = [
    path('', home, name='home'),
    path('posts/<str:slug>/', post_detail, name='post_detail'),
]
