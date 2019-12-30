from django.apps import AppConfig
from django.utils.html import format_html
from . import __version__ as VERSION

class ContactUsConfig(AppConfig):
    name = 'contact_us'
    verbose_name = format_html("Contact Us Management <span class='version'>{}</span>", VERSION)

