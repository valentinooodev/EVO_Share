from django.urls import path, include


app_name = 'apps'

urlpatterns = [
    path('', include('apps.posts.urls', namespace='posts')),
    path('users/', include('apps.users.urls', namespace='users')),
]
