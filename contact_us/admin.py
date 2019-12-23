from django.contrib import admin
from .models import Contact

class ContactUsAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'date_created', 'last_updated', 'email', 'phone', 'location', 'availability' ]
    search_fields = [ 'name', 'email', 'phone', 'location', 'availability' ]

admin.site.register(Contact, ContactUsAdmin)
