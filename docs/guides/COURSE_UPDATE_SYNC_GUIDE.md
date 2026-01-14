# CI-ELEARN LMS: Course Update Sync Guide
**Date:** January 14, 2026  
**Status:** Ready for Implementation  
**Source:** ci-elearn GitHub Repository (Main Branch)

---

## 📋 Executive Summary

The main **ci-elearn** repository has been updated with the complete **MSBTE K-Scheme Machine Learning (Course 316316, Semester 6)** curriculum. This document outlines all changes and provides step-by-step instructions to sync the LMS database and content.

---

## 🎯 Changes Made to ci-elearn Repository

### ✅ **Curriculum Alignment**
- **Structure:** Realigned from 6 units → **5 MSBTE-aligned units**
- **Old Structure Removed:** 
  - Unit 6 (Ethics & Applications)
  - Advanced Microprojects folder
  
- **New 5-Unit Structure:**
  1. **Unit I:** Introduction to Machine Learning
  2. **Unit II:** Data Preprocessing
  3. **Unit III:** Feature Selection
  4. **Unit IV:** Supervised Learning
  5. **Unit V:** Unsupervised Learning

### ✅ **Microprojects (18 Total)**
- **Distribution:** 4-5 projects per unit
- **Weight:** 75% of course assessment
- **Folder Structure:** `MICROPROJECT_X_Y/` with:
  - `README.md` - Project overview & LMS info
  - `PROJECT.md` - Detailed specification
  - `HOW_TO_DO.md` - Implementation guide
  - `DATASET.md` - Data sources
  - `SOLUTION_TEMPLATE.ipynb` - Student template
  - `SAMPLE_SOLUTION.ipynb` - Reference solution

### ✅ **Practicals (15 Total)**
- **Location:** `subjects/machine-learning/practicals/`
- **Naming:** `practical_1` through `practical_15`
- **Contents per practical:**
  - `Comprehensive.md` - Full specification
  - `Complete_Notebook.ipynb` - Full solution
  - `STUDENT_NOTEBOOK.ipynb` - Blank template
  - `SUBMISSION_TEMPLATE.md` - Submission format
  - `README.md` - Quick start

### ✅ **Assessments (4 Types)**
- **Location:** `subjects/machine-learning/assessments/`
- **Types:**
  - **Weekly Tests (WT):** 5 papers (WT1-WT5)
  - **Class Tests:** 2 papers (Class_Test_1, Class_Test_2)
  - **Prelim Exams:** 2 papers (Prelim_Exam_1, Prelim_Exam_2)
  - **ML_Quest:** Interactive quizzes with wordcloud analysis

### ✅ **Multimedia Integration**
- **Gamma Presentations:** 6 interactive embeds
  - 1 Intro presentation
  - 5 Unit presentations
- **Spotify Podcasts:** 7 episodes embedded
  - Distributed across all 5 units
- **Resource Reference:** `COURSE_RESOURCES_REFERENCE.md` (all embed IDs & links)

### ✅ **Documentation Updates**
- `course-overview.md` - Updated with intro podcast & resources
- `index.md` - Quick start guide & resource table
- `microprojects/INDEX.md` - Master index of all 18 projects
- `microprojects/overview.md` - Project listing by unit

---

## 🗄️ LMS Database Update Instructions

### **Step 1: Activate Virtual Environment**
```bash
cd /Users/akashchatake/Downloads/Chatake-Innoworks-Organization/ci-elearn-lms
source venv/bin/activate
```

### **Step 2: Create/Update Subjects**
```bash
python manage.py shell
```

```python
from courses.models import Subject

# Machine Learning Course
ml_subject, created = Subject.objects.get_or_create(
    code="316316",
    defaults={"name": "Machine Learning (K-Scheme)"}
)
print(f"ML Subject: {ml_subject.name} {'[Created]' if created else '[Updated]'}")
```

### **Step 3: Create/Update Units**
```python
from courses.models import Unit  # Adjust if model name differs

units_data = [
    {"number": 1, "name": "Introduction to Machine Learning", "description": "ML basics, types, and Python fundamentals"},
    {"number": 2, "name": "Data Preprocessing", "description": "Data cleaning, handling missing values, normalization"},
    {"number": 3, "name": "Feature Selection", "description": "Feature scaling, selection methods, dimensionality reduction"},
    {"number": 4, "name": "Supervised Learning", "description": "Classification, regression, model evaluation"},
    {"number": 5, "name": "Unsupervised Learning", "description": "Clustering, PCA, dimensionality reduction"},
]

for unit_data in units_data:
    unit, created = Unit.objects.get_or_create(
        subject=ml_subject,
        number=unit_data["number"],
        defaults={
            "name": unit_data["name"],
            "description": unit_data["description"],
            "gamma_embed_id": None,  # Add Gamma IDs from COURSE_RESOURCES_REFERENCE.md
            "podcast_url": None,  # Add Spotify URLs
        }
    )
    print(f"Unit {unit.number}: {unit.name} {'[Created]' if created else '[Updated]'}")
```

