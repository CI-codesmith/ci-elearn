from django.contrib import admin
from .models import PodcastSeries, PodcastEpisode


@admin.register(PodcastSeries)
class PodcastSeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'logo')
        }),
        ('Links', {
            'fields': ('main_url',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PodcastEpisode)
class PodcastEpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'series', 'episode_number', 'air_date', 'published')
    list_filter = ('series', 'published', 'air_date')
    search_fields = ('title', 'description', 'guest_name')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Episode Information', {
            'fields': ('series', 'title', 'slug', 'episode_number', 'air_date')
        }),
        ('Description & Guest', {
            'fields': ('description', 'guest_name', 'tags')
        }),
        ('Media Links', {
            'fields': ('audio_url', 'video_url', 'spotify_url', 'apple_podcasts_url', 'duration_minutes'),
            'description': 'Provide links to where this episode can be listened to or watched'
        }),
        ('Status', {
            'fields': ('published',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

