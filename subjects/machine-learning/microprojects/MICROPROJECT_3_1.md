# MICROPROJECT 3.1: Pattern Discovery Project

**Course:** 316316 - Machine Learning  
**Unit:** 3 (Unsupervised Learning)  
**Duration:** 1.5 weeks  
**Submission:** Jupyter Notebook + Visualizations + Report  
**Weight:** 15% of unit assessment

---

## 🎯 Objective
Apply unsupervised learning techniques to discover hidden patterns in data. Students will implement clustering and dimensionality reduction to gain insights from unlabeled data.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **Customer Segmentation** (Mall customers data)
- **Iris** (for clustering validation)
- **Wholesale customers** (business data)
- **Any unlabeled dataset** with ≥4 features, ≥200 samples

### Technical Requirements
- **Algorithms to implement:**
  - Clustering: K-Means, Hierarchical Clustering
  - Dimensionality Reduction: PCA, t-SNE
- **Evaluation:** Silhouette score, elbow method for K-Means
- **Visualization:** 2D/3D plots of clusters, explained variance plots

### Analysis Requirements
1. **Data Preprocessing** (scaling, outlier removal)
2. **Clustering Implementation** (compare algorithms)
3. **Dimensionality Reduction** (visualize high-dimensional data)
4. **Pattern Interpretation** (what do clusters represent?)
5. **Optimal Parameter Selection** (justify choices)

---

## 📤 Deliverables

### 1. Jupyter Notebook (75% weight)
- **File:** `MP3_1_[Name]_[Dataset].ipynb`
- **Include:** All code, visualizations, interpretations

### 2. Visualizations Folder (10% weight)
- **Files:** Exported plots (PNG/PDF)
- **Naming:** `cluster_plot.png`, `pca_variance.png`, etc.

### 3. PDF Report (15% weight)
- **File:** `MP3_1_[Name]_Report.pdf`
- **Content:** Methodology, results, business insights

---

## 📊 Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Thorough data prep, handles all issues | Good preprocessing | Basic cleaning | Inadequate |
| **Clustering** | Multiple algorithms, optimal K selection | 2+ algorithms | 1 algorithm | Poor implementation |
| **Dimensionality Reduction** | Proper implementation, good visualizations | Basic PCA/t-SNE | Minimal | Incorrect |
| **Evaluation** | Comprehensive metrics, interpretation | Good metrics | Basic evaluation | No evaluation |
| **Insights** | Deep pattern analysis, actionable insights | Good interpretation | Basic findings | No insights |
| **Visualization** | Excellent plots, well-labeled | Good plots | Basic plots | Poor quality |

**Total:** /30

**Grade Scale:** 24-30:A, 18-23:B, 12-17:C, <12:F

---

## 📝 Template Code

```python
# MICROPROJECT 3.1: Pattern Discovery
# Student: [Name]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. DATA LOADING & PREPROCESSING
# df = pd.read_csv('dataset.csv')
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(df)

# 2. OPTIMAL K SELECTION (ELBOW METHOD)
# wcss = []
# for k in range(1, 11):
#     kmeans = KMeans(n_clusters=k, random_state=42)
#     kmeans.fit(X_scaled)
#     wcss.append(kmeans.inertia_)

# plt.plot(range(1, 11), wcss)
# plt.title('Elbow Method')
# plt.show()

# 3. K-MEANS CLUSTERING
# kmeans = KMeans(n_clusters=optimal_k, random_state=42)
# clusters = kmeans.fit_predict(X_scaled)

# 4. DIMENSIONALITY REDUCTION
# pca = PCA(n_components=2)
# X_pca = pca.fit_transform(X_scaled)

# 5. VISUALIZATION
# plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis')
# plt.title('Clusters (PCA)')
# plt.show()

# 6. EVALUATION
# silhouette_avg = silhouette_score(X_scaled, clusters)
# print(f"Silhouette Score: {silhouette_avg}")
```

---

## 🆘 Resources
- Scikit-learn clustering guide
- Practical 6 reference
- Kaggle clustering tutorials

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_3_1.md