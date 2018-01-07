from django.contrib import admin
from login.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'email')
    list_filter = ('name',)
    fields = ('name', 'email')

admin.site.register(User,UserAdmin)