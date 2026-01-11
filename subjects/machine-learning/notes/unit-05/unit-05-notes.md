---
**MindforgeAi Publications**

**Technical Publication Series**

**Chatake Innoworks Pvt. Ltd.**

**Copyright © 2025 Chatake Innoworks Pvt. Ltd.**

**Authored by: Akash Chatake**
---
# UNIT V: UNSUPERVISED LEARNING ALGORITHMS - COMPLETE DIPLOMA NOTES

## MSBTE K-Scheme Syllabus (Course Code: 316316, Semester 6)

## Machine Learning - Detailed Theory Notes for Diploma Students

---

## Table of Contents

1. [Introduction to Unsupervised Learning](#introduction-to-unsupervised-learning)
2. [K-Means Clustering](#k-means-clustering)
   - 2.1 [How K-Means Works](#how-k-means-works)
   - 2.2 [Algorithm Steps](#algorithm-steps)
   - 2.3 [Choosing K Value](#choosing-k-value)
   - 2.4 [Python Implementation](#python-implementation-k-means)
3. [Hierarchical Clustering](#hierarchical-clustering)
   - 3.1 [Agglomerative Clustering](#agglomerative-clustering)
   - 3.2 [Divisive Clustering](#divisive-clustering)
   - 3.3 [Linkage Methods](#linkage-methods)
   - 3.4 [Dendrogram](#dendrogram)
   - 3.5 [Python Implementation](#python-implementation-hierarchical)
4. [Clustering Evaluation Metrics](#clustering-evaluation-metrics)
   - 4.1 [Internal Metrics](#internal-metrics)
   - 4.2 [External Metrics](#external-metrics)
   - 4.3 [Silhouette Analysis](#silhouette-analysis)
5. [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
   - 5.1 [Mathematical Foundation](#mathematical-foundation)
   - 5.2 [Implementation Steps](#implementation-steps)
   - 5.3 [Python Implementation](#python-implementation-pca)
6. [Ethics in Machine Learning](#ethics-in-machine-learning)
   - 6.1 [Bias and Fairness](#bias-and-fairness)
   - 6.2 [Privacy and Data Protection](#privacy-and-data-protection)
   - 6.3 [Transparency and Explainability](#transparency-and-explainability)
   - 6.4 [Accountability](#accountability)
7. [Model Deployment and Production](#model-deployment-and-production)
   - 7.1 [Model Serialization](#model-serialization)
   - 7.2 [APIs and Web Services](#apis-and-web-services)
   - 7.3 [Monitoring and Maintenance](#monitoring-and-maintenance)
   - 7.4 [Python Implementation](#python-implementation-deployment)
8. [Real-World Applications](#real-world-applications)
9. [Terminal Learning Objectives (TLOs) Mapping](#terminal-learning-objectives-tlos-mapping)
10. [Exam Questions and Practice](#exam-questions-and-practice)
11. [Summary](#summary)

---

## 1. Introduction to Unsupervised Learning

Unsupervised learning is a type of machine learning where algorithms learn patterns from unlabeled data without human supervision.

### Key Characteristics

- **No labeled data**: No target variable to predict
- **Pattern discovery**: Find hidden structures in data
- **Exploratory analysis**: Understand data distribution
- **Dimensionality reduction**: Reduce feature space

### Types of Unsupervised Learning

1. **Clustering**: Group similar data points together

   - K-Means clustering
   - Hierarchical clustering
   - DBSCAN
2. **Dimensionality Reduction**: Reduce number of features

   - Principal Component Analysis (PCA)
   - t-SNE
   - Autoencoders
3. **Association Rule Mining**: Find relationships between variables

   - Apriori algorithm
   - FP-Growth

### Applications

- Customer segmentation
- Anomaly detection
- Recommendation systems
- Image compression
- Topic modeling

### Flowchart

```
Unsupervised Learning
         ↓
Data Collection
         ↓
Data Preprocessing
         ↓
Choose Algorithm
    ├── Clustering
    │   ├── K-Means
    │   └── Hierarchical
    └── Dimensionality Reduction
        ├── PCA
        └── Others
         ↓
Model Training
         ↓
Evaluation & Interpretation
```

---

\newpage

## 2. K-Means Clustering

K-Means is one of the most popular clustering algorithms that partitions data into K clusters based on similarity.

### 2.1 How K-Means Works

K-Means aims to minimize the within-cluster sum of squares (WCSS), also known as inertia.

#### Objective Function

```
Minimize: Σ Σ ||x_i - μ_j||²
```

Where:

- x_i: data points
- μ_j: cluster centroids
- K: number of clusters

### 2.2 Algorithm Steps

1. **Initialize centroids**: Choose K random points as initial centroids
2. **Assign clusters**: Assign each data point to nearest centroid
3. **Update centroids**: Calculate new centroids as mean of points in cluster
4. **Repeat**: Steps 2-3 until convergence or max iterations
5. **Convergence**: When centroids don't change or change is minimal

### Algorithm Flowchart

```
Start
    ↓
Choose K
    ↓
Initialize K centroids randomly
    ↓
Repeat until convergence:
    ├── Assign each point to nearest centroid
    ├── Update centroids as cluster means
    ↓
End (Clusters formed)
```

### 2.3 Choosing K Value

#### Elbow Method

- Plot WCSS vs K
- Look for "elbow" point where WCSS decreases slowly
- Choose K at the elbow

#### Silhouette Analysis

- Measure how similar points are to their cluster vs other clusters
- Values range from -1 to +1
- Higher values indicate better clustering

#### Gap Statistics

- Compare within-cluster dispersion to reference distribution
- Choose K where gap statistic is maximum

### 2.4 Python Implementation

#### Example 1: Basic K-Means Clustering

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# Apply K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap='viridis', alpha=0.6)
plt.title('True Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, cmap='viridis', alpha=0.6)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
           s=300, c='red', marker='X', label='Centroids')
plt.title('K-Means Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

plt.tight_layout()
plt.show()

print("Cluster centers:")
print(kmeans.cluster_centers_)
print("Inertia (WCSS):", kmeans.inertia_)
```

#### Example 2: Elbow Method for Choosing K

```python
# Calculate WCSS for different K values
wcss = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-Cluster Sum of Squares)')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.show()

# Find optimal K (elbow point)
# In this case, K=4 is optimal based on the elbow
optimal_k = 4
print(f"Optimal number of clusters: {optimal_k}")
```

#### Example 3: Silhouette Analysis

```python
from sklearn.metrics import silhouette_score, silhouette_samples
import matplotlib.cm as cm

# Calculate silhouette scores for different K
silhouette_scores = []
k_range = range(2, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X)
    silhouette_avg = silhouette_score(X, cluster_labels)
    silhouette_scores.append(silhouette_avg)
    print(f"K={k}: Silhouette Score = {silhouette_avg:.3f}")

# Plot silhouette scores
plt.figure(figsize=(8, 5))
plt.plot(k_range, silhouette_scores, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Analysis for Optimal K')
plt.grid(True)
plt.show()

# Detailed silhouette plot for optimal K
k_optimal = k_range[np.argmax(silhouette_scores)]
kmeans_optimal = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
cluster_labels = kmeans_optimal.fit_predict(X)

# Compute silhouette scores for each sample
sample_silhouette_values = silhouette_samples(X, cluster_labels)

plt.figure(figsize=(10, 7))
y_lower = 10
for i in range(k_optimal):
    ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
    ith_cluster_silhouette_values.sort()
  
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
  
    color = cm.nipy_spectral(float(i) / k_optimal)
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values,
                     facecolor=color, edgecolor=color, alpha=0.7)
  
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10

plt.axvline(x=silhouette_score(X, cluster_labels), color="red", linestyle="--")
plt.xlabel("Silhouette coefficient values")
plt.ylabel("Cluster label")
plt.title("Silhouette plot for clusters")
plt.show()
```

#### Example 4: Manual K-Means Implementation

```python
def manual_kmeans(X, k, max_iters=100, tol=1e-4):
    # Randomly initialize centroids
    np.random.seed(42)
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]
  
    for iteration in range(max_iters):
        # Assign points to nearest centroid
        distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
        labels = np.argmin(distances, axis=0)
      
        # Update centroids
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])
      
        # Check for convergence
        if np.all(np.abs(new_centroids - centroids) < tol):
            break
          
        centroids = new_centroids
  
    # Calculate WCSS
    wcss = 0
    for i in range(k):
        cluster_points = X[labels == i]
        wcss += np.sum((cluster_points - centroids[i])**2)
  
    return labels, centroids, wcss

# Test manual implementation
labels_manual, centroids_manual, wcss_manual = manual_kmeans(X, 4)
print("Manual K-Means WCSS:", wcss_manual)
print("Manual centroids:")
print(centroids_manual)
```

---

\newpage

## 3. Hierarchical Clustering

Hierarchical clustering builds a hierarchy of clusters by either merging smaller clusters or splitting larger ones.

### 3.1 Agglomerative Clustering

**Bottom-up approach**: Start with individual points as clusters, merge them iteratively.

#### Steps

1. Treat each data point as a single cluster
2. Find closest pair of clusters
3. Merge them into one cluster
4. Repeat until desired number of clusters reached

### 3.2 Divisive Clustering

**Top-down approach**: Start with all points in one cluster, split them iteratively.

#### Steps

1. Start with all data points in one cluster
2. Find cluster to split
3. Split it into two clusters
4. Repeat until desired number of clusters reached

### 3.3 Linkage Methods

#### Single Linkage (Minimum)

- Distance between closest points of clusters
- Tends to create long, chain-like clusters

#### Complete Linkage (Maximum)

- Distance between farthest points of clusters
- Creates compact, spherical clusters

#### Average Linkage

- Average distance between all pairs of points
- Balance between single and complete linkage

#### Centroid Linkage

- Distance between cluster centroids
- Can be used with any distance metric

#### Ward's Method

- Minimizes within-cluster variance
- Similar to K-Means objective

### Comparison Table

| Linkage Method | Advantages                     | Disadvantages               | Best For           |
| -------------- | ------------------------------ | --------------------------- | ------------------ |
| Single         | Handles non-spherical clusters | Sensitive to noise          | Elongated clusters |
| Complete       | Compact clusters               | Sensitive to outliers       | Spherical clusters |
| Average        | Balanced approach              | Moderate performance        | General purpose    |
| Ward           | Similar to K-Means             | Requires Euclidean distance | Spherical clusters |

### 3.4 Dendrogram

A dendrogram is a tree-like diagram showing hierarchical relationships between clusters.

#### Reading a Dendrogram

- Height of merge indicates similarity
- Cutting horizontal line gives clusters
- Y-axis shows distance/similarity measure

### 3.5 Python Implementation

#### Example 1: Agglomerative Clustering

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Generate sample data
X, y_true = make_blobs(n_samples=150, centers=3, cluster_std=0.60, random_state=42)

# Apply hierarchical clustering
hierarchical = AgglomerativeClustering(n_clusters=3, linkage='ward')
y_hierarchical = hierarchical.fit_predict(X)

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y_true, cmap='viridis', alpha=0.6)
plt.title('True Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=y_hierarchical, cmap='viridis', alpha=0.6)
plt.title('Hierarchical Clusters')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()
```

#### Example 2: Creating Dendrogram

```python
# Create linkage matrix
linkage_matrix = linkage(X, method='ward')

# Plot dendrogram
plt.figure(figsize=(12, 8))
dendrogram(linkage_matrix, truncate_mode='level', p=5)
plt.xlabel('Sample index or cluster size')
plt.ylabel('Distance')
plt.title('Hierarchical Clustering Dendrogram')
plt.show()

# Different linkage methods comparison
methods = ['single', 'complete', 'average', 'ward']
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

for i, method in enumerate(methods):
    linkage_matrix = linkage(X, method=method)
    axes[i//2, i%2].set_title(f'Dendrogram - {method.capitalize()} Linkage')
    dendrogram(linkage_matrix, ax=axes[i//2, i%2], truncate_mode='level', p=3)
    axes[i//2, i%2].set_xlabel('Sample index')
    axes[i//2, i%2].set_ylabel('Distance')

plt.tight_layout()
plt.show()
```

#### Example 3: Comparing Linkage Methods

```python
# Compare different linkage methods
linkage_methods = ['single', 'complete', 'average', 'ward']
silhouette_scores = []

for method in linkage_methods:
    hierarchical = AgglomerativeClustering(n_clusters=3, linkage=method)
    labels = hierarchical.fit_predict(X)
    score = silhouette_score(X, labels)
    silhouette_scores.append(score)
    print(f"{method.capitalize()} Linkage: Silhouette Score = {score:.3f}")

# Plot comparison
plt.figure(figsize=(8, 5))
plt.bar(linkage_methods, silhouette_scores)
plt.xlabel('Linkage Method')
plt.ylabel('Silhouette Score')
plt.title('Comparison of Linkage Methods')
plt.show()
```

#### Example 4: Manual Hierarchical Clustering (Simplified)

```python
from scipy.spatial.distance import pdist, squareform

def manual_single_linkage(X, k):
    # Calculate distance matrix
    distance_matrix = squareform(pdist(X, metric='euclidean'))
  
    # Initialize clusters
    clusters = [[i] for i in range(len(X))]
  
    while len(clusters) > k:
        # Find minimum distance between clusters
        min_distance = float('inf')
        merge_i, merge_j = -1, -1
      
        for i in range(len(clusters)):
            for j in range(i+1, len(clusters)):
                # Single linkage: minimum distance between any points
                cluster_distances = []
                for point_i in clusters[i]:
                    for point_j in clusters[j]:
                        cluster_distances.append(distance_matrix[point_i, point_j])
                distance = min(cluster_distances)
              
                if distance < min_distance:
                    min_distance = distance
                    merge_i, merge_j = i, j
      
        # Merge clusters
        clusters[merge_i].extend(clusters[merge_j])
        del clusters[merge_j]
  
    # Convert to labels
    labels = np.zeros(len(X), dtype=int)
    for cluster_id, cluster in enumerate(clusters):
        for point in cluster:
            labels[point] = cluster_id
  
    return labels

# Test manual implementation
labels_manual = manual_single_linkage(X[:20], 3)  # Use subset for speed
print("Manual hierarchical clustering labels:", labels_manual)
```

---

## 4. Clustering Evaluation Metrics

### 4.1 Internal Metrics

#### Within-Cluster Sum of Squares (WCSS/Inertia)

```
WCSS = Σ Σ ||x_i - μ_j||²
```

- Measures compactness of clusters
- Lower values indicate better clustering
- Used in elbow method

#### Between-Cluster Sum of Squares (BCSS)

```
BCSS = Σ n_j ||μ_j - μ||²
```

- Measures separation between clusters
- Higher values indicate better clustering

#### Calinski-Harabasz Index

```
CH = (BCSS / (k-1)) / (WCSS / (n-k))
```

- Ratio of between-cluster to within-cluster dispersion
- Higher values indicate better clustering

### 4.2 External Metrics

#### Adjusted Rand Index (ARI)

- Measures similarity between true and predicted clusters
- Values range from -1 to 1
- 1 indicates perfect agreement

#### Adjusted Mutual Information (AMI)

- Measures agreement between true and predicted clusters
- Adjusted for chance
- Values range from 0 to 1

#### Homogeneity and Completeness

- **Homogeneity**: Each cluster contains only members of one class
- **Completeness**: All members of a class are in the same cluster
- **V-measure**: Harmonic mean of homogeneity and completeness

### 4.3 Silhouette Analysis

#### Silhouette Coefficient for a point

```
s(i) = (b(i) - a(i)) / max(a(i), b(i))
```

Where:

- a(i): Average distance to other points in same cluster
- b(i): Average distance to points in nearest cluster

#### Interpretation

- s(i) ≈ 1: Point is far from neighboring clusters
- s(i) ≈ 0: Point is on or very close to decision boundary
- s(i) ≈ -1: Point might be assigned to wrong cluster

### Python Implementation for Evaluation

```python
from sklearn.metrics import (silhouette_score, calinski_harabasz_score, 
                           adjusted_rand_score, adjusted_mutual_info_score,
                           homogeneity_score, completeness_score, v_measure_score)

# Generate data with known clusters
X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

# Apply clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
y_pred = kmeans.fit_predict(X)

# Internal metrics
silhouette = silhouette_score(X, y_pred)
ch_score = calinski_harabasz_score(X, y_pred)
inertia = kmeans.inertia_

print("=== Internal Metrics ===")
print(f"Silhouette Score: {silhouette:.3f}")
print(f"Calinski-Harabasz Score: {ch_score:.3f}")
print(f"Inertia (WCSS): {inertia:.3f}")

# External metrics (when true labels are available)
ari = adjusted_rand_score(y_true, y_pred)
ami = adjusted_mutual_info_score(y_true, y_pred)
homogeneity = homogeneity_score(y_true, y_pred)
completeness = completeness_score(y_true, y_pred)
v_measure = v_measure_score(y_true, y_pred)

print("\n=== External Metrics ===")
print(f"Adjusted Rand Index: {ari:.3f}")
print(f"Adjusted Mutual Information: {ami:.3f}")
print(f"Homogeneity: {homogeneity:.3f}")
print(f"Completeness: {completeness:.3f}")
print(f"V-Measure: {v_measure:.3f}")

# Visualize silhouette scores
from sklearn.metrics import silhouette_samples
import matplotlib.cm as cm

sample_silhouette_values = silhouette_samples(X, y_pred)
n_clusters = 4

plt.figure(figsize=(10, 7))
y_lower = 10

for i in range(n_clusters):
    ith_cluster_silhouette_values = sample_silhouette_values[y_pred == i]
    ith_cluster_silhouette_values.sort()
  
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
  
    color = cm.nipy_spectral(float(i) / n_clusters)
    plt.fill_betweenx(np.arange(y_lower, y_upper), 0, ith_cluster_silhouette_values,
                     facecolor=color, edgecolor=color, alpha=0.7)
  
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    y_lower = y_upper + 10

plt.axvline(x=silhouette, color="red", linestyle="--")
plt.xlabel("Silhouette coefficient values")
plt.ylabel("Cluster label")
plt.title("Silhouette plot for K-Means clustering")
plt.show()
```

---

## 5. Principal Component Analysis (PCA)

PCA is a dimensionality reduction technique that transforms data into principal components.

### 5.1 Mathematical Foundation

#### Covariance Matrix

```
C = (1/n) X^T X
```

#### Eigenvalue Decomposition

```
C v = λ v
```

#### Explained Variance

```
Explained Variance Ratio = λ_i / Σ λ_j
```

### 5.2 Implementation Steps

1. **Standardize data**: Mean = 0, variance = 1
2. **Compute covariance matrix**
3. **Calculate eigenvalues and eigenvectors**
4. **Sort by eigenvalues** (descending)
5. **Select top k components**
6. **Transform data**: Project onto new basis

### 5.3 Python Implementation

#### Example 1: PCA for Dimensionality Reduction

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# Load digits dataset (64 features)
digits = load_digits()
X = digits.data
y = digits.target

print("Original shape:", X.shape)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

print("PCA shape:", X_pca.shape)
print("Explained variance ratio:", pca.explained_variance_ratio_)
print("Total explained variance:", sum(pca.explained_variance_ratio_))

# Plot PCA results
plt.figure(figsize=(10, 8))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10', alpha=0.7)
plt.colorbar(scatter)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Digits Dataset')
plt.show()
```

#### Example 2: Choosing Number of Components

```python
# Plot explained variance
pca_full = PCA()
pca_full.fit(X)

plt.figure(figsize=(10, 6))
plt.plot(range(1, len(pca_full.explained_variance_ratio_) + 1), 
         pca_full.explained_variance_ratio_.cumsum(), marker='o')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('PCA: Cumulative Explained Variance')
plt.grid(True)
plt.show()

# Find number of components for 95% variance
cumsum = np.cumsum(pca_full.explained_variance_ratio_)
n_components_95 = np.argmax(cumsum >= 0.95) + 1
print(f"Components needed for 95% variance: {n_components_95}")
```

#### Example 3: PCA for Visualization

```python
# Reduce to 3D for visualization
pca_3d = PCA(n_components=3)
X_pca_3d = pca_3d.fit_transform(X)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_pca_3d[:, 0], X_pca_3d[:, 1], X_pca_3d[:, 2], 
                    c=y, cmap='tab10', alpha=0.7)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('PC3')
ax.set_title('3D PCA of Digits Dataset')
plt.colorbar(scatter)
plt.show()
```

---

## 6. Ethics in Machine Learning

### 6.1 Bias and Fairness

#### Types of Bias

- **Selection Bias**: Non-representative training data
- **Confirmation Bias**: Reinforcing existing beliefs
- **Algorithmic Bias**: Discriminatory outcomes

#### Fairness Metrics

- **Demographic Parity**: Equal positive outcomes across groups
- **Equal Opportunity**: Equal true positive rates
- **Equalized Odds**: Equal TPR and FPR across groups

### 6.2 Privacy and Data Protection

#### Privacy Concerns

- **Data Collection**: Consent and transparency
- **Data Storage**: Security and retention
- **Data Usage**: Purpose limitation

#### Regulations

- **GDPR**: General Data Protection Regulation
- **CCPA**: California Consumer Privacy Act
- **Data minimization**: Collect only necessary data

### 6.3 Transparency and Explainability

#### Black Box Problem

- Complex models are hard to interpret
- Need for explainable AI (XAI)

#### Techniques

- **Feature Importance**: Which features matter most
- **Partial Dependence Plots**: How features affect predictions
- **SHAP Values**: Shapley Additive Explanations

### 6.4 Accountability

#### Responsible AI Practices

- **Bias Audits**: Regular model evaluation
- **Human Oversight**: Human-in-the-loop systems
- **Error Reporting**: Mechanisms for reporting issues

---

## 7. Model Deployment and Production

### 7.1 Model Serialization

#### Pickle (Python)

```python
import pickle

# Save model
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Load model
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
```

#### Joblib (Better for large models)

```python
from joblib import dump, load

# Save model
dump(model, 'model.joblib')

# Load model
loaded_model = load('model.joblib')
```

### 7.2 APIs and Web Services

#### Flask API Example

```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
```

### 7.3 Monitoring and Maintenance

#### Performance Monitoring

- **Accuracy Drift**: Model performance over time
- **Data Drift**: Input data distribution changes
- **Concept Drift**: Relationship between inputs and outputs changes

#### Maintenance Tasks

- **Model Retraining**: Periodic updates with new data
- **Version Control**: Track model versions
- **Rollback Strategy**: Ability to revert to previous versions

### 7.4 Python Implementation

#### Example 1: Model Serialization

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import joblib

# Train a model
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, 'rf_model.joblib')
print("Model saved successfully")

# Load model
loaded_model = joblib.load('rf_model.joblib')
print("Model loaded successfully")

# Test prediction
sample_data = X[:5]
original_pred = model.predict(sample_data)
loaded_pred = loaded_model.predict(sample_data)

print("Predictions match:", np.array_equal(original_pred, loaded_pred))
```

#### Example 2: Simple Flask API

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model (assuming it's saved)
# model = joblib.load('rf_model.joblib')

@app.route('/')
def home():
    return "ML Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
      
        # Extract features
        features = data['features']
      
        # Convert to numpy array
        features_array = np.array(features).reshape(1, -1)
      
        # Make prediction (using dummy prediction for demo)
        # prediction = model.predict(features_array)
        prediction = [1]  # Dummy prediction
      
        # Return result
        return jsonify({
            'prediction': prediction,
            'status': 'success'
        })
  
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### Example 3: Model Monitoring

```python
import time
from sklearn.metrics import accuracy_score

class ModelMonitor:
    def __init__(self, model, threshold=0.8):
        self.model = model
        self.threshold = threshold
        self.predictions = []
        self.actuals = []
        self.accuracies = []
  
    def predict(self, X):
        return self.model.predict(X)
  
    def update_metrics(self, y_pred, y_true):
        self.predictions.extend(y_pred)
        self.actuals.extend(y_true)
      
        if len(self.predictions) >= 100:  # Calculate every 100 predictions
            accuracy = accuracy_score(self.actuals, self.predictions)
            self.accuracies.append(accuracy)
          
            if accuracy < self.threshold:
                print(f"WARNING: Model accuracy dropped to {accuracy:.3f}")
                # Trigger retraining or alert
          
            # Reset for next batch
            self.predictions = []
            self.actuals = []
  
    def get_performance_history(self):
        return self.accuracies

# Example usage
monitor = ModelMonitor(model)

# Simulate monitoring
for i in range(5):
    X_batch, y_batch = make_classification(n_samples=100, n_features=20, random_state=i)
    y_pred = monitor.predict(X_batch)
    monitor.update_metrics(y_pred, y_batch)
    time.sleep(0.1)  # Simulate time between batches

print("Performance history:", monitor.get_performance_history())
```

---

## 8. Real-World Applications

### Clustering Applications

- **Customer Segmentation**: Group customers by behavior
- **Image Segmentation**: Divide images into meaningful regions
- **Anomaly Detection**: Identify unusual patterns
- **Document Clustering**: Group similar documents

### Dimensionality Reduction Applications

- **Image Compression**: Reduce storage requirements
- **Feature Visualization**: Plot high-dimensional data
- **Noise Reduction**: Remove irrelevant features
- **Preprocessing**: Prepare data for other algorithms

### Ethics and Deployment

- **Fair Hiring Systems**: Bias-free recruitment
- **Credit Scoring**: Fair lending decisions
- **Healthcare AI**: Ethical medical predictions
- **Autonomous Vehicles**: Safe deployment practices

---

## 9. Terminal Learning Objectives (TLOs) Mapping

### TLO 1: Understand unsupervised learning concepts

- Covered in section 1

### TLO 2: Implement K-Means clustering

- Covered in section 2

### TLO 3: Apply hierarchical clustering

- Covered in section 3

### TLO 4: Evaluate clustering performance

- Covered in section 4

### TLO 5: Implement PCA for dimensionality reduction

- Covered in section 5

### TLO 6: Understand ethics in ML

- Covered in section 6

### TLO 7: Deploy ML models

- Covered in section 7

---

## 10. Exam Questions and Practice

### Short Answer Questions

1. What is unsupervised learning? Give examples.
2. Explain how K-Means clustering works.
3. What is the elbow method and why is it used?
4. Compare agglomerative and divisive clustering.
5. What is a dendrogram?
6. Explain the silhouette coefficient.
7. What is PCA and why is it used?
8. What are ethical concerns in machine learning?
9. How do you deploy a machine learning model?

### Long Answer Questions

1. Explain the K-Means algorithm with steps and example.
2. Discuss different linkage methods in hierarchical clustering.
3. Compare internal and external clustering evaluation metrics.
4. Explain PCA with mathematical foundation and implementation.
5. Discuss ethical considerations in machine learning deployment.

### Practical Questions

1. Implement K-Means clustering on iris dataset.
2. Create dendrogram for hierarchical clustering.
3. Apply PCA for dimensionality reduction.
4. Evaluate clustering using silhouette analysis.
5. Serialize and load a machine learning model.

### Numerical Problems

1. Calculate WCSS for given clusters.
2. Find optimal K using elbow method.
3. Compute silhouette coefficient for a point.
4. Calculate explained variance in PCA.
5. Determine number of components for 95% variance.

---

## 11. Summary

Unsupervised learning algorithms discover hidden patterns in data without labeled examples. Key takeaways:

1. **K-Means**: Simple, efficient clustering for spherical clusters
2. **Hierarchical Clustering**: Builds cluster hierarchy, good for small datasets
3. **Evaluation**: Use internal metrics when labels unavailable, external when available
4. **PCA**: Powerful dimensionality reduction, preserves variance
5. **Ethics**: Bias, fairness, and privacy are crucial considerations
6. **Deployment**: Model serialization, APIs, and monitoring ensure production success

Mastering these techniques enables you to extract insights from unlabeled data and deploy responsible AI systems.

---

*This completes the detailed notes for Unit V: Unsupervised Learning Algorithms. These notes are aligned with MSBTE K-Scheme syllabus and designed for diploma-level understanding with practical examples and code snippets.*


---
## Unit Notes

- 📝 **Complete Unit Notes (Markdown)**
  - [View Notes](../notes/unit-05/unit-05-notes.md)
---
