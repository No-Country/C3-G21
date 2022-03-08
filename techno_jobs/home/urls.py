from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='index'),
    path('faq/', views.faq, name='faq'),
    path('edit-user/<pk>', views.EditUser.as_view(), name='edit-user'),
    path('logout/', views.logout_view, name='logout'),

    # --- user ---
    path('<pk>', views.UserProfileView.as_view(), name='user-profile'),
    path('edit-profile/<pk>', views.EditUserProfile.as_view(), name='edit-profile'),

    # --- company ---
    path('<pk>', views.CompanyProfileView.as_view(), name='company-user-profile'),
    path('edit-company-profile/<pk>', views.EditCompanyProfile.as_view(), name='edit-company-profile'),
]