from django.contrib import admin
from .models import Event, Registration


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time')
    list_filter = ('date', 'time')

class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'event', 'created_at']
    search_fields = ['name', 'email', 'event__title']


admin.site.register(Event, EventAdmin)
admin.site.register(Registration, RegistrationAdmin)