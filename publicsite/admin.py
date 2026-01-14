from django.contrib import admin
from .models import PublicPageContent

@admin.register(PublicPageContent)
class PublicPageContentAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'title', 'updated_at')
    search_fields = ('page_name', 'title')
    readonly_fields = ('updated_at',)
