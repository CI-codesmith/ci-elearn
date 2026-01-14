# Website Integration Guide - Microprojects

This guide explains how to integrate the Machine Learning microprojects into your website frontend.

## Overview

The LMS now exposes microproject data through REST APIs that can be consumed by your website frontend. All 24 microprojects (18 regular + 3 advanced) are structured with units and available via JSON endpoints.

## API Endpoints

### 1. List All Microprojects
**Endpoint:** `/assessments/api/microprojects/`  
**Method:** GET  
**Response:**
```json
{
  "success": true,
  "total_count": 24,
  "units": {
    "1": {
      "unit_number": 1,
      "projects": [
        {
          "id": 1,
          "title": "Data Exploration Dashboard",
          "unit": 1,
          "max_marks": 100,
          "course_code": "316316",
          "course_name": "Machine Learning",
          "folder_name": "MICROPROJECT_1_1"
        },
        ...
      ]
    },
    ...
  },
  "microprojects": [...]
}
```

### 2. Get Specific Microproject Details
**Endpoint:** `/assessments/api/microprojects/<mp_id>/`  
**Method:** GET  
**Example:** `/assessments/api/microprojects/1/`  
**Response:**
```json
{
  "success": true,
  "microproject": {
    "id": 1,
    "title": "Data Exploration Dashboard",
    "unit": 1,
    "max_marks": 100,
    "course": {
      "code": "316316",
      "name": "Machine Learning"
    }
  }
}
```

### 3. Get Microprojects by Unit
**Endpoint:** `/assessments/api/units/<unit_num>/microprojects/`  
**Method:** GET  
**Example:** `/assessments/api/units/1/microprojects/`  
**Response:**
```json
{
  "success": true,
  "unit": 1,
  "count": 4,
  "microprojects": [
    {
      "id": 1,
      "title": "Data Exploration Dashboard",
      "unit": 1,
      "max_marks": 100,
      "subject__code": "316316",
      "subject__name": "Machine Learning"
    },
    ...
  ]
}
```

### 4. Get Microprojects Statistics
**Endpoint:** `/assessments/api/microprojects/stats/`  
**Method:** GET  
**Response:**
```json
{
  "success": true,
  "statistics": {
    "total_microprojects": 24,
    "total_units": 6,
    "by_unit": {
      "1": 4,
      "2": 5,
      "3": 3,
      "4": 3,
      "5": 3,
      "6": 3,
      "7": 3
    }
  }
}
```

## Microproject Structure

Each microproject folder follows this structure:

```
MICROPROJECT_X_Y/
├── README.md                 # Overview with LMS connection info
├── PROJECT.md               # Detailed specification
├── HOW_TO_DO.md            # Step-by-step guide
├── DATASET.md              # Dataset documentation
├── SOLUTION_TEMPLATE.ipynb # Starting template
└── SAMPLE_SOLUTION.ipynb   # Reference solution
```

## Unit Organization

### Unit 1: Introduction to Machine Learning (4 Projects)
- MP 1.1 - Data Exploration Dashboard (8%)
- MP 1.2 - Python ML Libraries Mastery (8%)
- MP 1.3 - Traditional vs ML Comparison (8%)
- MP 1.4 - Dataset Curation Project (9%)

### Unit 2: Data Preparation (5 Projects)
- MP 2.1 - Data Cleaning & Preprocessing (10%)
- MP 2.2 - Handling Missing Values (10%)
- MP 2.3 - Data Encoding & Scaling (10%)
- MP 2.4 - Feature Engineering Basics (12%)
- MP 2.5 - Data Visualization & Analysis (12%)

### Unit 3: Feature Selection (3 Projects)
- MP 3.1 - Feature Selection Methods (10%)
- MP 3.2 - Correlation Analysis (10%)
- MP 3.3 - Removing Irrelevant Features (10%)

### Unit 4: Supervised Learning (3 Projects)
- MP 4.1 - Classification Algorithms (10%)
- MP 4.2 - Regression Algorithms (10%)
- MP 4.3 - Model Evaluation & Metrics (12%)

### Unit 5: Unsupervised Learning (3 Projects)
- MP 5.1 - Clustering Techniques (10%)
- MP 5.2 - Clustering Comparison (10%)
- MP 5.3 - PCA & Dimensionality Reduction (12%)

### Unit 6: Ethics & Applications (3 Projects)
- MP 6.1 - ML Ethics & Bias (10%)
- MP 6.2 - Model Deployment & Production (12%)
- MP 6.3 - Real-World ML Applications (10%)

### Unit 7: Advanced Projects (3 Projects - Extra Credit)
- MP ADV-1 - End-to-End ML Pipeline
- MP ADV-2 - Deep Learning for Image Classification
- MP ADV-3 - Time Series Forecasting

## Website Integration Examples

### JavaScript/React Example

