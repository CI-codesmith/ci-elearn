
# MICROPROJECT 3.2: Dimensionality Reduction

**Course:** 316316 - Machine Learning  
**Unit:** 3 (Unsupervised Learning)  
**Group Size:** 3 students  
**Duration:** 1.5 weeks  
**Weight:** 10% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Data preprocessing and feature scaling
- **ML Engineer:** Dimensionality reduction implementation and analysis
- **Analyst:** Visualization and interpretation of results

---

## 🎯 Objective
Apply and compare dimensionality reduction techniques (PCA, t-SNE) on high-dimensional datasets. Visualize and interpret the reduced feature space for clustering or classification tasks.

---

## 📋 Requirements

### Dataset Selection
Choose **one** high-dimensional dataset:
- **Digits** (classification)
- **Wine** (classification)
- **MNIST** (optional, for advanced)

### Technical Requirements
- Implement **Principal Component Analysis (PCA)**
- Implement **t-distributed Stochastic Neighbor Embedding (t-SNE)**
- Visualize 2D/3D projections (scatter plots, color by class/cluster)
- Compare explained variance (PCA) and cluster separation (t-SNE)
- Use reduced features for clustering or classification

### Model Requirements
1. **Data Preprocessing** (scaling, encoding)
2. **Dimensionality Reduction** (PCA, t-SNE)
3. **Visualization** (scatter plots, explained variance)
4. **Downstream Task** (clustering/classification with reduced features)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP3_2_Group[ID]_DimReduction.ipynb`
- **Sections:** Preprocessing → Dimensionality reduction → Visualization → Downstream task

### 2. Analysis Report (20% weight)
- **File:** `MP3_2_Group[ID]_Report.pdf`
- **Content:** Method comparison, interpretation, impact on downstream task

### 3. Visualizations (15% weight)
- **File:** `MP3_2_Group[ID]_Visualizations.pdf`
- **Content:** 2D/3D plots, explained variance, cluster separation

### 4. Presentation (15% weight)
- **File:** `MP3_2_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Proper scaling, encoding | Good preprocessing | Basic | Poor/none |
| **PCA Implementation** | Correct, explained, visualized | Good PCA | Basic | Poor/none |
| **t-SNE Implementation** | Correct, visualized, interpreted | Good t-SNE | Basic | Poor/none |
| **Visualization** | Excellent, clear, insightful | Good plots | Basic plots | Poor quality |
| **Downstream Task** | Improved/maintained performance | Good performance | Basic | Poor |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 3.2: Dimensionality Reduction
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('your_dataset.csv')

# 2. PREPROCESSING
# ...

# 3. PCA
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X_scaled)

# 4. t-SNE
# tsne = TSNE(n_components=2, random_state=42)
# X_tsne = tsne.fit_transform(X_scaled)

# 5. VISUALIZATION
# ...

# 6. CLUSTERING/CLASSIFICATION
# ...
```

---

## 🆘 Resources
- Scikit-learn PCA and t-SNE guides
- Visualization tutorials (matplotlib, seaborn)
- Course practicals 8 reference

**Deadline:** [Date]