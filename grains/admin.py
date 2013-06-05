from django.contrib import admin
from .models import Grain


class GrainAdmin(admin.ModelAdmin):
    model = Grain
    list_display = 'key', 'value'

admin.site.register(Grain, GrainAdmin)