```javascript
// Fetch all microprojects
async function loadMicroprojects() {
  const response = await fetch('/assessments/api/microprojects/');
  const data = await response.json();
  
  if (data.success) {
    displayMicroprojects(data.units);
  }
}

// Fetch specific unit
async function loadUnitMicroprojects(unitNum) {
  const response = await fetch(`/assessments/api/units/${unitNum}/microprojects/`);
  const data = await response.json();
  
  if (data.success) {
    return data.microprojects;
  }
}

// Display in UI
function displayMicroprojects(units) {
  Object.entries(units).forEach(([unitId, unitData]) => {
    const unitSection = document.createElement('section');
    unitSection.className = 'unit-section';
    
    const title = document.createElement('h2');
    title.textContent = `Unit ${unitData.unit_number}`;
    unitSection.appendChild(title);
    
    unitData.projects.forEach(project => {
      const card = document.createElement('div');
      card.className = 'project-card';
      card.innerHTML = `
        <h3>${project.title}</h3>
        <p>Marks: ${project.max_marks}</p>
        <p>Folder: ${project.folder_name}</p>
        <a href="/microprojects/${project.folder_name}/">View Details</a>
      `;
      unitSection.appendChild(card);
    });
    
    document.getElementById('mp-container').appendChild(unitSection);
  });
}
```

### Python/Django Template Example

```django
{% load static %}

{% for unit_id, unit_data in units.items %}
<div class="unit-{{ unit_data.unit_number }}">
  <h2>Unit {{ unit_data.unit_number }}</h2>
  
  <div class="mp-grid">
    {% for project in unit_data.projects %}
    <div class="mp-card">
      <h3>{{ project.title }}</h3>
      <p><strong>Marks:</strong> {{ project.max_marks }}</p>
      <p><strong>Folder:</strong> {{ project.folder_name }}</p>
      <a href="{% url 'microproject_detail' project.id %}" class="btn btn-primary">
        View Details
      </a>
      <a href="/microprojects/{{ project.folder_name }}/" class="btn btn-secondary">
        Access Files
      </a>
    </div>
    {% endfor %}
  </div>
</div>
{% endfor %}
```

## File Access

Microproject files are located at:
```
/microprojects/MICROPROJECT_X_Y/
```

To serve these files, add to your Django settings:

```python
# settings.py
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'microprojects'),
]

# For development - serve media
MEDIA_URL = '/microprojects/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'microprojects')
```

## LMS Connection Info in Each README

Each microproject's README.md now includes an **LMS Integration** section with:
- Course code and name
- Unit number
- Assessment type
- Weight in course
- Submission path
- Grading criteria
- LMS-specific submission requirements

Example from each MP README:
```markdown
## 🔗 LMS Integration
**Course:** [316316 - Machine Learning](../courses/)  
**Unit:** Unit 1  
**Assessment Type:** Microproject  
**Weight in Course:** 8%  
**Submission Path:** LMS → Courses → Machine Learning → Unit 1 → Data Exploration Dashboard  
**Activity Name:** MICROPROJECT_1_1  
```

## Syncing Data

When new microprojects are added:

1. **Add folders** to `/microprojects/` directory
2. **Update README files** with LMS connection info using:
   ```bash
   python manage.py init_microprojects
   ```
3. **Refresh API** - endpoints automatically serve updated data
4. **Update website** - reload from API endpoints

## Integration Checklist

- [ ] Create microprojects listing page
- [ ] Add unit-based filtering
- [ ] Link to individual MP detail pages
- [ ] Embed README content in website
- [ ] Display file download buttons
- [ ] Show grading rubric
- [ ] Add submission guidelines
- [ ] Connect to course pages
- [ ] Display progress tracking (if authenticated)

## Database Schema

The microprojects are stored in the Activity model:

```python
class Activity(models.Model):
    subject = ForeignKey(Subject)  # 316316 - Machine Learning
    title = CharField(max_length=200)  # e.g., "Data Exploration Dashboard"
    unit = IntegerField()  # 1-7 (Unit 7 is Advanced)
    activity_type = CharField(choices=[..., ('microproject', 'Microproject')])
    max_marks = IntegerField()  # 100 for all MPs
```

## Troubleshooting

### API returns no data
- Ensure migrations are run: `python manage.py migrate`
- Verify `init_microprojects` command was executed
- Check if Subject "316316 - Machine Learning" exists in admin

### Files not accessible
- Verify files copied to `/microprojects/` directory
- Check file permissions
- Ensure Django MEDIA settings configured

### Website not showing updates
- Clear browser cache
- Restart Django development server
- Check API endpoint directly in browser

## Support

For questions about integrating microprojects:
1. Check the LMS admin panel for Activity records
2. Review API responses in browser developer tools
3. Verify folder structure matches expected layout
4. Check Django logs for errors

---

**Last Updated:** January 13, 2026
