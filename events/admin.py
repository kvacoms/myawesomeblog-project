from django.contrib import admin

# Register your models here.
from events import models


@admin.register(models.Event)
class InboxAdmin(admin.ModelAdmin):
    list_display = [
        'event_image',
        'event_text',
    ]
