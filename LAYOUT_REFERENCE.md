# UI LAYOUT REFERENCE GUIDE

## 1. ROLE SELECTOR PAGE (`/portal/`)
```
┌──────────────────────────────────────────────┐
│  📚 Chatake Innoworks | Welcome, John Doe   │ ← Header
│                                   [Logout]   │
├──────────────────────────────────────────────┤
│ Home  Portal  Admin  LMS                     │ ← Sidebar Nav
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│         SELECT YOUR ROLE                     │
│  "Choose a role to access your dashboard"   │
│                                              │
│  ┌─────────────┐  ┌─────────────┐          │
│  │     📚      │  │     👨‍🏫      │          │
│  │   STUDENT   │  │   TEACHER   │          │
│  │ Access and  │  │ Manage and  │          │
│  │ track your  │  │ grade your  │          │
│  │ programs... │  │ classes...  │          │
│  │             │  │             │          │
│  │ [ENTER]     │  │ [ENTER]     │          │
│  └─────────────┘  └─────────────┘          │
│                                              │
│  ┌─────────────┐  ┌─────────────┐          │
│  │     💼      │  │     🚀      │          │
│  │    INTERN   │  │ PROJECT LED │          │
│  │ Complete    │  │ Manage your │          │
│  │ internship  │  │ project...  │          │
│  │ tasks...    │  │             │          │
│  │             │  │             │          │
│  │ [ENTER]     │  │ [ENTER]     │          │
│  └─────────────┘  └─────────────┘          │
│                                              │
│  ┌─────────────┐  ┌─────────────┐          │
│  │     💳      │  │     ⚙️       │          │
│  │  ACCOUNTS   │  │    ADMIN    │          │
│  │ Manage fees │  │ Administer  │          │
│  │ and...      │  │ system...   │          │
│  │             │  │             │          │
│  │ [ENTER]     │  │ [ENTER]     │          │
│  └─────────────┘  └─────────────┘          │
│                                              │
└──────────────────────────────────────────────┘
```

---

## 2. STUDENT DASHBOARD (`/portal/student/`)
```
┌─────────────────┬─────────────────────────────────────┐
│ 📚 Chatake      │ Welcome, John Doe | [Logout]        │ ← Header
├─────────────────┼─────────────────────────────────────┤
│ Dashboard       │ STUDENT DASHBOARD                   │
│ [active]        │ "Welcome back! Here's your overview"│
│                 │                                     │
│ Current Role    ├─────────────────────────────────────┤
│ ► STUDENT       │                                     │
│                 │ 📚 YOUR PROGRAMS & BATCHES          │
│ Quick Actions   │ ┌─────────────────────────────────┐ │
│ • View Prog...  │ │ Program │Code │Batch │ Y │Status│ │
│ • My Enroll...  │ ├─────────────────────────────────┤ │
│ • Progress...   │ │ Coaching│ CS  │ Batch│2024│ACTIVE│ │
│                 │ │         │     │ 1    │    │       │ │
│ Navigation      │ ├─────────────────────────────────┤ │
│ • Home          │ │ [View] [View] [View]           │ │
│ • [Logout]      │ └─────────────────────────────────┘ │
│                 │                                     │
│                 │ 📋 RECENT ASSIGNMENTS              │
│                 │ [Coming Soon]                       │
│                 │                                     │
│                 │ 📊 PROGRESS TRACKING               │
│                 │ [Coming Soon]                       │
│                 │                                     │
│                 │ 🗓️ UPCOMING EVENTS                 │
│                 │ [Coming Soon]                       │
│                 │                                     │
└─────────────────┴─────────────────────────────────────┘
```

---

