from django.db import models
from location.models import Location

class Contact(models.Model):
    name = models.CharField(max_length=32, unique=True, blank=False)
    phone = models.CharField(max_length=32, unique=True, blank=False)
    email = models.EmailField(unique=True, blank=False)
    availability = models.CharField(max_length=32, blank=False)
    location = models.OneToOneField(
        Location,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name
    
