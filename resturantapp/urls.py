from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('fooditem/<int:pk>', views.fooditem, name='fooditem'),
    path('cart/add/<int:fooditem_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:fooditem_id>/', views.remove_cart, name='remove_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('upload/', views.upload_food, name='upload')
]