from django.contrib import admin
from . models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')
    search_fields = ('user_username', 'phone')
    
admin.site.register(Profile, ProfileAdmin)