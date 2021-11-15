from authapp import models
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_admin', 'is_superuser']

admin.site.register(models.User, UserAdmin)
