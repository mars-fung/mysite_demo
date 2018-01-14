from django.contrib import admin
from . import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'email', 'sex' ,'address', 'create_time')
    list_filter = ('name','email')
    fields = ('name', 'email', 'password')

admin.site.register(models.User, UserAdmin)