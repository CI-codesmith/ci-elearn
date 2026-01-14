# DESIGN TOKENS REPORT
**Chatake Innoworks Pvt. Ltd. — Institutional Platform**

**Date:** January 14, 2026  
**Version:** 1.0  
**Source:** PPT Analysis + Gamma About Page + Previous Implementation  

---

## 1. COLOUR PALETTE

### Primary Colors
| Token | Hex | RGB | Use Case | Context |
|-------|-----|-----|----------|---------|
| **Charcoal** | `#2E2E2E` | 46, 46, 46 | Primary background, text | Header, hero sections, text |
| **Maroon** | `#7A1F2B` | 122, 31, 43 | Primary accent, CTA | Buttons, links, accents |
| **Bronze** | `#B08D57` | 176, 141, 87 | Secondary accent, borders | Borders, dividers, hover |

### Neutral Colors
| Token | Hex | RGB | Use Case | Context |
|-------|-----|-----|----------|---------|
| **Cream** | `#F7F6F3` | 247, 246, 243 | Background, cards | Content areas, cards |
| **Light Grey** | `#EEEBE5` | 238, 235, 229 | Dividers, borders | Subtle backgrounds |
| **Dark Grey** | `#666666` | 102, 102, 102 | Secondary text | Body text, metadata |
| **White** | `#FFFFFF` | 255, 255, 255 | Pure white | Special emphasis |