## 3. TEACHER DASHBOARD (`/portal/teacher/`)
```
┌─────────────────┬─────────────────────────────────────┐
│ 📚 Chatake      │ Welcome, Prof. Smith | [Logout]     │
├─────────────────┼─────────────────────────────────────┤
│ Dashboard       │ TEACHER DASHBOARD                   │
│ [active]        │ "Welcome back! Here's your overview"│
│                 │                                     │
│ Current Role    ├─────────────────────────────────────┤
│ ► TEACHER       │                                     │
│                 │ 👥 YOUR CLASSES & BATCHES          │
│ Quick Actions   │ ┌─────────────────────────────────┐ │
│ • Manage Cl...  │ │ Program │Code │Batch │Stu │Stat││ │
│ • Create Bat... │ ├─────────────────────────────────┤ │
│ • View Stud...  │ │ Coaching│ CS  │Batch │ N/A│ACTV│ │
│                 │ │         │     │ 1    │    │    │ │
│ Navigation      │ ├─────────────────────────────────┤ │
│ • Home          │ │ [Manage]                        │ │
│ • [Logout]      │ └─────────────────────────────────┘ │
│                 │                                     │
│                 │ 📝 CREATE ASSIGNMENT               │
│                 │ [Coming Soon]                       │
│                 │                                     │
│                 │ ✅ GRADING DASHBOARD               │
│                 │ [Coming Soon]                       │
│                 │                                     │
│                 │ 📊 CLASS ANALYTICS                 │
│                 │ [Coming Soon]                       │
│                 │                                     │
└─────────────────┴─────────────────────────────────────┘
```

---

## 4. ADMIN DASHBOARD (`/portal/admin/`)
```
┌─────────────────┬─────────────────────────────────────┐
│ 📚 Chatake      │ Welcome, Admin | [Logout]           │
├─────────────────┼─────────────────────────────────────┤
│ Dashboard       │ ADMIN DASHBOARD                     │
│ [active]        │ "Welcome back! Here's your overview"│
│                 │                                     │
│ Current Role    ├─────────────────────────────────────┤
│ ► ADMIN         │                                     │
│                 │ ⚙️ SYSTEM ADMINISTRATION            │
│ Quick Actions   │ ┌──────────────┐  ┌──────────────┐ │
│ • Admin Pan...  │ │ 👥 USERS     │  │ 📚 PROGRAMS  │ │
│ • System St...  │ │ Manage users,│  │ Create and   │ │
│ • Users         │ │ roles...     │  │ manage...    │ │
│                 │ │ [MANAGE]     │  │ [MANAGE]     │ │
│ Navigation      │ └──────────────┘  └──────────────┘ │
│ • Home          │ ┌──────────────┐  ┌──────────────┐ │
│ • [Logout]      │ │ 🎓 ENROLL... │  │ 🏫 SCHOOL    │ │
│                 │ │ View and     │  │ Manage       │ │
│                 │ │ manage...    │  │ school...    │ │
│                 │ │ [MANAGE]     │  │ [MANAGE]     │ │
│                 │ └──────────────┘  └──────────────┘ │
│                 │ ┌──────────────┐  ┌──────────────┐ │
│                 │ │ 💼 INTERNSH..│  │ 🚀 PROJECTS  │ │
│                 │ │ Manage       │  │ Manage       │ │
│                 │ │ internship..│  │ projects...  │ │
│                 │ │ [MANAGE]     │  │ [MANAGE]     │ │
│                 │ └──────────────┘  └──────────────┘ │
│                 │                                     │
│                 │ 📊 SYSTEM ANALYTICS                │
│                 │ [Coming Soon]                       │
│                 │                                     │
│                 │ 🔔 SYSTEM LOGS & ALERTS            │
│                 │ [Coming Soon]                       │
│                 │                                     │
└─────────────────┴─────────────────────────────────────┘
```

---

## 5. MOBILE LAYOUT (< 768px)
```
┌────────────────────────────┐
│ 📚 Chatake | [Logout]      │ ← Header
├────────────────────────────┤
│                            │
│ STUDENT DASHBOARD          │
│ (Same content stacked)     │
│                            │
│ [Navigation collapsed      │
│  - can be toggled]         │
│                            │
│ 📚 YOUR PROGRAMS           │
│ ┌──────────────────────┐   │
│ │ Coaching | Batch 1   │   │
│ │ [ACTIVE]             │   │
│ │ [View]               │   │
│ └──────────────────────┘   │
│                            │
│ 📋 RECENT ASSIGNMENTS      │
│ [Coming Soon]              │
│                            │
│ (Footer)                   │
│                            │
└────────────────────────────┘
```

