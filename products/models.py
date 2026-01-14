from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=160, unique=True, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["name", "category"]),
            models.Index(fields=["category", "-created"]),
        ]

    def __str__(self):
        return self.name

