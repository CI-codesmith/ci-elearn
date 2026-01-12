
# MICROPROJECT 4.4: Ensemble Methods

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Advanced Topics)  
**Group Size:** 3 students  
**Duration:** 2 weeks  
**Weight:** 12% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Data preparation and feature engineering
- **ML Engineer:** Ensemble model implementation and tuning
- **Analyst:** Evaluation, visualization, and reporting

---

## 🎯 Objective
Implement and compare ensemble learning methods (Bagging, Boosting) for classification or regression. Analyze the impact of ensembling on model performance and robustness.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **California Housing** (regression)
- **Titanic Survival** (classification)
- **MNIST** (classification)

### Technical Requirements
- Implement at least **2 ensemble methods:**
	- Bagging (Random Forest, BaggingClassifier)
	- Boosting (AdaBoost, GradientBoosting, XGBoost)
- Compare with baseline (single model)
- Evaluate with metrics: accuracy, RMSE, F1-score, ROC-AUC
- Visualize feature importances and ensemble effects

### Model Requirements
1. **Data Preprocessing** (scaling, encoding)
2. **Model Training** (ensemble and baseline)
3. **Evaluation** (metrics, visualizations)
4. **Analysis** (ensemble vs single model)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP4_4_Group[ID]_Ensemble.ipynb`
- **Sections:** Preprocessing → Modeling → Evaluation → Analysis

### 2. Model Report (20% weight)
- **File:** `MP4_4_Group[ID]_Report.pdf`
- **Content:** Method comparison, results, analysis

### 3. Visualizations (15% weight)
- **File:** `MP4_4_Group[ID]_Visualizations.pdf`
- **Content:** Feature importances, ensemble effects

### 4. Presentation (15% weight)
- **File:** `MP4_4_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Proper scaling, encoding | Good preprocessing | Basic | Poor/none |
| **Ensemble Implementation** | 2+ methods, correct, justified | Good implementation | Basic | Poor/none |
| **Evaluation** | Comprehensive, correct metrics | Good metrics | Basic metrics | Incorrect/none |
| **Visualization** | Excellent, clear, insightful | Good plots | Basic plots | Poor quality |
| **Analysis** | Insightful, ensemble impact | Good analysis | Basic | Poor/none |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 4.4: Ensemble Methods
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. PREPROCESSING
# ...

# 3. BASELINE MODEL
# ...

# 4. ENSEMBLE METHODS
# ...

# 5. EVALUATION
# ...

# 6. VISUALIZATION
# ...
```

---

## 🆘 Resources
- Scikit-learn ensemble methods guide
- XGBoost documentation (optional)
- Course practicals 12 reference

**Deadline:** [Date]