---

## CSS COLORS IN ACTION

### Primary Color (#7A1F2B - Maroon)
- Page headers
- Main navigation text
- Button backgrounds
- Role tile top border (hover)
- Status badges
- Links hover state

### Secondary Color (#2E2E2E - Charcoal)  
- Body text
- Secondary buttons
- Sidebar section titles
- Button hover states
- Dark accents

### Background Color (#F7F6F3 - Cream)
- Main page background
- Dashboard content area
- Form backgrounds
- Light section backgrounds

### Accent Color (#B08D57 - Bronze)
- Highlights in badges
- Minimal decorative accents
- Border accents (rare)

### Neutral Borders (#e0e0e0 - Light Gray)
- Table borders
- Card borders
- Form input borders
- Section separators

---

## RESPONSIVE BEHAVIOR

### Desktop (> 768px)
- Fixed 250px sidebar always visible
- Full-width content area
- Multi-column grid layouts

### Tablet/Mobile (≤ 768px)
- Sidebar moves above content
- Single column layout
- Full-width tables
- Stacked sections

---

## TYPOGRAPHY HIERARCHY

### Heading Sizes (Merriweather)
```
H1 (2.5rem)   - Page title / Platform name
H2 (2rem)     - Section headers / Dashboard title
H3 (1.5rem)   - Subsection headers
H4 (1.2rem)   - Card titles / Labels
Small (0.9rem)- Metadata / Secondary text
```

### Font Weights
- 400: Body text, regular content
- 600: Strong emphasis, labels
- 700: Bold headings, CTAs

---

## COMPONENT EXAMPLES

### Button Styles
```
Primary (Maroon):      [ENTER DASHBOARD]  → hover: Charcoal
Secondary (Gray):      [View]             → hover: Maroon
Small (Table):         [View]             → hover: Charcoal
```

### Badge Styles
```
Status Badge:          [ACTIVE]  (Maroon bg, white text)
Count Badge:           [5]       (Gray bg)
Category Badge:        [2024]    (Gray bg)
```

### Alert Styles
```
Info Box:              ℹ️ Coming Soon: View assignments
Success Box:           ✓ Registration successful
Warning Box:           ⚠️ Pending approval
Error Box:             ✗ Invalid submission
```

---

## INTERACTION PATTERNS

### Hover States
- Links: Underline + color change
- Buttons: Color shift + subtle lift
- Cards: Border color + shadow increase
- Table rows: Subtle background change

### Focus States
- Form inputs: Primary color border + outline
- Buttons: Primary color background
- Links: Underline + text decoration

### Active States
- Sidebar nav: Bold + primary color
- Tabs: Underline + color change
- Buttons: Pressed appearance

---

## ACCESSIBILITY FEATURES

✓ Semantic HTML (header, nav, main, section)
✓ Proper heading hierarchy (H1 → H2 → H3)
✓ Link text is descriptive
✓ Buttons have clear labels
✓ Color not sole indicator (badges use text)
✓ Sufficient color contrast (WCAG AA)
✓ Focus states visible
✓ Form labels associated with inputs

---

## PERFORMANCE NOTES

- Single CSS file (7.9 KB unminified)
- No external CSS frameworks
- No JavaScript dependencies
- Font files via Google Fonts API
- Static images use Unicode emoji
- Optimized for fast loading

---

## FUTURE ENHANCEMENTS

- [ ] Dark mode variant (via CSS custom properties)
- [ ] Print styles for reports
- [ ] Accessibility audit (WCAG AAA)
- [ ] Animation library integration
- [ ] Theme customization interface
- [ ] RTL language support
- [ ] Loading states and spinners
- [ ] Toast notification system

---

This guide provides visual reference for the institutional UI design and can be used during development and quality assurance testing.
