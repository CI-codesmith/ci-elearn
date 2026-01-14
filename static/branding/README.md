# Branding Assets

This directory contains official Chatake Innoworks branding materials.

## Asset Organization

- `logos/` — Primary logo variants (PNG, SVG)
- `banners/` — Hero banners and cover images
- `letterhead/` — Official letterhead templates
- `icons/` — UI icon set
- `docs/` — Corporate structure and vision documents (PDFs)

## Asset Copy Instructions

Run the following commands to populate assets from external directories:

```bash
# Copy logos from Downloads-Warehouse
cp /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/Downloads-Warehouse/logo* static/branding/logos/ 2>/dev/null || echo "No logos found"

# Copy banners
cp /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/Downloads-Warehouse/banner* static/branding/banners/ 2>/dev/null || echo "No banners found"

# Copy letterhead
cp /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/Downloads-Warehouse/letterhead* static/branding/letterhead/ 2>/dev/null || echo "No letterhead found"

# Copy Corporate Structure documents
cp /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/Corporate-Structure/*.pdf static/branding/docs/ 2>/dev/null || echo "No PDFs found"
cp /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/Corporate-Structure/*.pptx static/branding/docs/ 2>/dev/null || echo "No PPTs found"
```

## Using Assets in Templates

Reference assets using Django's `{% static %}` tag:

```html
{% load static %}
<img src="{% static 'branding/logos/primary-logo.png' %}" alt="Chatake Innoworks">
```

All assets are local (no external URLs).
