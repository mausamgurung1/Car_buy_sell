from django.contrib import admin

from .models import \
    Listing  # Assuming models.py is in the same directory as admin.py


class ListingAdmin(admin.ModelAdmin):
    pass  # Customize this class as needed

admin.site.register(Listing, ListingAdmin)
