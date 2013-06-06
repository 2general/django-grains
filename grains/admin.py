from django.conf import settings
from django.contrib import admin
from .models import Grain


class GrainAdmin(admin.ModelAdmin):
    model = Grain
    list_display = 'key', 'value'
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


admin.site.register(Grain, GrainAdmin)
