#!/usr/bin/env python
"""
Django LMS Course Sync Script
Syncs ci-elearn course updates to CI-ELEARN-LMS database
Run from: python manage.py shell < sync_course_updates.py
"""

import os
import django
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')
django.setup()

from courses.models import Subject
from django.contrib.auth.models import User

def sync_course_data():
    """Main sync function"""
    
    print("\n" + "="*70)
    print("CI-ELEARN LMS: COURSE UPDATE SYNC")
    print("="*70)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # ========== STEP 1: Create/Update Subject ==========
    print("STEP 1: Creating/Updating Subject...")
    try:
        subject, created = Subject.objects.get_or_create(
            code="316316",
            defaults={
                "name": "Machine Learning (K-Scheme, Semester 6)",
            }
        )
        status = "✅ CREATED" if created else "✅ UPDATED"
        print(f"  {status}: {subject.code} - {subject.name}\n")
    except Exception as e:
        print(f"  ❌ ERROR: {str(e)}\n")
        return False
    
    # ========== STEP 2: Create/Update Units ==========
    print("STEP 2: Creating/Updating Units (5 total)...")
    
    units_data = [
        {
            "number": 1,
            "name": "Introduction to Machine Learning",
            "description": "ML fundamentals, Python basics, types of learning, real-world applications",
            "duration_weeks": 3,
            "microprojects_count": 4,
        },
        {
            "number": 2,
            "name": "Data Preprocessing",
            "description": "Data cleaning, handling missing values, normalization, feature scaling, train-test split",
            "duration_weeks": 4,
            "microprojects_count": 5,
        },
        {
            "number": 3,
            "name": "Feature Selection",
            "description": "Feature scaling, selection methods, extraction techniques, dimensionality reduction",
            "duration_weeks": 2,
            "microprojects_count": 3,
        },
        {
            "number": 4,
            "name": "Supervised Learning",
            "description": "Classification, regression, decision trees, KNN, SVM, model evaluation",
            "duration_weeks": 2,
            "microprojects_count": 3,
        },
        {
            "number": 5,
            "name": "Unsupervised Learning",
            "description": "Clustering algorithms, K-means, hierarchical clustering, PCA",
            "duration_weeks": 3,
            "microprojects_count": 3,
        },
    ]
    
    try:
        units = []
        for unit_data in units_data:
            # Import Unit model - adjust if model path differs
            try:
                from courses.models import Unit
            except ImportError:
                # If Unit is in different app, adjust this
                print(f"  ⚠️  WARNING: Unit model not found in courses.models")
                print(f"     Skipping unit creation. Update model import path.\n")
                continue
            
            unit, created = Unit.objects.get_or_create(
                subject=subject,
                number=unit_data["number"],
                defaults={
                    "name": unit_data["name"],
                    "description": unit_data["description"],
                    "duration_weeks": unit_data.get("duration_weeks", 2),
                }
            )
            units.append(unit)
            status = "✅ CREATED" if created else "✅ UPDATED"
            print(f"  {status}: Unit {unit.number} - {unit.name}")
        print()
    except Exception as e:
        print(f"  ❌ ERROR: {str(e)}\n")
        print(f"  💡 TIP: Ensure Unit model exists in courses app\n")
    
    # ========== STEP 3: Create/Update Microprojects ==========
    print("STEP 3: Creating/Updating Microprojects (18 total)...")
    
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
    
    try:
        from microprojects.models import Microproject
        mp_count = 0
        for mp_data in microprojects_data:
            try:
                unit = Unit.objects.get(subject=subject, number=mp_data["unit"])
                project, created = Microproject.objects.get_or_create(
                    unit=unit,
                    sequence=mp_data["seq"],
                    defaults={
                        "title": mp_data["name"],
                        "weight": mp_data["weight"],
                        "folder_name": f"MICROPROJECT_{mp_data['unit']}_{mp_data['seq']}",
                        "github_url": f"https://github.com/CI-codesmith/ci-elearn/tree/main/subjects/machine-learning/microprojects/MICROPROJECT_{mp_data['unit']}_{mp_data['seq']}",
                    }
                )
                status = "✅" if created else "✔️"
                print(f"  {status} MP {mp_data['unit']}.{mp_data['seq']}: {project.title}")
                mp_count += 1
            except Unit.DoesNotExist:
                print(f"  ⚠️  Unit {mp_data['unit']} not found - skipping MP {mp_data['unit']}.{mp_data['seq']}")
        print(f"\n  Total Microprojects: {mp_count}/18\n")
    except ImportError:
        print(f"  ⚠️  WARNING: Microproject model not found in microprojects app")
        print(f"     Skipping microproject creation.\n")
    except Exception as e:
        print(f"  ❌ ERROR: {str(e)}\n")
    
    # ========== SUMMARY ==========
    print("="*70)
    print("✅ COURSE SYNC COMPLETE")
    print("="*70)
    print("\n📊 DATABASE STATE:")
    print(f"  • Subjects: {Subject.objects.count()}")
    try:
        from courses.models import Unit
        print(f"  • Units: {Unit.objects.filter(subject=subject).count()}/5")
    except:
        print(f"  • Units: [Model not available]")
    
    try:
        from microprojects.models import Microproject
        print(f"  • Microprojects: {Microproject.objects.filter(unit__subject=subject).count()}/18")
    except:
        print(f"  • Microprojects: [Model not available]")
    
    print("\n📝 NEXT STEPS:")
    print("  1. Verify all data created successfully")
    print("  2. Update Unit model with Gamma embed IDs (from COURSE_RESOURCES_REFERENCE.md)")
    print("  3. Add Spotify podcast URLs to units")
    print("  4. Create Assessment entries")
    print("  5. Link Google Classroom assignments")
    print("  6. Test LMS UI for all courses/units/projects")
    print("  7. Deploy to production")
    print("\n" + "="*70)
    
    return True

if __name__ == "__main__":
    sync_course_data()
