from django.contrib import admin

# Register your models here.
from events import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'event_image',
        'event_text',
    ]
