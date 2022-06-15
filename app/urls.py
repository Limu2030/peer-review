from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update'),
    path('post/', views.post, name='post'),

]