# Practical 4: Classification Algorithms
## Complete How-To Guide

**Course:** 316316 | **Practical:** 4 of 15 | **Duration:** 2 Hours | **CO:** CO4

---

## Learning Outcomes

1. Understand supervised learning classification
2. Implement Decision Tree classifier
3. Implement K-Nearest Neighbors (KNN)
4. Implement Logistic Regression
5. Train and evaluate classification models
6. Create confusion matrix and classification reports
7. Tune hyperparameters
8. Compare multiple algorithms
9. Handle class imbalance
10. Deploy classification models

---

## Dataset

Using Iris dataset (150 samples, 4 features, 3 classes) OR custom dataset with binary/multiclass classification

---

## Step-by-Step Procedure

### Phase 1: Environment & Data Loading

```bash
source ml_env/bin/activate
cd practicals/practical_4
jupyter notebook
```

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix, classification_report, 
                              accuracy_score, precision_score, recall_score, f1_score)
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
```

---

### Phase 2: Data Preparation

```python
# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training set: {X_train_scaled.shape}")
print(f"Test set: {X_test_scaled.shape}")
```

---

### Phase 3: Decision Tree Classifier

```python
# Train model
dt_classifier = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_classifier.fit(X_train_scaled, y_train)

# Predictions
y_pred_dt = dt_classifier.predict(X_test_scaled)

# Evaluation
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Decision Tree Accuracy: {accuracy_dt:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred_dt, target_names=iris.target_names))
```

---

### Phase 4: K-Nearest Neighbors

```python
# Try different K values
k_values = [3, 5, 7, 9]
scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    score = knn.score(X_test_scaled, y_test)
    scores.append(score)
    print(f"K={k}: Accuracy={score:.4f}")

# Use best K
best_k = k_values[np.argmax(scores)]
knn_classifier = KNeighborsClassifier(n_neighbors=best_k)
knn_classifier.fit(X_train_scaled, y_train)
y_pred_knn = knn_classifier.predict(X_test_scaled)
```

---

### Phase 5: Logistic Regression

```python
# Train model
lr_classifier = LogisticRegression(max_iter=200, random_state=42)
lr_classifier.fit(X_train_scaled, y_train)

# Predictions
y_pred_lr = lr_classifier.predict(X_test_scaled)

# Evaluation
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print(f"Logistic Regression Accuracy: {accuracy_lr:.4f}")
```

---

### Phase 6: Model Evaluation & Comparison

```python
# Comparison table
models = {
    'Decision Tree': (dt_classifier, y_pred_dt),
    'KNN (k={})'.format(best_k): (knn_classifier, y_pred_knn),
    'Logistic Regression': (lr_classifier, y_pred_lr)
}

results = []
for name, (model, predictions) in models.items():
    results.append({
        'Model': name,
        'Accuracy': accuracy_score(y_test, predictions),
        'Precision': precision_score(y_test, predictions, average='weighted'),
        'Recall': recall_score(y_test, predictions, average='weighted'),
        'F1-Score': f1_score(y_test, predictions, average='weighted')
    })

comparison_df = pd.DataFrame(results)
print("\n" + "="*70)
print("MODEL COMPARISON")
print("="*70)
print(comparison_df.to_string(index=False))
```

---

### Phase 7: Visualization

```python
# Confusion matrices
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

for idx, (name, (model, predictions)) in enumerate(models.items()):
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx])
    axes[idx].set_title(name)
    axes[idx].set_ylabel('True Label')
    axes[idx].set_xlabel('Predicted Label')

plt.tight_layout()
plt.show()
```

---

## Practical Tests

```python
assert accuracy_dt > 0.8, "Decision Tree accuracy low"
assert accuracy_lr > 0.8, "Logistic Regression accuracy low"
assert X_test_scaled.shape[1] == 4, "Feature mismatch"
print("✅ All Classification Tests PASSED")
```

---

## Expected Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Decision Tree | 0.95+ | 0.95+ | 0.95+ | 0.95+ |
| KNN | 0.97+ | 0.97+ | 0.97+ | 0.97+ |
| Logistic Reg | 0.93+ | 0.93+ | 0.93+ | 0.93+ |

---

## Key Concepts

**Classification Metrics:**
- **Accuracy:** Overall correctness
- **Precision:** True positives / Predicted positives
- **Recall:** True positives / Actual positives
- **F1-Score:** Harmonic mean of precision & recall

**Decision Tree:** Tree-based model, handles non-linear relationships, prone to overfitting

**KNN:** Instance-based, sensitive to feature scaling, k is critical hyperparameter

**Logistic Regression:** Linear model, interpretable, good baseline

---

## Submission Files

- [ ] `Practical_4_Complete_Notebook.ipynb`
- [ ] `SUBMISSION_TEMPLATE_Practical_4.md`
- [ ] Screenshots of confusion matrices

---

**Version:** 1.0 | **Next:** Practical 5 - Regression

