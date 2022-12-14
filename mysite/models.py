from cms.models.pluginmodel import CMSPlugin
from tinymce.models import HTMLField
from django.db import models

class Blog(CMSPlugin):
    title = models.CharField(max_length=50, default='Guest')
    body = HTMLField()