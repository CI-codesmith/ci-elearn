#!/usr/bin/env python3
"""
Create blank Jupyter notebooks for all practicals with detailed information headers.
Students can paste their work in the blank code cells provided.
"""

import json
import os
from pathlib import Path

# Practical information
practicals = [
    {
        "number": 1,
        "title": "Installation of IDE with Necessary Libraries",
        "duration": "2 Hours",
        "cos": ["CO1"],
        "key_topics": ["Python setup", "Virtual environment", "ML libraries", "Jupyter Notebook", "Testing installation"],
        "description": "Set up Python development environment with essential ML libraries and verify installation."
    },
    {
        "number": 2,
        "title": "Data Preprocessing Techniques",
        "duration": "2 Hours",
        "cos": ["CO1", "CO2"],
        "key_topics": ["Missing values", "Outlier detection", "Feature scaling", "Encoding", "Data transformation"],
        "description": "Learn and implement various data preprocessing and cleaning techniques."
    },
    {
        "number": 3,
        "title": "Reading Datasets (Text, CSV, JSON, XML)",
        "duration": "2 Hours",
        "cos": ["CO2"],
        "key_topics": ["CSV", "JSON", "XML parsing", "File I/O", "Data validation", "Format conversion"],
        "description": "Read and parse datasets in multiple formats and prepare them for analysis."
    },
    {
        "number": 4,
        "title": "Classification Algorithms",
        "duration": "4 Hours",
        "cos": ["CO2", "CO3", "CO4"],
        "key_topics": ["Logistic Regression", "Decision Trees", "Random Forest", "SVM", "Naive Bayes", "Model evaluation"],
        "description": "Implement and compare various classification algorithms on different datasets."
    },
    {
        "number": 5,
        "title": "Regression Models",
        "duration": "4 Hours",
        "cos": ["CO2", "CO4"],
        "key_topics": ["Linear Regression", "Polynomial Regression", "Ridge/Lasso", "SVR", "Ensemble methods"],
        "description": "Implement and evaluate different regression models for predictive analysis."
    },
    {
        "number": 6,
        "title": "Clustering Algorithms",
        "duration": "2 Hours",
        "cos": ["CO3", "CO4"],
        "key_topics": ["K-Means", "Hierarchical Clustering", "DBSCAN", "GMM", "Silhouette analysis"],
        "description": "Implement various clustering algorithms and evaluate cluster quality."
    },
    {
        "number": 7,
        "title": "Dimensionality Reduction",
        "duration": "2 Hours",
        "cos": ["CO3", "CO4"],
        "key_topics": ["PCA", "LDA", "t-SNE", "UMAP", "Feature selection", "Autoencoder"],
        "description": "Apply dimensionality reduction techniques to high-dimensional datasets."
    },
    {
        "number": 8,
        "title": "Model Evaluation and Validation",
        "duration": "2 Hours",
        "cos": ["CO4"],
        "key_topics": ["Classification metrics", "Regression metrics", "Cross-validation", "Hyperparameter tuning", "Bias-Variance"],
        "description": "Evaluate and validate machine learning models using various metrics and techniques."
    },
    {
        "number": 9,
        "title": "Feature Extraction and Transformation",
        "duration": "2 Hours",
        "cos": ["CO1", "CO3"],
        "key_topics": ["Polynomial features", "Text extraction", "TF-IDF", "Word embeddings", "Feature pipelines"],
        "description": "Extract and transform features from raw data for machine learning models."
    },
    {
        "number": 10,
        "title": "Ensemble Learning Methods",
        "duration": "2 Hours",
        "cos": ["CO4", "CO5"],
        "key_topics": ["Bagging", "Boosting", "XGBoost", "Stacking", "Voting", "LightGBM", "CatBoost"],
        "description": "Implement ensemble learning methods to improve model performance."
    },
    {
        "number": 11,
        "title": "Advanced Optimization Techniques",
        "duration": "2 Hours",
        "cos": ["CO4", "CO5"],
        "key_topics": ["Gradient Descent variants", "Momentum", "Adam", "Learning rate scheduling", "Bayesian optimization"],
        "description": "Learn and implement advanced optimization techniques for neural networks and models."
    },
    {
        "number": 12,
        "title": "Time Series Analysis and Forecasting",
        "duration": "2 Hours",
        "cos": ["CO2", "CO4", "CO5"],
        "key_topics": ["Decomposition", "ARIMA", "SARIMA", "Exponential smoothing", "LSTM", "Prophet"],
        "description": "Analyze time series data and implement forecasting models."
    },
    {
        "number": 13,
        "title": "Anomaly Detection",
        "duration": "2 Hours",
        "cos": ["CO3", "CO4", "CO5"],
        "key_topics": ["Statistical methods", "Isolation Forest", "LOF", "One-class SVM", "Autoencoder"],
        "description": "Detect anomalies and outliers in datasets using various techniques."
    },
    {
        "number": 14,
        "title": "ML Model on Boston Housing Dataset",
        "duration": "2 Hours",
        "cos": ["CO4", "CO5"],
        "key_topics": ["Complete ML pipeline", "EDA", "Feature engineering", "Model comparison", "Deployment"],
        "description": "Build an end-to-end ML pipeline with the Boston Housing dataset."
    },
    {
        "number": 15,
        "title": "Customer Segmentation using K-Means Clustering",
        "duration": "4 Hours",
        "cos": ["CO4", "CO5"],
        "key_topics": ["K-Means", "Elbow method", "Silhouette analysis", "RFM analysis", "Business insights"],
        "description": "Perform customer segmentation using clustering techniques."
    }
]

