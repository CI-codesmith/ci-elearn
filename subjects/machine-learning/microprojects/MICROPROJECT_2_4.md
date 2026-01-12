
# MICROPROJECT 2.4: Feature Engineering

**Course:** 316316 - Machine Learning  
**Unit:** 2 (Supervised Learning)  
**Group Size:** 3 students  
**Duration:** 1.5 weeks  
**Weight:** 10% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Feature creation, transformation, and selection
- **ML Engineer:** Model implementation and evaluation
- **Analyst:** Feature impact analysis and reporting

---

## 🎯 Objective
Explore, create, and evaluate new features to improve model performance. Demonstrate the impact of feature engineering on supervised learning tasks.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **California Housing** (regression)
- **Titanic Survival** (classification)
- **Auto MPG** (regression)

### Technical Requirements
- Perform **feature creation** (polynomial, interaction, domain-specific)
- Apply **feature transformation** (scaling, encoding, binning)
- Use **feature selection** techniques (filter, wrapper, embedded)
- Compare model performance before and after feature engineering
- Visualize feature importances and effects

### Model Requirements
1. **Baseline Model** (minimal preprocessing)
2. **Feature Engineering** (create/transform/select features)
3. **Enhanced Model** (train and evaluate)
4. **Performance Comparison** (metrics, visualizations)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP2_4_Group[ID]_FeatureEngineering.ipynb`
- **Sections:** Baseline → Feature engineering → Enhanced model → Comparison

### 2. Feature Engineering Report (20% weight)
- **File:** `MP2_4_Group[ID]_Report.pdf`
- **Content:** Feature creation/selection process, impact analysis

### 3. Visualizations (15% weight)
- **File:** `MP2_4_Group[ID]_Visualizations.pdf`
- **Content:** Feature importances, before/after comparisons

### 4. Presentation (15% weight)
- **File:** `MP2_4_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Feature Creation** | Multiple, relevant, creative | Good features | Basic features | Few/irrelevant |
| **Feature Transformation** | Proper scaling/encoding | Good transformation | Basic | Poor/none |
| **Feature Selection** | Robust, justified | Good selection | Basic | Poor/none |
| **Model Performance** | Significant improvement | Good improvement | Minor | No improvement |
| **Visualization** | Excellent plots, clear impact | Good plots | Basic plots | Poor quality |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 2.4: Feature Engineering
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures, OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_regression, f_classif
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. BASELINE MODEL
# ...

# 3. FEATURE ENGINEERING
# Polynomial features, interaction terms, encoding, scaling

# 4. FEATURE SELECTION
# selector = SelectKBest(score_func=f_regression or f_classif, k=5)
# X_new = selector.fit_transform(X, y)

# 5. ENHANCED MODEL
# ...

# 6. PERFORMANCE COMPARISON
# ...
```

---

## 🆘 Resources
- Feature engineering guides (Kaggle, scikit-learn)
- Course practicals 6 reference

**Deadline:** [Date]