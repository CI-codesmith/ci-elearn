---
**MindforgeAi Publications**

**Technical Publication Series**

**Chatake Innoworks Pvt. Ltd.**

**Copyright © 2025 Chatake Innoworks Pvt. Ltd.**

**Authored by: Akash Chatake**
---
# UNIT IV: SUPERVISED LEARNING ALGORITHMS - COMPLETE DIPLOMA NOTES

## MSBTE K-Scheme Syllabus (Course Code: 316316, Semester 6)

## Machine Learning - Detailed Theory Notes for Diploma Students

---

## Table of Contents

1. [Introduction to Supervised Learning](#introduction-to-supervised-learning)
2. [Decision Tree Algorithm](#decision-tree-algorithm)
   - 2.1 [How Decision Trees Work](#how-decision-trees-work)
   - 2.2 [Tree Construction](#tree-construction)
   - 2.3 [Splitting Criteria](#splitting-criteria)
   - 2.4 [Pruning Techniques](#pruning-techniques)
   - 2.5 [Python Implementation](#python-implementation-decision-tree)
3. [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
   - 3.1 [How KNN Works](#how-knn-works)
   - 3.2 [Distance Metrics](#distance-metrics)
   - 3.3 [Choosing K Value](#choosing-k-value)
   - 3.4 [Python Implementation](#python-implementation-knn)
4. [Support Vector Machine (SVM)](#support-vector-machine-svm)
   - 4.1 [Linear SVM](#linear-svm)
   - 4.2 [Non-Linear SVM](#non-linear-svm)
   - 4.3 [Kernel Functions](#kernel-functions)
   - 4.4 [Python Implementation](#python-implementation-svm)
5. [Linear Regression](#linear-regression)
   - 5.1 [Simple Linear Regression](#simple-linear-regression)
   - 5.2 [Multiple Linear Regression](#multiple-linear-regression)
   - 5.3 [Cost Function and Gradient Descent](#cost-function-and-gradient-descent)
   - 5.4 [Python Implementation](#python-implementation-linear-regression)
6. [Logistic Regression](#logistic-regression)
   - 6.1 [Sigmoid Function](#sigmoid-function)
   - 6.2 [Cost Function](#cost-function)
   - 6.3 [Multi-class Classification](#multi-class-classification)
   - 6.4 [Python Implementation](#python-implementation-logistic-regression)
7. [Model Evaluation Metrics](#model-evaluation-metrics)
   - 7.1 [Classification Metrics](#classification-metrics)
   - 7.2 [Regression Metrics](#regression-metrics)
   - 7.3 [Confusion Matrix](#confusion-matrix)
   - 7.4 [ROC and AUC](#roc-and-auc)
8. [Algorithm Comparison](#algorithm-comparison)
9. [Real-World Applications](#real-world-applications)
10. [Terminal Learning Objectives (TLOs) Mapping](#terminal-learning-objectives-tlos-mapping)
11. [Exam Questions and Practice](#exam-questions-and-practice)
12. [Summary](#summary)

---

## 1. Introduction to Supervised Learning

Supervised learning is a type of machine learning where the algorithm learns from labeled training data to make predictions on new, unseen data.

### Key Concepts

- **Labeled Data**: Training data with known outputs
- **Features/Input Variables**: Independent variables (X)
- **Target/Output Variable**: Dependent variable (Y)
- **Training Phase**: Learning patterns from data
- **Prediction Phase**: Applying learned patterns to new data

### Types of Supervised Learning

1. **Regression**: Predict continuous values

   - House price prediction
   - Stock price forecasting
   - Temperature prediction
2. **Classification**: Predict discrete categories

   - Email spam detection
   - Disease diagnosis
   - Customer churn prediction

### Supervised Learning Workflow

```
Data Collection
     ↓
Data Preprocessing
     ↓
Feature Selection/Extraction
     ↓
Algorithm Selection
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Deployment
```

---

\newpage

## 2. Decision Tree Algorithm

Decision trees are versatile algorithms that can perform both classification and regression tasks. They work by recursively splitting the data based on feature values.

### 2.1 How Decision Trees Work

A decision tree is a flowchart-like structure where:

- **Internal nodes**: Represent features/attributes
- **Branches**: Represent decision rules
- **Leaf nodes**: Represent outcomes/classes

### Example Decision Tree

```
Outlook
├── Sunny
│   ├── Humidity
│   │   ├── High → No
│   │   └── Normal → Yes
└── Overcast → Yes
└── Rain
    ├── Wind
    │   ├── Strong → No
    │   └── Weak → Yes
```

### 2.2 Tree Construction

#### Recursive Partitioning

1. Start with all training data at root
2. Select best feature to split on
3. Partition data based on feature values
4. Repeat for each subset until stopping criteria met

#### Stopping Criteria

- All instances in node belong to same class
- No more features to split on
- Maximum tree depth reached
- Minimum samples per leaf reached

### 2.3 Splitting Criteria

#### For Classification

1. **Gini Impurity**: Measures node purity

   ```
   Gini = 1 - Σ(p_i²)
   ```

   Where p_i is proportion of class i
2. **Entropy**: Measures disorder

   ```
   Entropy = -Σ(p_i * log₂(p_i))
   ```
3. **Information Gain**: Reduction in entropy

   ```
   IG = Entropy(parent) - Σ(weighted_entropy(children))
   ```

#### For Regression

1. **Mean Squared Error (MSE)**
2. **Mean Absolute Error (MAE)**

### 2.4 Pruning Techniques

#### Pre-pruning (Early Stopping)

- Stop growing tree before it becomes too complex
- Set maximum depth, minimum samples, etc.

#### Post-pruning

- Grow full tree, then remove branches
- **Reduced Error Pruning**: Remove branches if accuracy improves
- **Cost Complexity Pruning**: Balance accuracy vs complexity

### 2.5 Python Implementation

#### Example 1: Decision Tree Classification

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
dt_classifier = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
dt_classifier.fit(X_train, y_train)

# Make predictions
y_pred = dt_classifier.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Tree Accuracy: {accuracy:.3f}")

# Feature importance
feature_importance = dt_classifier.feature_importances_
print("Feature Importance:", feature_importance)
```

#### Example 2: Decision Tree Regression

```python
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import make_regression

# Generate regression data
X, y = make_regression(n_samples=100, n_features=1, noise=0.1, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
dt_regressor = DecisionTreeRegressor(max_depth=4, random_state=42)
dt_regressor.fit(X_train, y_train)

# Make predictions
y_pred = dt_regressor.predict(X_test)

# Evaluate
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"Decision Tree MSE: {mse:.3f}")
```

#### Example 3: Visualizing Decision Tree

```python
from sklearn.tree import plot_tree

# Plot tree
plt.figure(figsize=(20,10))
plot_tree(dt_classifier, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree Visualization")
plt.show()
```

#### Example 4: Manual Gini Calculation

```python
import numpy as np

def gini_impurity(y):
    """Calculate Gini impurity for a node"""
    if len(y) == 0:
        return 0
  
    classes, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    gini = 1 - np.sum(probabilities ** 2)
    return gini

# Example
y_example = [0, 0, 1, 1, 1]
gini = gini_impurity(y_example)
print(f"Gini Impurity: {gini:.3f}")
```

---

\newpage

## 3. K-Nearest Neighbors (KNN)

KNN is a simple, instance-based learning algorithm that classifies new instances based on similarity to training instances.

### 3.1 How KNN Works

1. **Store Training Data**: Memorize all training examples
2. **Calculate Distance**: Compute distance between new instance and all training instances
3. **Find K Neighbors**: Select K closest training instances
4. **Vote/Predict**: For classification - majority vote; For regression - average value

### Classification Example

```
New point: (5, 3)
K = 3

Training points:
A: (2, 2) - Class Red
B: (3, 3) - Class Red  
C: (4, 4) - Class Blue
D: (6, 2) - Class Blue
E: (7, 3) - Class Blue

Distances: A=3.16, B=2.00, C=1.41, D=1.00, E=2.00
K=3 closest: C(1.41), D(1.00), E(2.00) - All Blue
Prediction: Blue
```

### 3.2 Distance Metrics

#### Euclidean Distance (L2)

```
d = √(Σ(x_i - y_i)²)
```

#### Manhattan Distance (L1)

```
d = Σ|x_i - y_i|
```

#### Minkowski Distance (Lp)

```
d = (Σ|x_i - y_i|^p)^(1/p)
```

#### Hamming Distance

- For categorical variables
- Number of positions where values differ

### 3.3 Choosing K Value

#### Small K (e.g., K=1)

- **Advantages**: Captures local patterns, low bias
- **Disadvantages**: High variance, sensitive to noise

#### Large K (e.g., K=20)

- **Advantages**: More stable, less sensitive to noise
- **Disadvantages**: May miss local patterns, higher bias

#### Choosing Optimal K

- **Odd K**: Avoid ties in binary classification
- **Cross-validation**: Test different K values
- **Rule of thumb**: K = √(n) where n is sample size

### 3.4 Python Implementation

#### Example 1: KNN Classification

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Generate data
X, y = make_classification(n_samples=200, n_features=2, n_classes=2, 
                          n_informative=2, n_redundant=0, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train KNN
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Evaluate
print("KNN Classification Report:")
print(classification_report(y_test, y_pred))
```

#### Example 2: KNN Regression

```python
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import mean_absolute_error

# Generate regression data
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train KNN regressor
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)

# Make predictions
y_pred = knn_reg.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, y_pred)
print(f"KNN Regression MAE: {mae:.3f}")
```

#### Example 3: Finding Optimal K

```python
from sklearn.model_selection import cross_val_score

# Test different K values
k_values = range(1, 21, 2)
cv_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)
    cv_scores.append(scores.mean())

# Find best K
best_k = k_values[np.argmax(cv_scores)]
print(f"Best K value: {best_k}")
print(f"Best CV Score: {max(cv_scores):.3f}")

# Plot K vs accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, cv_scores, marker='o')
plt.xlabel('K Value')
plt.ylabel('Cross-Validation Accuracy')
plt.title('KNN: K Value vs Accuracy')
plt.grid(True)
plt.show()
```

#### Example 4: Manual KNN Implementation

```python
import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def knn_predict(X_train, y_train, X_test, k=5):
    predictions = []
  
    for test_point in X_test:
        # Calculate distances
        distances = [euclidean_distance(test_point, train_point) for train_point in X_train]
      
        # Get k nearest neighbors
        k_indices = np.argsort(distances)[:k]
        k_labels = [y_train[i] for i in k_indices]
      
        # Majority vote
        most_common = Counter(k_labels).most_common(1)[0][0]
        predictions.append(most_common)
  
    return np.array(predictions)

# Test manual KNN
X_train_small = X_train[:20]
y_train_small = y_train[:20]
X_test_small = X_test[:10]

predictions = knn_predict(X_train_small, y_train_small, X_test_small, k=3)
accuracy = np.mean(predictions == y_test[:10])
print(f"Manual KNN Accuracy: {accuracy:.3f}")
```

---

\newpage

## 4. Support Vector Machine (SVM)

SVM is a powerful supervised learning algorithm that finds the optimal hyperplane to separate classes in feature space.

### 4.1 Linear SVM

#### Concept

- Find hyperplane that maximizes margin between classes
- Support vectors are data points closest to the hyperplane
- Margin = distance between hyperplane and nearest support vectors

#### Mathematical Formulation

For linearly separable data:

```
Minimize: (1/2)||w||²
Subject to: y_i(w·x_i + b) ≥ 1 for all i
```

Where:

- w: normal vector to hyperplane
- b: bias term
- y_i: class labels (+1 or -1)

### 4.2 Non-Linear SVM

#### Kernel Trick

Transform data to higher-dimensional space where linear separation is possible.

#### Common Kernel Functions

1. **Polynomial Kernel**

   ```
   K(x,y) = (x·y + c)^d
   ```
2. **Radial Basis Function (RBF)**

   ```
   K(x,y) = exp(-γ||x-y||²)
   ```
3. **Sigmoid Kernel**

   ```
   K(x,y) = tanh(α(x·y) + c)
   ```

### 4.3 Kernel Functions

#### Choosing the Right Kernel

| Kernel     | Use Case                                 | Parameters    |
| ---------- | ---------------------------------------- | ------------- |
| Linear     | Linearly separable data                  | None          |
| Polynomial | Non-linear, polynomial decision boundary | degree, coef0 |
| RBF        | Complex non-linear boundaries            | gamma         |
| Sigmoid    | Neural network-like behavior             | coef0         |

#### Kernel Parameters

- **C**: Regularization parameter (trade-off between margin and misclassification)
- **gamma**: Kernel coefficient for RBF (smaller = smoother, larger = more complex)

### 4.4 Python Implementation

#### Example 1: Linear SVM

```python
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate linearly separable data
X, y = make_classification(n_samples=200, n_features=2, n_classes=2, 
                          n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train linear SVM
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train, y_train)

# Make predictions
y_pred = svm_linear.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Linear SVM Accuracy: {accuracy:.3f}")
print(f"Number of support vectors: {svm_linear.n_support_}")
```

#### Example 2: Non-Linear SVM with RBF Kernel

```python
# Create and train RBF SVM
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_rbf.fit(X_train, y_train)

# Make predictions
y_pred_rbf = svm_rbf.predict(X_test)

# Evaluate
accuracy_rbf = accuracy_score(y_test, y_pred_rbf)
print(f"RBF SVM Accuracy: {accuracy_rbf:.3f}")
```

#### Example 3: SVM with Different Kernels

```python
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
accuracies = []

for kernel in kernels:
    if kernel == 'poly':
        svm = SVC(kernel=kernel, degree=3, C=1.0)
    else:
        svm = SVC(kernel=kernel, C=1.0)
  
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    print(f"{kernel.upper()} SVM Accuracy: {acc:.3f}")

# Plot comparison
plt.figure(figsize=(8, 5))
plt.bar(kernels, accuracies)
plt.xlabel('Kernel')
plt.ylabel('Accuracy')
plt.title('SVM Kernel Comparison')
plt.show()
```

#### Example 4: SVM Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {'C': [0.1, 1, 10, 100],
              'gamma': [1, 0.1, 0.01, 0.001],
              'kernel': ['rbf']}

# Grid search
grid = GridSearchCV(SVC(), param_grid, cv=5)
grid.fit(X_train, y_train)

print("Best parameters:", grid.best_params_)
print("Best cross-validation score:", grid.best_score_)

# Evaluate best model
best_model = grid.best_estimator_
y_pred_best = best_model.predict(X_test)
accuracy_best = accuracy_score(y_test, y_pred_best)
print(f"Best model test accuracy: {accuracy_best:.3f}")
```

---

## 5. Linear Regression

Linear regression is a supervised learning algorithm that models the relationship between a dependent variable and one or more independent variables.

### 5.1 Simple Linear Regression

#### Model

```
y = mx + c
```

Where:

- y: dependent variable
- x: independent variable
- m: slope/coefficient
- c: intercept

#### Assumptions

1. Linearity: Linear relationship between x and y
2. Independence: Observations are independent
3. Homoscedasticity: Constant variance of residuals
4. Normality: Residuals are normally distributed

### 5.2 Multiple Linear Regression

#### Model

```
y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ + ε
```

#### Matrix Form

```
y = Xβ + ε
```

Where:

- y: target vector
- X: feature matrix
- β: coefficient vector
- ε: error term

### 5.3 Cost Function and Gradient Descent

#### Mean Squared Error (MSE)

```
MSE = (1/n) Σ(y_i - ŷ_i)²
```

#### Gradient Descent

1. Initialize parameters (θ)
2. Compute predictions (ŷ)
3. Calculate cost (J)
4. Update parameters: θ = θ - α * ∂J/∂θ
5. Repeat until convergence

### 5.4 Python Implementation

#### Example 1: Simple Linear Regression

```python
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error, r2_score

# Generate data
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Make predictions
y_pred = lr.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression MSE: {mse:.3f}")
print(f"Linear Regression R²: {r2:.3f}")
print(f"Coefficient: {lr.coef_[0]:.3f}")
print(f"Intercept: {lr.intercept_:.3f}")
```

#### Example 2: Multiple Linear Regression

```python
# Generate multiple features
X, y = make_regression(n_samples=100, n_features=3, noise=10, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
lr_multi = LinearRegression()
lr_multi.fit(X_train, y_train)

# Make predictions
y_pred_multi = lr_multi.predict(X_test)

# Evaluate
mse_multi = mean_squared_error(y_test, y_pred_multi)
r2_multi = r2_score(y_test, y_pred_multi)

print(f"Multiple LR MSE: {mse_multi:.3f}")
print(f"Multiple LR R²: {r2_multi:.3f}")
print("Coefficients:", lr_multi.coef_)
print(f"Intercept: {lr_multi.intercept_:.3f}")
```

#### Example 3: Manual Linear Regression

```python
def manual_linear_regression(X, y):
    # Add bias term
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
  
    # Normal equation: θ = (X^T X)^(-1) X^T y
    theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
  
    return theta

# Test manual implementation
X_simple = X_train[:50, 0].reshape(-1, 1)  # Single feature
y_simple = y_train[:50]

theta_manual = manual_linear_regression(X_simple, y_simple)
print("Manual coefficients:", theta_manual)

# Compare with sklearn
lr_manual = LinearRegression()
lr_manual.fit(X_simple, y_simple)
print("Sklearn coefficients:", [lr_manual.intercept_, lr_manual.coef_[0]])
```

#### Example 4: Polynomial Regression

```python
from sklearn.preprocessing import PolynomialFeatures

# Generate non-linear data
X, y = make_regression(n_samples=100, n_features=1, noise=20, random_state=42)

# Create polynomial features
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Train polynomial regression
poly_lr = LinearRegression()
poly_lr.fit(X_poly, y)

# Make predictions
X_test_poly = poly_features.transform(X_test)
y_pred_poly = poly_lr.predict(X_test_poly)

# Evaluate
mse_poly = mean_squared_error(y_test, y_pred_poly)
r2_poly = r2_score(y_test, y_pred_poly)

print(f"Polynomial Regression MSE: {mse_poly:.3f}")
print(f"Polynomial Regression R²: {r2_poly:.3f}")
```

---

## 6. Logistic Regression

Logistic regression is a classification algorithm that predicts the probability of a binary outcome.

### 6.1 Sigmoid Function

#### Logistic Function

```
σ(z) = 1 / (1 + e^(-z))
```

Where z = w·x + b

#### Properties

- Output range: (0, 1)
- S-shaped curve
- Differentiable everywhere

### 6.2 Cost Function

#### Log Loss (Binary Cross-Entropy)

```
J = -(1/n) Σ[y_i log(ŷ_i) + (1-y_i) log(1-ŷ_i)]
```

#### Why not MSE?

- Non-convex optimization
- Not suitable for probabilistic interpretation

### 6.3 Multi-class Classification

#### One-vs-Rest (OvR)

- Train n binary classifiers for n classes
- Each classifier predicts probability of belonging to one class

#### Softmax Regression

- Generalization of logistic regression for multiple classes
- Uses softmax function instead of sigmoid

### 6.4 Python Implementation

#### Example 1: Binary Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, confusion_matrix

# Generate binary classification data
X, y = make_classification(n_samples=200, n_features=2, n_classes=2, 
                          n_informative=2, n_redundant=0, random_state=42)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train model
log_reg = LogisticRegression(random_state=42)
log_reg.fit(X_train, y_train)

# Make predictions
y_pred = log_reg.predict(X_test)
y_pred_proba = log_reg.predict_proba(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Accuracy: {accuracy:.3f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)
```

#### Example 2: Multi-class Logistic Regression

```python
# Generate multi-class data
X_multi, y_multi = make_classification(n_samples=300, n_features=2, n_classes=3, 
                                      n_informative=2, n_redundant=0, 
                                      n_clusters_per_class=1, random_state=42)

# Split data
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X_multi, y_multi, test_size=0.3, random_state=42)

# Train multi-class logistic regression
log_reg_multi = LogisticRegression(multi_class='ovr', random_state=42)
log_reg_multi.fit(X_train_multi, y_train_multi)

# Make predictions
y_pred_multi = log_reg_multi.predict(X_test_multi)

# Evaluate
accuracy_multi = accuracy_score(y_test_multi, y_pred_multi)
print(f"Multi-class LR Accuracy: {accuracy_multi:.3f}")
```

#### Example 3: Logistic Regression with Regularization

```python
# Different regularization strengths
C_values = [0.01, 0.1, 1, 10, 100]
accuracies = []

for C in C_values:
    log_reg_reg = LogisticRegression(C=C, random_state=42)
    log_reg_reg.fit(X_train, y_train)
    y_pred_reg = log_reg_reg.predict(X_test)
    acc = accuracy_score(y_test, y_pred_reg)
    accuracies.append(acc)
    print(f"C={C}: Accuracy={acc:.3f}")

# Plot regularization effect
plt.figure(figsize=(8, 5))
plt.semilogx(C_values, accuracies, marker='o')
plt.xlabel('C (Inverse regularization strength)')
plt.ylabel('Accuracy')
plt.title('Logistic Regression: Regularization Effect')
plt.grid(True)
plt.show()
```

#### Example 4: Manual Logistic Regression

```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def manual_logistic_regression(X, y, learning_rate=0.01, epochs=1000):
    # Add bias term
    X_b = np.c_[np.ones((X.shape[0], 1)), X]
  
    # Initialize weights
    weights = np.zeros(X_b.shape[1])
  
    for epoch in range(epochs):
        # Forward pass
        z = X_b.dot(weights)
        predictions = sigmoid(z)
      
        # Compute gradients
        errors = predictions - y
        gradients = X_b.T.dot(errors) / len(y)
      
        # Update weights
        weights -= learning_rate * gradients
  
    return weights

# Test manual implementation
X_binary = X_train[:100]
y_binary = y_train[:100]

weights_manual = manual_logistic_regression(X_binary, y_binary)
print("Manual weights:", weights_manual)

# Compare with sklearn
log_reg_manual = LogisticRegression(random_state=42)
log_reg_manual.fit(X_binary, y_binary)
print("Sklearn weights:", np.concatenate([[log_reg_manual.intercept_[0]], log_reg_manual.coef_[0]]))
```

---

## 7. Model Evaluation Metrics

### 7.1 Classification Metrics

#### Accuracy

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

#### Precision

```
Precision = TP / (TP + FP)
```

#### Recall (Sensitivity)

```
Recall = TP / (TP + FN)
```

#### F1-Score

```
F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

#### Specificity

```
Specificity = TN / (TN + FP)
```

### 7.2 Regression Metrics

#### Mean Absolute Error (MAE)

```
MAE = (1/n) Σ|y_i - ŷ_i|
```

#### Mean Squared Error (MSE)

```
MSE = (1/n) Σ(y_i - ŷ_i)²
```

#### Root Mean Squared Error (RMSE)

```
RMSE = √MSE
```

#### R² Score (Coefficient of Determination)

```
R² = 1 - (SS_res / SS_tot)
```

### 7.3 Confusion Matrix

| Actual\Predicted | Positive | Negative |
| ---------------- | -------- | -------- |
| Positive         | TP       | FN       |
| Negative         | FP       | TN       |

### 7.4 ROC and AUC

#### ROC Curve

- Plots True Positive Rate vs False Positive Rate
- Diagonal line = random classifier
- Curve closer to top-left = better classifier

#### AUC (Area Under Curve)

- AUC = 1: Perfect classifier
- AUC = 0.5: Random classifier
- AUC = 0: Worst classifier

### Python Implementation for Metrics

```python
from sklearn.metrics import (accuracy_score, precision_score, recall_score, 
                           f1_score, confusion_matrix, roc_curve, auc,
                           mean_absolute_error, mean_squared_error, r2_score)

# Classification metrics
print("=== Classification Metrics ===")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"Precision: {precision_score(y_test, y_pred):.3f}")
print(f"Recall: {recall_score(y_test, y_pred):.3f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.3f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Regression metrics (using linear regression predictions)
print("\n=== Regression Metrics ===")
print(f"MAE: {mean_absolute_error(y_test, y_pred_lr):.3f}")
print(f"MSE: {mean_squared_error(y_test, y_pred_lr):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred_lr)):.3f}")
print(f"R²: {r2_score(y_test, y_pred_lr):.3f}")

# ROC curve
y_pred_proba = log_reg.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.show()
```

---

## 8. Algorithm Comparison

| Algorithm           | Type           | Advantages                        | Disadvantages                     | Best Use Case                           |
| ------------------- | -------------- | --------------------------------- | --------------------------------- | --------------------------------------- |
| Decision Tree       | Both           | Interpretable, handles mixed data | Overfitting, unstable             | Small datasets, interpretability needed |
| KNN                 | Both           | Simple, no training phase         | Slow prediction, memory intensive | Small datasets, non-parametric          |
| SVM                 | Both           | Effective in high dimensions      | Slow training, kernel selection   | Text classification, image recognition  |
| Linear Regression   | Regression     | Simple, interpretable             | Assumes linearity                 | Linear relationships                    |
| Logistic Regression | Classification | Probabilistic output, fast        | Assumes linearity                 | Binary classification                   |

---

## 9. Real-World Applications

### Decision Trees

- Customer churn prediction
- Credit risk assessment
- Medical diagnosis
- Fraud detection

### KNN

- Recommender systems
- Image recognition
- Pattern recognition
- Anomaly detection

### SVM

- Text classification
- Face detection
- Bioinformatics
- Handwriting recognition

### Linear/Logistic Regression

- House price prediction
- Email spam filtering
- Disease prediction
- Marketing analytics

---

## 10. Terminal Learning Objectives (TLOs) Mapping

### TLO 1: Understand supervised learning concepts

- Covered in section 1

### TLO 2: Implement Decision Tree algorithm

- Covered in section 2

### TLO 3: Apply KNN algorithm

- Covered in section 3

### TLO 4: Use SVM for classification

- Covered in section 4

### TLO 5: Implement Linear and Logistic Regression

- Covered in sections 5-6

### TLO 6: Evaluate model performance

- Covered in section 7

---

## 11. Exam Questions and Practice

### Short Answer Questions

1. What is supervised learning? Give examples.
2. Explain how a decision tree works.
3. What is the difference between Gini impurity and entropy?
4. How does KNN algorithm work?
5. What is the kernel trick in SVM?
6. Explain the sigmoid function in logistic regression.
7. What is the difference between precision and recall?

### Long Answer Questions

1. Explain the decision tree algorithm with construction steps and splitting criteria.
2. Compare KNN with other classification algorithms.
3. Discuss SVM with different kernel functions and their applications.
4. Explain linear regression with cost function and gradient descent.
5. Describe logistic regression and its applications in classification.

### Practical Questions

1. Implement decision tree classification on iris dataset.
2. Apply KNN algorithm with different K values and compare results.
3. Train SVM with different kernels and evaluate performance.
4. Implement linear regression and analyze coefficients.
5. Build logistic regression model and plot ROC curve.

### Numerical Problems

1. Calculate Gini impurity for a dataset with classes [A,A,B,B,B].
2. Find Euclidean distance between points (2,3) and (5,7).
3. Calculate precision, recall, and F1-score given TP=80, FP=20, FN=10, TN=90.
4. Compute MSE for predicted values [2,4,6] and actual values [1,4,7].

---

## 12. Summary

Supervised learning algorithms form the backbone of predictive modeling. Key takeaways:

1. **Decision Trees**: Intuitive, interpretable, prone to overfitting
2. **KNN**: Simple, lazy learner, sensitive to K value and scaling
3. **SVM**: Powerful for complex boundaries, kernel trick enables non-linearity
4. **Linear Regression**: Foundation for regression, assumes linear relationships
5. **Logistic Regression**: Go-to for binary classification, provides probabilities
6. **Evaluation**: Choose metrics based on problem type and business requirements

Mastering these algorithms requires understanding their mathematical foundations, implementation details, and appropriate use cases.

---

*This completes the detailed notes for Unit IV: Supervised Learning Algorithms. These notes are aligned with MSBTE K-Scheme syllabus and designed for diploma-level understanding with practical examples and code snippets.*


---
## Unit Notes

- 📝 **Complete Unit Notes (Markdown)**
  - [View Notes](../notes/unit-04/unit-04-notes.md)
---
