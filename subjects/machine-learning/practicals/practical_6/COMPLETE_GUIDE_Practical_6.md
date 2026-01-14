# Practical 6: Clustering Algorithms - Complete Guide

## Learning Objectives

After completing this practical, you will:
1. Understand clustering concepts and unsupervised learning
2. Implement K-Means clustering algorithm
3. Apply Hierarchical clustering with dendrograms
4. Use DBSCAN for density-based clustering
5. Find optimal number of clusters
6. Calculate silhouette scores and evaluation metrics
7. Create clustering visualizations
8. Compare different clustering algorithms
9. Handle outliers in clustering
10. Select appropriate algorithms for different datasets

## Phase 0: Environment Setup

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.datasets import load_iris, make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from scipy.cluster.hierarchy import dendrogram, linkage
import warnings
warnings.filterwarnings('ignore')
```

## Phase 1: Data Preparation for Clustering

Clustering requires properly scaled data. Unlike supervised learning, there's no target variable.

```python
# Load iris dataset (150 samples, 4 features)
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

# Standardize features (CRITICAL for clustering)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f"Dataset shape: {X_scaled.shape}")
print(f"Mean of scaled data: {X_scaled.mean(axis=0)}")
print(f"Std of scaled data: {X_scaled.std(axis=0)}")
```

## Phase 2: K-Means Clustering

K-Means partitions data into K clusters by minimizing within-cluster variance.

**Algorithm:**
1. Initialize K centroids randomly
2. Assign each point to nearest centroid
3. Recalculate centroids as mean of cluster points
4. Repeat until convergence

```python
# Train K-Means with k=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_scaled)

# Get cluster centers
centroids = kmeans.cluster_centers_
inertia = kmeans.inertia_

print(f"Cluster labels: {np.unique(kmeans_labels)}")
print(f"Inertia: {inertia:.3f}")
print(f"Silhouette Score: {silhouette_score(X_scaled, kmeans_labels):.3f}")

# Visualize K-Means (first 2 features)
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=kmeans_labels, cmap='viridis', s=100, alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=300, edgecolors='black', linewidth=2)
plt.title('K-Means Clustering (k=3)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar()
plt.show()
```

## Phase 3: Optimal Number of Clusters - Elbow Method

Finding the right number of clusters is crucial.

```python
inertias = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

# Plot elbow curve
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].plot(K_range, inertias, 'bo-')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')
axes[0].grid()

axes[1].plot(K_range, silhouette_scores, 'go-')
axes[1].set_xlabel('Number of Clusters (k)')
axes[1].set_ylabel('Silhouette Score')
axes[1].set_title('Silhouette Score vs k')
axes[1].grid()

plt.tight_layout()
plt.show()

optimal_k = K_range[np.argmax(silhouette_scores)]
print(f"Optimal k (by silhouette): {optimal_k}")
```

## Phase 4: Hierarchical Clustering

Builds a tree of clusters (dendrogram) using bottom-up approach.

**Linkage methods:**
- Complete: max distance between clusters
- Average: mean distance
- Ward: minimizes variance

```python
# Perform hierarchical clustering
linkage_matrix = linkage(X_scaled, method='ward')

# Create dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_matrix, truncate_mode='lastp', p=12)
plt.title('Hierarchical Clustering Dendrogram (Ward Linkage)')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()

# Get cluster assignments at 3 clusters
hierarchical = AgglomerativeClustering(n_clusters=3, linkage='ward')
hier_labels = hierarchical.fit_predict(X_scaled)

print(f"Hierarchical silhouette score: {silhouette_score(X_scaled, hier_labels):.3f}")
print(f"Davies-Bouldin Index: {davies_bouldin_score(X_scaled, hier_labels):.3f}")

# Visualize
plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=hier_labels, cmap='plasma', s=100, alpha=0.6)
plt.title('Hierarchical Clustering (k=3, Ward)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar()
plt.show()
```

## Phase 5: DBSCAN - Density-Based Clustering

Groups points that are closely packed (high density).

**Parameters:**
- eps: Maximum distance between points
- min_samples: Minimum points to form a cluster
- Points are classified as core, border, or noise

```python
# DBSCAN clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_scaled)

n_clusters_dbscan = len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)
n_outliers = list(dbscan_labels).count(-1)

print(f"Number of clusters: {n_clusters_dbscan}")
print(f"Number of outliers: {n_outliers}")
print(f"Silhouette score: {silhouette_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1]):.3f}")

