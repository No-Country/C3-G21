from django.contrib import admin
from .models import User, Company, Offer

# Register your models here.
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Offer)