def create_notebook(practical_info, output_path):
    """Create a Jupyter notebook for a practical with information header and blank cells."""
    
    # Create the notebook structure
    notebook = {
        "cells": [],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.9.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    # Create information header
    header_markdown = f"""# Practical {practical_info['number']}: {practical_info['title']}

## Practical Information

| Attribute | Details |
|-----------|---------|
| **Practical Number** | {practical_info['number']} |
| **Title** | {practical_info['title']} |
| **Duration** | {practical_info['duration']} |
| **Course Outcomes (COs)** | {', '.join(practical_info['cos'])} |
| **Description** | {practical_info['description']} |

## Key Topics Covered

{chr(10).join([f'- {topic}' for topic in practical_info['key_topics']])}

---

## Instructions for Students

1. **Complete all tasks** outlined in this practical
2. **Write your code** in the cells provided below
3. **Add comments** to explain your code
4. **Include proper output** (prints, visualizations, etc.)
5. **Submit your completed notebook** before the deadline

---

## Your Work Starts Here

Use the cell(s) below to write your implementation:
"""
    
    # Add header cell
    notebook["cells"].append({
        "cell_type": "markdown",
        "metadata": {},
        "source": header_markdown.split('\n')
    })
    
    # Add blank code cell for student work
    notebook["cells"].append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Practical {}: {}\n".format(practical_info['number'], practical_info['title']),
            "# Write your implementation here\n",
            "\n",
            "\n"
        ]
    })
    
    # Add additional blank code cells for flexibility
    for i in range(2):
        notebook["cells"].append({
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Additional code cell\n",
                "\n",
                "\n"
            ]
        })
    
    # Write notebook to file
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Created: {output_path}")

def main():
    """Main function to create all practical notebooks."""
    base_path = Path("/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/ML_Course/practicals")
    
    print("\n📓 Creating Student Notebooks for All Practicals\n")
    print("=" * 70)
    
    for practical in practicals:
        practical_folder = base_path / f"practical_{practical['number']}"
        
        # Create practical folder if it doesn't exist
        practical_folder.mkdir(parents=True, exist_ok=True)
        
        # Create notebook filename
        notebook_filename = f"Practical_{practical['number']}_STUDENT_NOTEBOOK.ipynb"
        notebook_path = practical_folder / notebook_filename
        
        # Create the notebook
        create_notebook(practical, notebook_path)
    
    print("=" * 70)
    print(f"\n✅ Successfully created {len(practicals)} student notebooks!")
    print("\n📍 Location: ML_Course/practicals/practical_[number]/")
    print("📝 Filename Format: Practical_[number]_STUDENT_NOTEBOOK.ipynb")
    print("\n🎓 Students can now download and submit their work!\n")

if __name__ == "__main__":
    main()
