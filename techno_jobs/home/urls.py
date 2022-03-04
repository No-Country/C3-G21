from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='index'),
    path('faq/', views.faq, name='faq'),
    path('register/', views.register, name='register'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]