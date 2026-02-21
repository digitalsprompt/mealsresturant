from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login' ),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_details, name='profile_details'),
    path('profile/update/', views.profile_update, name='profile_update'),
    
]