from django.contrib import admin
from .models import Shortener


class ShortenerAdmin(admin.ModelAdmin):
    list_display = ('url', 'domain_shortened_domain')


admin.site.register(Shortener, ShortenerAdmin)