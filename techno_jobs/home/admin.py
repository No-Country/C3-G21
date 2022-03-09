from django.contrib import admin
from .models import User, UserProfile, CompanyProfile, Offer

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(CompanyProfile)
# admin.site.register(Offer)
