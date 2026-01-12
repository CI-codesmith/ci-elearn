
# MICROPROJECT 2.5: Hyperparameter Optimization

**Course:** 316316 - Machine Learning  
**Unit:** 2 (Supervised Learning)  
**Group Size:** 3 students  
**Duration:** 1.5 weeks  
**Weight:** 10% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Data preparation and pipeline setup
- **ML Engineer:** Hyperparameter search and model tuning
- **Analyst:** Results analysis and reporting

---

## 🎯 Objective
Apply and compare different hyperparameter optimization techniques to improve supervised learning model performance. Demonstrate the impact of tuning on model accuracy and generalization.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **California Housing** (regression)
- **Titanic Survival** (classification)
- **Auto MPG** (regression)

### Technical Requirements
- Implement at least **2 models** (regression/classification)
- Use **Grid Search** and **Randomized Search** for hyperparameter tuning
- Optionally, try **Bayesian Optimization** (e.g., with scikit-optimize or optuna)
- Compare default vs tuned model performance
- Visualize search results (heatmaps, score plots)

### Model Requirements
1. **Baseline Model** (default hyperparameters)
2. **Hyperparameter Search** (GridSearchCV, RandomizedSearchCV)
3. **Tuned Model** (best parameters)
4. **Performance Comparison** (metrics, visualizations)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP2_5_Group[ID]_HyperparameterTuning.ipynb`
- **Sections:** Baseline → Tuning → Tuned model → Comparison

### 2. Tuning Report (20% weight)
- **File:** `MP2_5_Group[ID]_Report.pdf`
- **Content:** Search space, best parameters, impact analysis

### 3. Visualizations (15% weight)
- **File:** `MP2_5_Group[ID]_Visualizations.pdf`
- **Content:** Heatmaps, score plots, before/after comparisons

### 4. Presentation (15% weight)
- **File:** `MP2_5_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Hyperparameter Search** | Grid & random, well-justified | Good search | Basic search | Poor/none |
| **Model Performance** | Significant improvement | Good improvement | Minor | No improvement |
| **Visualization** | Excellent plots, clear impact | Good plots | Basic plots | Poor quality |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /30 per group

---

## 📝 Template Code

```python
# MICROPROJECT 2.5: Hyperparameter Optimization
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LinearRegression, Ridge, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. BASELINE MODEL
# ...

# 3. GRID SEARCH
# param_grid = {...}
# grid = GridSearchCV(...)
# grid.fit(...)

# 4. RANDOMIZED SEARCH
# param_dist = {...}
# rand = RandomizedSearchCV(...)
# rand.fit(...)

# 5. PERFORMANCE COMPARISON
# ...
```

---

## 🆘 Resources
- Scikit-learn hyperparameter tuning guide
- Optuna, scikit-optimize (optional)
- Course practicals 7 reference

**Deadline:** [Date]