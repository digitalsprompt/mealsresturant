from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = CloudinaryField('image', folder='food_images', blank=True, null=True, help_text='Upload an image of the food item')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name