from django.urls import path

from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home, name='index'),
    path('faq/', views.faq, name='faq'),

    path('edit-user/<pk>', views.EditUser.as_view(), name='edit-user'),

    # --- user ---
    path('<pk>', views.UserProfileView.as_view(), name='user-profile'),
    path('edit-profile/<pk>', views.EditUserProfile.as_view(), name='edit-profile'),
    path('delete/<pk>', views.DeleteUser.as_view(), name='delete'),

    # --- company ---
    path('company-signup/', views.create_company, name='create-company'),
    path('company/<pk>', views.CompanyProfileView.as_view(), name='company-user-profile'),
    path('edit-company-profile/<pk>', views.EditCompanyProfile.as_view(), name='edit-company-profile'),
    path('delete-company/<pk>', views.DeleteCompany.as_view(), name='delete-company'),

    # ---- jobs ----
    path('jobs/', views.JobsView.as_view(), name='jobs'),
    path('job/<pk>', views.OfferView.as_view(), name='job-view'),
    path('apply/<int:jobid>', views.apply, name='job-apply'),

    path('logout/', views.logout_view, name='logout'),
]