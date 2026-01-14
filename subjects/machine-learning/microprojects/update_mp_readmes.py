#!/usr/bin/env python3
"""
Script to update all Microproject README files with LMS unit connections
Maps microprojects to course units and assessment activities
"""

import os
import re

# Mapping of microprojects to units and their details
MP_MAPPING = {
    "MICROPROJECT_1_1": {
        "unit": 1,
        "title": "Data Exploration Dashboard",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 8
    },
    "MICROPROJECT_1_2": {
        "unit": 1,
        "title": "Python ML Libraries Mastery",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 8
    },
    "MICROPROJECT_1_3": {
        "unit": 1,
        "title": "Traditional vs ML Comparison",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 8
    },
    "MICROPROJECT_1_4": {
        "unit": 1,
        "title": "Dataset Curation Project",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 9
    },
    "MICROPROJECT_2_1": {
        "unit": 2,
        "title": "Data Cleaning & Preprocessing",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_2_2": {
        "unit": 2,
        "title": "Handling Missing Values",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_2_3": {
        "unit": 2,
        "title": "Data Encoding & Scaling",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_2_4": {
        "unit": 2,
        "title": "Feature Engineering Basics",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 12
    },
    "MICROPROJECT_2_5": {
        "unit": 2,
        "title": "Data Visualization & Analysis",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 12
    },
    "MICROPROJECT_3_1": {
        "unit": 3,
        "title": "Feature Selection Methods",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_3_2": {
        "unit": 3,
        "title": "Correlation Analysis",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_3_3": {
        "unit": 3,
        "title": "Removing Irrelevant Features",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_4_1": {
        "unit": 4,
        "title": "Classification Algorithms",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_4_2": {
        "unit": 4,
        "title": "Regression Algorithms",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_4_3": {
        "unit": 4,
        "title": "Model Evaluation & Metrics",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 12
    },
    "MICROPROJECT_5_1": {
        "unit": 5,
        "title": "Clustering Techniques",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_5_2": {
        "unit": 5,
        "title": "Clustering Comparison",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_5_3": {
        "unit": 5,
        "title": "PCA & Dimensionality Reduction",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 12
    },
    "MICROPROJECT_6_1": {
        "unit": 6,
        "title": "ML Ethics & Bias",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_6_2": {
        "unit": 6,
        "title": "Model Deployment & Production",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 12
    },
    "MICROPROJECT_6_3": {
        "unit": 6,
        "title": "Real-World ML Applications",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 10
    },
    "MICROPROJECT_ADVANCED_1": {
        "unit": 7,
        "title": "End-to-End ML Pipeline with Production",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 0,
        "advanced": True
    },
    "MICROPROJECT_ADVANCED_2": {
        "unit": 7,
        "title": "Deep Learning for Image Classification",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 0,
        "advanced": True
    },
    "MICROPROJECT_ADVANCED_3": {
        "unit": 7,
        "title": "Time Series Forecasting (ARIMA & LSTM)",
        "course_code": "316316",
        "course_name": "Machine Learning",
        "weight_percentage": 0,
        "advanced": True
    }
}

def get_lms_connection_section(mp_folder):
    """Generate the LMS connection section for a microproject"""
    if mp_folder not in MP_MAPPING:
        return ""
    
    mp_info = MP_MAPPING[mp_folder]
    is_advanced = mp_info.get("advanced", False)
    
    lms_section = f"""
## 🔗 LMS Integration
**Course:** [{mp_info['course_code']} - {mp_info['course_name']}](../courses/)  
**Unit:** Unit {mp_info['unit']}  
**Assessment Type:** Microproject  
"""
    
    if is_advanced:
        lms_section += "**Difficulty:** Advanced (Optional - For High Performers)  \n"
        lms_section += "**Weight:** Extra Credit  \n"
    else:
        lms_section += f"**Weight in Course:** {mp_info['weight_percentage']}%  \n"
        lms_section += f"**Submission Path:** LMS → Courses → {mp_info['course_name']} → Unit {mp_info['unit']} → {mp_info['title']}  \n"
    
    lms_section += f"**Activity Name:** {mp_folder}  \n"
    lms_section += f"""
### Submission Requirements (via LMS)
- Submit your completed work through the LMS submission portal
- Include all required files: Jupyter Notebook, datasets, documentation
- Follow the file naming convention: `MP{mp_info['unit']}_[StudentName]_[Dataset].[ext]`
- Late submissions incur 10% penalty per day (48-hour grace period available upon request)
- Maximum re-submissions allowed: 1 (within 1 week of feedback)

### Grading Criteria (LMS Assessment)
- **Code Implementation:** 40%
- **Analysis/Insights:** 30%
- **Documentation:** 20%
- **Presentation:** 10%

"""
    return lms_section

def update_readme(mp_folder_path, mp_folder_name):
    """Update the README.md file of a microproject with LMS connections"""
    readme_path = os.path.join(mp_folder_path, "README.md")
    
    if not os.path.exists(readme_path):
        print(f"⚠️  No README.md found in {mp_folder_name}")
        return False
    
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if LMS section already exists
        if "## 🔗 LMS Integration" in content:
            print(f"✓ {mp_folder_name} - LMS section already exists, skipping")
            return True
        
        # Generate LMS connection section
        lms_section = get_lms_connection_section(mp_folder_name)
        if not lms_section:
            print(f"⚠️  No mapping found for {mp_folder_name}")
            return False
        
        # Find the best position to insert (after 🎓 Difficulty Level or 📁 Folder Contents)
        difficulty_pattern = r"(## 🎓 Difficulty Level.*?\n)"
        folder_pattern = r"(## 📁 Folder Contents.*?\n)"
        
        # Try to insert after difficulty level first
        if re.search(difficulty_pattern, content, re.DOTALL):
            updated_content = re.sub(
                difficulty_pattern,
                r"\1" + lms_section,
                content,
                flags=re.DOTALL
            )
        else:
            # Otherwise insert before getting started
            getting_started_pattern = r"(## 🚀 Getting Started)"
            updated_content = re.sub(
                getting_started_pattern,
                lms_section + r"\1",
                content
            )
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✓ Updated {mp_folder_name}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {mp_folder_name}: {str(e)}")
        return False

def main():
    """Main function to process all microproject folders"""
    microprojects_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("Updating Microproject README files with LMS connections")
    print("=" * 60)
    
    # Get all MICROPROJECT folders
    mp_folders = [
        d for d in os.listdir(microprojects_dir)
        if d.startswith("MICROPROJECT_") and 
        os.path.isdir(os.path.join(microprojects_dir, d))
    ]
    
    mp_folders.sort()
    
    success_count = 0
    total_count = len(mp_folders)
    
    for mp_folder in mp_folders:
        mp_path = os.path.join(microprojects_dir, mp_folder)
        if update_readme(mp_path, mp_folder):
            success_count += 1
    
    print("=" * 60)
    print(f"Summary: {success_count}/{total_count} microprojects updated")
    print("=" * 60)
    
    return success_count == total_count

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
