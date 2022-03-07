from django.contrib import admin
from .models import User, UserProfile, Company, Offer

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Company)
admin.site.register(Offer)
