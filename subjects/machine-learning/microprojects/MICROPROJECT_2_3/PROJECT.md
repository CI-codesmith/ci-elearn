# MICROPROJECT 2.4: Data Scaling and Normalization (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 2 (Data Preparation)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to scale features and select important features in a dataset using simple methods. Understand why these steps matter for ML.

---

## 📋 Requirements

### Task 1: Feature Scaling
- Use pandas and Scikit-learn to normalize or standardize features in a small dataset (e.g., Iris, Wine, or any CSV)
- Show beforLoad a Dataset
- Use pandas to load a small dataset (e.g., Iris, Wine, or any CSV)

### Task 2: Scale Features
- Show statistics (mean, min, max) before scaling
- Use Scikit-learn's StandardScaler or MinMaxScaler to scale features
- Show statistics after scaling

### Task 3: Explain Scaling
- Write a markdown cell explaining why scaling is important and when to use each method

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP2_3_Group[ID]_ModelSelection.ipynb`
- **Sections:** Data loading → Preprocessing → Modeling → Evaluation → Model selection

### 2. Model Comparison Report (20% weight)
- **File:** `MP2_3_Group[ID]_Report.pdf`
- **Content:** Model comparison, selection rationale, validation analysis

### 3. Visualizations (15% weight)
- **File:** `MP2_3_Group[ID]_Visualizations.pdf`
- **Content:** Boxplots, learning/validation curves

### 4. Presentation (15% weight)
- **File:** `MP2_3_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Preprocessing** | Handles all data issues, robust pipeline | Good preprocessing | Basic preprocessing | Poor/inadequate |
| **Model Implementation** | 4+ models, proper CV | 4 models, basic CV | 3 models | 1-2 models or broken |
| **Evaluation Metrics** | Comprehensive, visualized | Good metrics | Basic metrics | Incorrect metrics |
| **Model Selection** | Justified, robust, clear | Good selection | Basic selection | No justification |
| **Visualization** | Excellent plots, learning curves | Good plots | Basic plots | Poor quality |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 2.3: Model Evaluation & Selection
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold, KFold, validation_curve, learning_curve
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. PREPROCESSING
# ...

# 3. TRAIN/TEST SPLIT
# ...

# 4. MODEL TRAINING & CROSS-VALIDATION
models = {
	'Linear Regression': LinearRegression(),
	'Random Forest Regressor': RandomForestRegressor(n_estimators=100, random_state=42),
	'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
	'Random Forest Classifier': RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
	# Use KFold or StratifiedKFold as appropriate
	if 'Classifier' in name or 'Logistic' in name:
		cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
	else:
		cv = KFold(n_splits=5, shuffle=True, random_state=42)
	scores = cross_val_score(model, X, y, cv=cv, scoring='r2' if 'Regress' in name else 'f1_weighted')
	results[name] = scores
	print(f"{name} CV Scores: {scores}")
	print(f"Mean: {np.mean(scores):.4f}, Std: {np.std(scores):.4f}")

# 5. LEARNING/VALIDATION CURVES (example for one model)
# ...

# 6. VISUALIZATION
# ...

# 7. MODEL SELECTION
# ...
```

---

## 🆘 Resources
- Scikit-learn model selection guide
- Cross-validation and validation curve tutorials
- Course practicals 5-6 reference

**Deadline:** [Date]