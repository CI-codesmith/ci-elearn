from django.db import models

# Public site requires minimal models. 
# Company info is read-only from settings and templates.

class PublicPageContent(models.Model):
    """Optional: Store editable content for public pages via admin"""
    page_name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name_plural = "Public Page Content"
