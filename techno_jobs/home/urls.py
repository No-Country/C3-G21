from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='index'),
    path('faq/', views.faq, name='faq'),
    path('register-user/', views.register_user, name='register-user'),
    path('register-company/', views.register_company, name='register-company'),
    path('login/', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('company-profile/', views.company_profile, name='company-profile'),
    path('logout/', views.logout_view, name='logout'),
]