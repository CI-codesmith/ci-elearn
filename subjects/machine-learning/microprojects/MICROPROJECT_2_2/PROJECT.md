# MICROPROJECT 2.3: Data Encoding and Categorical Variables (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 2 (Data Preparation)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + CSV + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to split a dataset into training and testing sets using pandas and Scikit-learn. Understand why splitting is important for ML.

---

## 📋 Requirements

### Task 1: Load a Dataset
- Use pandas to load a small dataset (e.g., Iris, Titanic, or any CSV)

### Task 2: Train-Test Split
### Task 2: Identify Categorical Variables
- Find all categorical columns in the dataset
- Show their unique values and counts

### Task 3: Encode Categorical Variables
- Use pandas or Scikit-learn to encode categorical variables (one-hot encoding or label encoding)
- Explain your choices in markdown

### Task 4: Save Encoded Data
- Save the encoded dataset as a new CSV file
---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Train and test CSV files
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP2_2_Group[ID]_Classification.ipynb`
- **Include:** Complete implementation, evaluation, visualizations

### 2. Model Comparison Report (20% weight)
- **File:** `MP2_2_Group[ID]_Report.pdf`
- **Content:** Algorithm comparison, best model analysis

### 3. Performance Visualization (15% weight)
- **File:** `MP2_2_Group[ID]_Visualizations.pdf`
- **Content:** ROC curves, confusion matrices, metric comparisons

### 4. Group Presentation (15% weight)
- **File:** `MP2_2_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Preprocessing** | Handles class imbalance, proper encoding | Good preprocessing | Basic preprocessing | Poor/inadequate |
| **Model Implementation** | 4+ models, proper tuning | 4 models, basic tuning | 3 models | 1-2 models or broken |
| **Evaluation Metrics** | Comprehensive metrics, ROC analysis | Good metrics coverage | Basic metrics | Incorrect metrics |
| **Model Comparison** | Detailed comparison, use-case driven | Good comparison | Basic comparison | No comparison |
| **Code Quality** | Clean, modular, documented | Mostly clean | Functional | Messy/broken |
| **Visualization** | Excellent plots, confusion matrices | Good plots | Basic plots | Poor quality |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 2.2: Classification Challenge
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, auc

# 1. DATA LOADING & PREPROCESSING
# df = pd.read_csv('titanic.csv')

# Handle missing values, encode categorical variables
# Scale features if needed

# 2. TRAIN/TEST SPLIT
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. MODEL TRAINING
models = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(probability=True, random_state=42)
}

results = {}

for name, model in models.items():
    # Train model
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    auc_score = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else 'N/A'
    
    results[name] = {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1': f1,
        'auc': auc_score,
        'model': model,
        'predictions': y_pred,
        'probabilities': y_pred_proba
    }
    
    print(f"{name}:")
    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  F1-Score: {f1:.4f}")
    if auc_score != 'N/A':
        print(f"  AUC-ROC: {auc_score:.4f}")
    print()

# 4. VISUALIZATION
# Confusion Matrices
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

for i, (name, result) in enumerate(results.items()):
    cm = confusion_matrix(y_test, result['predictions'])
    sns.heatmap(cm, annot=True, fmt='d', ax=axes[i], cmap='Blues')
    axes[i].set_title(f'{name} Confusion Matrix')
    axes[i].set_xlabel('Predicted')
    axes[i].set_ylabel('Actual')

plt.tight_layout()
plt.savefig('confusion_matrices.png')
plt.show()

# ROC Curves
plt.figure(figsize=(10, 8))
for name, result in results.items():
    if result['probabilities'] is not None:
        fpr, tpr, _ = roc_curve(y_test, result['probabilities'])
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.2f})')

plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curves')
plt.legend()
plt.savefig('roc_curves.png')
plt.show()

# 5. BEST MODEL SELECTION
# Choose based on primary metric (e.g., F1 for imbalanced, Accuracy for balanced)
best_model_name = max(results.keys(), key=lambda x: results[x]['f1'])
best_model = results[best_model_name]

print(f"Best Model: {best_model_name}")
print(f"F1-Score: {best_model['f1']:.4f}")
print(f"Accuracy: {best_model['accuracy']:.4f}")

# Feature importance (for tree-based models)
if hasattr(best_model['model'], 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': best_model['model'].feature_importances_
    }).sort_values('importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=feature_importance.head(10))
    plt.title('Top 10 Feature Importances')
    plt.savefig('feature_importance.png')
    plt.show()
```

---

## 🆘 Resources
- Scikit-learn classification guide
- Imbalanced-learn for class imbalance
- Course practicals 4 reference

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_2_2.md