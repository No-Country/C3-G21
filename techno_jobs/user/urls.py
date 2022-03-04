from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.register, name='register'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('logout/', views.logout_view, name='logout'),
]
