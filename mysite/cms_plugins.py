from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import gettext_lazy as _
from .models import Blog

@plugin_pool.register_plugin
class HelloPlugin(CMSPluginBase):
    model = Blog
    render_template = "person.html"
    cache = False