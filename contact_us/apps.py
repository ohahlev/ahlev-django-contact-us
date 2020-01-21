from django.apps import AppConfig
from . import __version__ as VERSION

class ContactUsConfig(AppConfig):
    name = "contact_us"
    verbose_name = "Contact Us Management %s" % VERSION

