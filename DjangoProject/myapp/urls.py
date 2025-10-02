from django.urls import path 
from . import views # Import views from the current app 
# from django.contrib.auth import views as auth_views # Alternative for direct import of built-in views

urlpatterns = [ 
 # path('hello/', views.hello_world, name='hello_world'), # Old URL (can be kept or removed) 
 path('', views.home, name='home'), # New URL for the root of the app 
 path('register/', views.register, name='register'), # New URL for registration 
 path('login/', views.CustomLoginView.as_view(), name='login'), # New URL for login
 path('logout/', views.CustomLogoutView.as_view(), name='logout'), # New URL for logout 
] 