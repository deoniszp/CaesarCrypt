from django.contrib import admin
from .models import Text

class TextAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']
    ordering = ['title']

admin.site.register(Text, TextAdmin)