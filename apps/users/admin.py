from django.contrib import admin
from .models import UserModel


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserModel, UserAdmin)
