from django.conf import settings
from django.contrib import admin
from django.utils.html import escape
from .models import Grain


class GrainAdmin(admin.ModelAdmin):
    model = Grain
    list_display = 'key', 'render_value'
    fields = 'value',
    search_fields = 'key', 'value'
    ordering = 'key',

    def render_change_form(self, request, context,
                           add=False, change=False, form_url='', obj=None):
        if (obj.content_type == u'text/html'
             and 'django_wysiwyg' in settings.INSTALLED_APPS):
            self.change_form_template = 'grains/admin/wysiwyg_change_form.html'
        return super(GrainAdmin, self).render_change_form(
            request, context,
            add=add, change=change, form_url=form_url, obj=obj)

    def render_value(self, obj):
        if obj.content_type == u'text/html':
            return obj.value
        return escape(obj.value)
    render_value.allow_tags = True
    render_value.short_description = u'value'

    class Media:
        js = 'grains/js/admin/grain.js',
        css = {'screen': ['grains/css/admin/grain.css']}

admin.site.register(Grain, GrainAdmin)