### **Step 4: Create/Update Microprojects**
```python
from microprojects.models import Microproject

microprojects_data = [
    # Unit I (4 projects)
    {"unit": 1, "seq": 1, "name": "ML Basics & Python Fundamentals", "weight": 8},
    {"unit": 1, "seq": 2, "name": "Python ML Libraries (NumPy, Pandas, Matplotlib)", "weight": 8},
    {"unit": 1, "seq": 3, "name": "Types of ML & Real-World Applications", "weight": 8},
    {"unit": 1, "seq": 4, "name": "Exploratory Data Analysis (EDA)", "weight": 9},
    
    # Unit II (5 projects)
    {"unit": 2, "seq": 1, "name": "Data Cleaning Techniques", "weight": 10},
    {"unit": 2, "seq": 2, "name": "Handling Missing Data", "weight": 10},
    {"unit": 2, "seq": 3, "name": "Dataset Splitting (Train/Test/Validation)", "weight": 10},
    {"unit": 2, "seq": 4, "name": "Data Transformation & Normalization", "weight": 12},
    {"unit": 2, "seq": 5, "name": "Preprocessing Pipeline Implementation", "weight": 12},
    
    # Unit III (3 projects)
    {"unit": 3, "seq": 1, "name": "Feature Scaling & Standardization", "weight": 10},
    {"unit": 3, "seq": 2, "name": "Feature Selection Methods", "weight": 10},
    {"unit": 3, "seq": 3, "name": "Feature Extraction Techniques", "weight": 10},
    
    # Unit IV (3 projects)
    {"unit": 4, "seq": 1, "name": "Classification Algorithms (Decision Trees, KNN, SVM)", "weight": 10},
    {"unit": 4, "seq": 2, "name": "Regression Algorithms (Linear, Logistic)", "weight": 10},
    {"unit": 4, "seq": 3, "name": "Model Performance Evaluation & Metrics", "weight": 12},
    
    # Unit V (3 projects)
    {"unit": 5, "seq": 1, "name": "Clustering Basics (K-Means, Hierarchical)", "weight": 10},
    {"unit": 5, "seq": 2, "name": "Advanced Clustering Techniques", "weight": 10},
    {"unit": 5, "seq": 3, "name": "Dimensionality Reduction & PCA", "weight": 12},
]

for mp in microprojects_data:
    unit = Unit.objects.get(subject=ml_subject, number=mp["unit"])
    project, created = Microproject.objects.get_or_create(
        unit=unit,
        sequence=mp["seq"],
        defaults={
            "title": mp["name"],
            "weight": mp["weight"],
            "folder_path": f"MICROPROJECT_{mp['unit']}_{mp['seq']}",
            "github_url": f"https://github.com/CI-codesmith/ci-elearn/tree/main/subjects/machine-learning/microprojects/MICROPROJECT_{mp['unit']}_{mp['seq']}",
        }
    )
    print(f"MP {mp['unit']}.{mp['seq']}: {project.title} {'[Created]' if created else '[Updated]'}")
```

### **Step 5: Create/Update Practicals**
```python
from practicals.models import Practical  # Adjust model name as needed

for i in range(1, 16):
    practical, created = Practical.objects.get_or_create(
        number=i,
        defaults={
            "title": f"Practical {i}",
            "folder_path": f"practical_{i}",
            "github_url": f"https://github.com/CI-codesmith/ci-elearn/tree/main/subjects/machine-learning/practicals/practical_{i}",
            "weight": 1.0,  # Each practical = 1/15 of practicals weight
        }
    )
    print(f"Practical {i} {'[Created]' if created else '[Updated]'}")
```

