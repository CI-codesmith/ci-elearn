# Practical 7: Dimensionality Reduction - Complete Guide

## Learning Objectives
1. Understand curse of dimensionality
2. Apply PCA (Principal Component Analysis)
3. Calculate explained variance ratio
4. Reduce features to optimal dimensions
5. Feature selection techniques (SelectKBest, Random Forest)
6. Visualize high-dimensional data with t-SNE
7. Create scree plots and loadings analysis
8. Compare PCA vs Feature Selection
9. Handle different data distributions
10. Select appropriate reduction method for datasets

## Phase 0: Environment Setup
```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Phase 1: Understanding Dimensionality

Curse of Dimensionality: As dimensions increase, data becomes sparse, making patterns harder to find. Solution: Reduce dimensions while preserving information.

## Phase 2: PCA Fundamentals

PCA finds principal components (new features) that capture maximum variance:
- Component 1: Direction of maximum variance
- Component 2: Orthogonal direction, second-highest variance
- And so on...

```python
iris = load_iris()
X = iris.data
X_scaled = StandardScaler().fit_transform(X)
pca = PCA()
pca.fit(X_scaled)
print(f"Explained variance: {pca.explained_variance_ratio_}")
```

## Phase 3: Selecting Number of Components

Use elbow method or 95% variance threshold:
```python
cumsum = np.cumsum(pca.explained_variance_ratio_)
n_components = np.argmax(cumsum >= 0.95) + 1
```

## Phase 4: Feature Selection

SelectKBest ranks features by statistical score (F-test):
```python
selector = SelectKBest(f_classif, k=2)
X_selected = selector.fit_transform(X_scaled, y)
```

## Phase 5: Tree-Based Feature Importance

Random Forest provides non-linear feature relationships:
```python
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X, y)
importances = rf.feature_importances_
```

## Phase 6: t-SNE Visualization

t-SNE creates 2D/3D visualizations for non-linear data:
```python
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_scaled)
```

## Phase 7: Comparison

| Method | Pros | Cons |
|--------|------|------|
| PCA | Fast, linear, interpretable | Only linear relationships |
| Feature Selection | Uses original features | May miss interactions |
| t-SNE | Excellent visualization | Non-deterministic, slow |

## Phase 8: Testing

See Practical_7_Complete_Notebook.ipynb for 5 complete tests.

---
**Status:** Complete