# Visualize DBSCAN
plt.figure(figsize=(8, 6))
colors = ['red' if label == -1 else label for label in dbscan_labels]
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=colors, cmap='viridis', s=100, alpha=0.6)
plt.title('DBSCAN Clustering (eps=0.5, min_samples=5)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```

## Phase 6: Algorithm Comparison

```python
algorithms = ['K-Means', 'Hierarchical', 'DBSCAN']
silhouette_list = [
    silhouette_score(X_scaled, kmeans_labels),
    silhouette_score(X_scaled, hier_labels),
    silhouette_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1])
]
davies_bouldin_list = [
    davies_bouldin_score(X_scaled, kmeans_labels),
    davies_bouldin_score(X_scaled, hier_labels),
    davies_bouldin_score(X_scaled[dbscan_labels != -1], dbscan_labels[dbscan_labels != -1])
]

# Create comparison dataframe
comparison_df = pd.DataFrame({
    'Algorithm': algorithms,
    'Silhouette Score': silhouette_list,
    'Davies-Bouldin Index': davies_bouldin_list
})

print("\nAlgorithm Comparison:")
print(comparison_df)

# Visualize
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].bar(algorithms, silhouette_list)
axes[0].set_ylabel('Silhouette Score (higher better)')
axes[0].set_title('Silhouette Score Comparison')
axes[0].set_ylim([0, 1])

axes[1].bar(algorithms, davies_bouldin_list)
axes[1].set_ylabel('Davies-Bouldin Index (lower better)')
axes[1].set_title('Davies-Bouldin Index Comparison')

plt.tight_layout()
plt.show()
```

## Phase 7: Advanced - Synthetic Dataset Testing

```python
# Generate synthetic data
X_synthetic, y_true = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)
X_synthetic_scaled = StandardScaler().fit_transform(X_synthetic)

# Apply all algorithms
kmeans_syn = KMeans(n_clusters=4, random_state=42, n_init=10)
hier_syn = AgglomerativeClustering(n_clusters=4, linkage='ward')
dbscan_syn = DBSCAN(eps=0.6, min_samples=5)

labels_km = kmeans_syn.fit_predict(X_synthetic_scaled)
labels_hier = hier_syn.fit_predict(X_synthetic_scaled)
labels_db = dbscan_syn.fit_predict(X_synthetic_scaled)

# Visualize all three
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].scatter(X_synthetic_scaled[:, 0], X_synthetic_scaled[:, 1], c=labels_km, cmap='viridis')
axes[0].set_title('K-Means')

axes[1].scatter(X_synthetic_scaled[:, 0], X_synthetic_scaled[:, 1], c=labels_hier, cmap='plasma')
axes[1].set_title('Hierarchical')

colors = ['red' if label == -1 else label for label in labels_db]
axes[2].scatter(X_synthetic_scaled[:, 0], X_synthetic_scaled[:, 1], c=colors)
axes[2].set_title('DBSCAN')

plt.tight_layout()
plt.show()
```

## Phase 8: Testing and Validation

See Practical_6_Complete_Notebook.ipynb for 5 complete tests.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Poor clustering | Check scaling, try different k, adjust eps for DBSCAN |
| Outliers disturbing results | Use DBSCAN, or remove outliers before K-Means |
| Dendrogram too complex | Use truncate_mode in dendrogram() |
| Inconsistent results | Set random_state for reproducibility, increase n_init |

## Key Concepts

- **Silhouette Score:** Measures cluster separation (-1 to 1, higher better)
- **Davies-Bouldin Index:** Ratio of within-cluster to between-cluster distances (lower better)
- **Inertia:** Sum of squared distances from points to centroids (for K-Means)
- **Dendrogram:** Tree showing hierarchical relationships
- **Core Points, Border Points, Noise:** DBSCAN classification types

## Algorithm Selection Guide

| Scenario | Best Algorithm |
|----------|----------------|
| Spherical, similar-sized clusters | K-Means |
| Arbitrary shapes and sizes | Hierarchical, DBSCAN |
| Unknown number of clusters | Hierarchical (dendrogram) or Elbow method |
| Outliers present | DBSCAN |
| Large dataset | K-Means |
| Dendrograms needed | Hierarchical |

---

**Status:** Complete | **Next:** Practical 7 - Dimensionality Reduction
