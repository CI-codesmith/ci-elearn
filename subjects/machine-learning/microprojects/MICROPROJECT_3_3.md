
# MICROPROJECT 3.3: Anomaly Detection

**Course:** 316316 - Machine Learning  
**Unit:** 3 (Unsupervised Learning)  
**Group Size:** 3 students  
**Duration:** 1.5 weeks  
**Weight:** 10% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Data preprocessing and outlier analysis
- **ML Engineer:** Anomaly detection model implementation
- **Analyst:** Evaluation and visualization of anomalies

---

## 🎯 Objective
Implement and compare anomaly detection algorithms on real-world datasets. Visualize and interpret detected anomalies, and evaluate model effectiveness.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **Credit Card Fraud** (binary anomaly)
- **KDD Cup 1999** (network intrusion)
- **Synthetic dataset** (optional)

### Technical Requirements
- Implement at least **2 algorithms:**
	- Isolation Forest
	- One-Class SVM
	- (Optional) Local Outlier Factor
- Visualize detected anomalies (scatter plots, time series, etc.)
- Evaluate with metrics: Precision, Recall, F1-score (for labeled data), or silhouette score (for unsupervised)
- Compare model performance and discuss use cases

### Model Requirements
1. **Data Preprocessing** (scaling, encoding, handling imbalance)
2. **Model Training** (fit anomaly detectors)
3. **Evaluation** (metrics, visualizations)
4. **Comparison & Interpretation**

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP3_3_Group[ID]_AnomalyDetection.ipynb`
- **Sections:** Preprocessing → Modeling → Evaluation → Interpretation

### 2. Analysis Report (20% weight)
- **File:** `MP3_3_Group[ID]_Report.pdf`
- **Content:** Method comparison, anomaly interpretation

### 3. Visualizations (15% weight)
- **File:** `MP3_3_Group[ID]_Visualizations.pdf`
- **Content:** Anomaly plots, metric comparisons

### 4. Presentation (15% weight)
- **File:** `MP3_3_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Proper scaling, encoding | Good preprocessing | Basic | Poor/none |
| **Algorithm Implementation** | 2+ methods, correct, justified | Good implementation | Basic | Poor/none |
| **Evaluation** | Comprehensive, correct metrics | Good metrics | Basic metrics | Incorrect/none |
| **Visualization** | Excellent, clear, insightful | Good plots | Basic plots | Poor quality |
| **Interpretation** | Clear, insightful, actionable | Good interpretation | Basic | Poor/none |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 3.3: Anomaly Detection
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.neighbors import LocalOutlierFactor
from sklearn.metrics import precision_score, recall_score, f1_score, silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. PREPROCESSING
# ...

# 3. ISOLATION FOREST
# iso = IsolationForest(contamination=0.01, random_state=42)
# y_pred_iso = iso.fit_predict(X_scaled)

# 4. ONE-CLASS SVM
# svm = OneClassSVM(nu=0.01, kernel='rbf', gamma=0.1)
# y_pred_svm = svm.fit_predict(X_scaled)

# 5. VISUALIZATION
# ...

# 6. EVALUATION
# ...
```

---

## 🆘 Resources
- Scikit-learn anomaly detection guide
- Visualization tutorials (matplotlib, seaborn)
- Course practicals 9 reference

**Deadline:** [Date]