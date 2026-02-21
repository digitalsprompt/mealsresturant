from django.contrib import admin
from . models import Category, FoodItem
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)
    
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)