### **Step 6: Create/Update Assessments**
```python
from assessments.models import Assessment, AssessmentType

# Define assessment types
assessment_types = [
    {"code": "WT", "name": "Weekly Test", "count": 5},
    {"code": "CT", "name": "Class Test", "count": 2},
    {"code": "PE", "name": "Prelim Exam", "count": 2},
    {"code": "MQ", "name": "ML Quest (Quiz)", "count": 1},
]

for at in assessment_types:
    for i in range(1, at["count"] + 1):
        assessment, created = Assessment.objects.get_or_create(
            code=f"{at['code']}{i}",
            defaults={
                "type": at["code"],
                "title": f"{at['name']} {i}",
                "github_url": f"https://github.com/CI-codesmith/ci-elearn/tree/main/subjects/machine-learning/assessments/{at['code']}",
            }
        )
        print(f"Assessment {at['code']}{i} {'[Created]' if created else '[Updated]'}")
```

### **Step 7: Verify Data**
```python
# Check all counts
print(f"\n=== VERIFICATION ===")
print(f"Subjects: {Subject.objects.count()}")
print(f"Units: {Unit.objects.filter(subject=ml_subject).count()}")
print(f"Microprojects: {Microproject.objects.filter(unit__subject=ml_subject).count()}")
```

---

## 📱 Google Classroom Integration

### **To Link Google Classroom Materials:**

1. **Access Google Drive:** `chatakeinnoworks@gmail.com`
2. **Create/Update Classroom:**
   - Course Code: **316316**
   - Course Name: **Machine Learning (K-Scheme)**
   
3. **Map LMS Content to Classroom:**
   - **Topics:** One per unit (Unit I-V)
   - **Assignments:** Link to microprojects (MICROPROJECT_X_Y)
   - **Materials:** Link to practicals and assessments

4. **Add Links in LMS:**
   ```
   Unit > Google Classroom Link:
   https://classroom.google.com/c/[CLASSROOM_ID]/a/[ASSIGNMENT_ID]
   ```

### **Classroom Structure:**
```
📚 Machine Learning (316316)
├── 📖 Unit I: Introduction to ML
│   ├── 📝 MICROPROJECT_1_1 through 1_4
│   └── 📎 Practical materials
├── 📖 Unit II: Data Preprocessing
│   ├── 📝 MICROPROJECT_2_1 through 2_5
│   └── 📎 Practical materials
├── 📖 Unit III: Feature Selection
├── 📖 Unit IV: Supervised Learning
├── 📖 Unit V: Unsupervised Learning
└── 📋 Assessments
    ├── Weekly Tests (WT1-WT5)
    ├── Class Tests (CT1-CT2)
    ├── Prelim Exams (PE1-PE2)
    └── ML Quests
```

---

## 🔗 Resource References

### **Gamma Embed IDs (from ci-elearn COURSE_RESOURCES_REFERENCE.md)**
- Intro Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`
- Unit I Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`
- Unit II Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`
- Unit III Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`
- Unit IV Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`
- Unit V Presentation: `[Check COURSE_RESOURCES_REFERENCE.md]`

### **Spotify Podcast URLs (7 Episodes)**
All episodes available in: `ci-elearn/subjects/machine-learning/COURSE_RESOURCES_REFERENCE.md`

### **GitHub Repository Links**
- Main Course Site: https://github.com/CI-codesmith/ci-elearn
- LMS Project: https://github.com/CI-codesmith/ci-elearn-lms
- Live Site: https://ci-codesmith.github.io/ci-elearn/

---

## 📊 Data Mapping Summary

| Element | Count | Distribution | Weight |
|---------|-------|--------------|--------|
| **Units** | 5 | Equal coverage | - |
| **Microprojects** | 18 | 4-5 per unit | 75% |
| **Practicals** | 15 | 3 per unit | 15% |
| **Assessments** | 10 | Various types | 10% |
| **Total Weight** | - | - | **100%** |

---

## ⚙️ Next Steps

1. **Activate venv** and run Django shell commands (Step 1-7 above)
2. **Verify database entries** created successfully
3. **Test LMS UI** to ensure all units/projects display correctly
4. **Set up Google Classroom** mapping
5. **Deploy updated LMS** to production
6. **Notify students** of course structure update

---

## 📝 Notes

- All microproject files are in markdown + Jupyter notebooks
- Course resources (embeds, podcasts) are permanently stored in `COURSE_RESOURCES_REFERENCE.md`
- Assessment files are in Word format (.docx) - consider converting to web-accessible format
- Practical notebooks include both complete solutions and student templates
- All content is Git-versioned and tracked in ci-elearn repository

---

**Last Updated:** January 14, 2026  
**Ready for Implementation:** ✅ YES
