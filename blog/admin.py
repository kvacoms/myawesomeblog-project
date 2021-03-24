from django.contrib import admin

# Register your models here.
from blog import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'image',
        'text',
        'title',
        'date',
    ]