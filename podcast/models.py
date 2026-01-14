from django.db import models
from django.utils.text import slugify


class PodcastSeries(models.Model):
    """Podcast series (e.g., Chatake Voices Podcast)"""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    logo = models.ImageField(upload_to='podcast/logos/', null=True, blank=True)
    main_url = models.URLField(help_text="Link to main podcast page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Podcast Series"
        verbose_name_plural = "Podcast Series"
    
    def __str__(self):
        return self.name


class PodcastEpisode(models.Model):
    """Individual podcast episodes"""
    series = models.ForeignKey(PodcastSeries, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    description = models.TextField()
    episode_number = models.IntegerField()
    air_date = models.DateField()
    duration_minutes = models.IntegerField(null=True, blank=True)
    
    # Audio/Video links
    audio_url = models.URLField(null=True, blank=True, help_text="Link to audio file")
    video_url = models.URLField(null=True, blank=True, help_text="Link to video (YouTube, etc.)")
    spotify_url = models.URLField(null=True, blank=True)
    apple_podcasts_url = models.URLField(null=True, blank=True)
    
    # Metadata
    guest_name = models.CharField(max_length=200, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True, help_text="Comma-separated tags")
    published = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Podcast Episode"
        verbose_name_plural = "Podcast Episodes"
        ordering = ['-air_date']
        unique_together = ('series', 'episode_number')
    
    def __str__(self):
        return f"{self.series.name} - Ep {self.episode_number}: {self.title}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