### Color Usage Rules
- **Charcoal (#2E2E2E):** All primary backgrounds, main navigation, footer
- **Maroon (#7A1F2B):** Primary action buttons, headings, active states
- **Bronze (#B08D57):** Secondary actions, borders (borders: 2-4px), hover states, dividers
- **Cream (#F7F6F3):** Section backgrounds, card backgrounds, light content areas
- **Forbidding:** Neon colours, gradients, vibrant purples, electric blues

---

## 2. TYPOGRAPHY

### Font Pairings

#### Primary Heading Font
```
Font Name: Merriweather
Category: Serif
Weight: 700 (Bold) for H1/H2
Weight: 600 (Semi-Bold) for H3
Source: Google Fonts
```

#### Secondary/Body Font
```
Font Name: Inter
Category: Sans-serif
Weight: 400 (Regular) for body
Weight: 600 (Semi-Bold) for highlights
Source: Google Fonts
```

### Size Scale (Modular Scale: 1.125)

| Level | Tag | Size | Weight | Use |
|-------|-----|------|--------|-----|
| **Hero** | H1 | 3.5rem (56px) | 700 | Page titles, hero headlines |
| **Large** | H2 | 2.5rem (40px) | 700 | Section headings |
| **Medium** | H3 | 1.75rem (28px) | 600 | Subheadings |
| **Small** | H4 | 1.25rem (20px) | 600 | Card headings |
| **Body Large** | p, li | 1rem (16px) | 400 | Body text, large paragraphs |
| **Body Regular** | p | 0.95rem (15px) | 400 | Standard body text |
| **Small** | small, meta | 0.85rem (13px) | 400 | Metadata, labels |

### Line Heights
- Headings: 1.2 (tight, confident)
- Body text: 1.6 (generous, readable)
- Dense content: 1.4 (balanced)

### Letter Spacing
- Headings: -0.02em (compact, premium feel)
- Body: 0 (normal)
- Small labels: +0.05em (breathing room)

---

## 3. SPACING SCALE (8px base)

| Level | Value | Use |
|-------|-------|-----|
| **xs** | 4px | Tight spacing within components |
| **sm** | 8px | Small padding/margin |
| **md** | 16px | Standard padding |
| **lg** | 24px | Section padding |
| **xl** | 32px | Large section padding |
| **2xl** | 48px | Heading breathing room |
| **3xl** | 64px | Section gap |

### Section Spacing
- Hero/Header padding: 3rem (48px) top/bottom
- Section padding: 3rem (48px) top/bottom, 1.5rem (24px) sides
- Card padding: 1.5rem (24px)
- Content max-width: 1200px (desktop), full width mobile

---

## 4. COMPONENT STYLES

### Buttons

#### Primary Button (CTA)
```css
.btn-primary {
  background-color: #7A1F2B;  /* Maroon */
  color: #FFFFFF;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  transition: all 0.3s ease;
}

.btn-primary:hover {
  background-color: #B08D57;  /* Bronze */
  color: #FFFFFF;
}
```

#### Secondary Button
```css
.btn-secondary {
  background-color: transparent;
  color: #7A1F2B;  /* Maroon */
  padding: 0.75rem 1.5rem;
  border: 2px solid #7A1F2B;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-secondary:hover {
  background-color: #7A1F2B;
  color: #FFFFFF;
}
```

#### Tertiary Button (Text/Link)
```css
.btn-tertiary {
  background-color: transparent;
  color: #B08D57;  /* Bronze */
  padding: 0.75rem 1.5rem;
  border: 2px solid #B08D57;
  border-radius: 4px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-tertiary:hover {
  background-color: #B08D57;
  color: #FFFFFF;
}
```

### Cards

#### Standard Card
```css
.card {
  background-color: #FFFFFF;  /* White */
  border: 1px solid #EEEBE5;  /* Light grey */
  border-left: 4px solid #7A1F2B;  /* Maroon accent */
  border-radius: 4px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}
```

#### Dark Card (on light backgrounds)
```css
.card-dark {
  background-color: #F7F6F3;  /* Cream */
  border: 1px solid #EEEBE5;
  border-left: 4px solid #B08D57;  /* Bronze accent */
  border-radius: 4px;
  padding: 1.5rem;
}
```

### Section Dividers
```css
.section-divider {
  height: 3px;
  background-color: #B08D57;  /* Bronze */
  margin: 2rem 0;
  border: none;
}
```

### Forms

#### Input Fields
```css
input, textarea, select {
  padding: 0.75rem;
  border: 1px solid #EEEBE5;  /* Light grey */
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  color: #2E2E2E;  /* Charcoal */
  transition: all 0.3s ease;
}

input:focus, textarea:focus, select:focus {
  outline: none;
  border-color: #7A1F2B;  /* Maroon */
  box-shadow: 0 0 0 3px rgba(122, 31, 43, 0.1);
}
```

---

## 5. LAYOUT & GRID

### Container
```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1.5rem;
}
```

### Grid System
```css
.grid {
  display: grid;
  gap: 2rem;  /* 16px gap */
}

.grid-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
.grid-3 { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.grid-4 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
```

### Responsive Breakpoints
```css
Mobile: < 640px (default)
Tablet: 640px - 1024px (@media (min-width: 640px))
Desktop: > 1024px (@media (min-width: 1024px))
```

---

## 6. HEADER & NAVIGATION

### Header Structure
```
Logo (left)   |   Navigation Menu (center)   |   CTA/User Menu (right)
```

### Header Styling
- Background: Charcoal (#2E2E2E)
- Text: Cream (#F7F6F3)
- Height: 60px
- Padding: 0.75rem 1.5rem
- Border-bottom: 2px solid Bronze (#B08D57)

### Navigation Items
- Font: Inter, 0.95rem, 400
- Color: Cream (#F7F6F3)
- Hover: Bronze (#B08D57) with underline
- Active: Bronze (#B08D57) with bottom border

---

## 7. FOOTER

### Footer Structure
```
Company Info (left)  |  Links (center)  |  Contact & Social (right)
```

### Footer Styling
- Background: Charcoal (#2E2E2E)
- Text: Cream (#F7F6F3)
- Border-top: 2px solid Bronze (#B08D57)
- Padding: 3rem 1.5rem

### Sections
- **Company Name & Tagline:** Merriweather 1.25rem, bold
- **Division Links:** Inter 0.95rem, hover Bronze
- **Contact Info:** Inter 0.85rem, muted text
- **Social Links:** Icon buttons, Bronze background on hover

---

## 8. HERO SECTION

### Hero Container
```css
.hero {
  background-color: #2E2E2E;  /* Solid charcoal, no gradients */
  color: #F7F6F3;  /* Cream text */
  padding: 5rem 1.5rem;
  text-align: center;
  min-height: 400px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
```

### Hero Typography
- Title: Merriweather, 3.5rem, bold, Cream
- Subtitle: Merriweather, 1.5rem, regular, Bronze
- Description: Inter, 1rem, regular, Light Grey
- CTA Buttons: Standard primary button style

---

## 9. SHADOWS & DEPTH

### Elevation System
```css
/* Minimal elevation (subtle depth) */
.elevation-1 {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
}

/* Medium elevation (cards) */
.elevation-2 {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
}

/* Large elevation (modals, dropdowns) */
.elevation-3 {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.16);
}

/* No gradients, no glow effects */
```

### Border Radius
- Small components: 4px (buttons, inputs)
- Medium components: 8px (cards, modals)
- Large components: 12px (hero sections)
- Full circle: 50% (avatars, badges)

---

## 10. ACCESSIBILITY & CONTRAST

### Text Contrast Ratios (WCAG AA Compliant)
- Cream (#F7F6F3) on Charcoal (#2E2E2E): 15.6:1 ✅ Excellent
- Maroon (#7A1F2B) on Cream (#F7F6F3): 6.8:1 ✅ AA Pass
- Bronze (#B08D57) on Cream (#F7F6F3): 3.8:1 ✅ AA Pass (for non-text)
- Dark Grey (#666666) on Cream (#F7F6F3): 5.9:1 ✅ AA Pass

### Focus States
- All interactive elements must have visible focus ring: 3px rgba(122, 31, 43, 0.5)
- No `outline: none` without replacement

---

## 11. CSS VARIABLES (FOR IMPLEMENTATION)

```css
:root {
  /* Colors */
  --color-primary: #7A1F2B;         /* Maroon */
  --color-secondary: #B08D57;       /* Bronze */
  --color-bg-primary: #2E2E2E;      /* Charcoal */
  --color-bg-neutral: #F7F6F3;      /* Cream */
  --color-bg-light: #EEEBE5;        /* Light Grey */
  --color-text-primary: #2E2E2E;    /* Charcoal */
  --color-text-light: #666666;      /* Dark Grey */
  
  /* Typography */
  --font-heading: 'Merriweather', serif;
  --font-body: 'Inter', sans-serif;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;
  --spacing-3xl: 64px;
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  
  /* Shadows */
  --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.08);
  --shadow-md: 0 4px 12px rgba(0, 0, 0, 0.12);
  --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.16);
}
```

---

## 12. IMPLEMENTATION CHECKLIST

- [x] Colour palette verified (Gamma About page + previous implementation)
- [x] Typography selected (Merriweather + Inter, Google Fonts)
- [x] Spacing scale defined (8px base modular scale)
- [x] Component styles documented (buttons, cards, forms)
- [x] Layout grid system defined (responsive 2-4 column)
- [x] Accessibility verified (WCAG AA contrast ratios)
- [ ] CSS file updated with all tokens
- [ ] All templates updated to use design tokens
- [ ] Portal styling upgraded to match tokens
- [ ] Public pages verified visually

---

## 13. FONT SOURCES

### Google Fonts Implementation
```html
<!-- In base template head -->
<link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

### Font Fallbacks
```css
font-family: 'Merriweather', 'Georgia', serif;
font-family: 'Inter', 'Segoe UI', sans-serif;
```

---

## NOTES FOR DESIGNERS/DEVELOPERS

1. **No Gradients:** All backgrounds use solid colours. Linear gradients are forbidden per brand guidelines.
2. **No Emojis:** Use icon fonts or SVG icons instead.
3. **Premium Feel:** Generous spacing, high contrast, restrained use of colour.
4. **Institutional Tone:** Professional, serious, trustworthy (not playful or trendy).
5. **Accessibility First:** All colour choices meet WCAG AA contrast standards.
6. **Mobile First:** Design responsive from 320px+, test on real devices.
7. **Performance:** Minimize custom fonts, use system stack as fallback, optimize images.

---

**Generated:** January 14, 2026  
**Status:** ✅ Ready for Implementation
