from django.contrib import admin

from crudapp import models


class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', ]


admin.site.register(models.Account, AccountAdmin)
