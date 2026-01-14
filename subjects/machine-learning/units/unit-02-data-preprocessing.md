---

**MindforgeAi Publications**

**Technical Publication Series**

**Chatake Innoworks Pvt. Ltd.**

**Copyright © 2025 Chatake Innoworks Pvt. Ltd.**

**Authored by: Akash Chatake**

---

# UNIT II: DATA PREPROCESSING - COMPLETE DIPLOMA NOTES
## MSBTE K-Scheme Syllabus (Course Code: 316316, Semester 6)
## Machine Learning - Detailed Theory Notes for Diploma Students

---

## 📚 Course Materials for Unit II

### 📖 Lecture Slides
**Unit II: Data Preprocessing**

<iframe src="https://gamma.app/embed/dmgcvde54l7q3sn" style="width: 700px; max-width: 100%; height: 450px" allow="fullscreen" title="Data Preprocessing"></iframe>

---

### 🎙️ Podcast: Data Preprocessing & Feature Engineering

**Episode 2: Learning from Data and Patterns**

<iframe data-testid="embed-iframe" style="border-radius:12px" src="https://open.spotify.com/embed/episode/6t5sC5yXY9OyKArTyKbCM3?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>

### 💼 Microprojects for Unit II

Complete the following hands-on projects to reinforce your learning:

1. **[Microproject 2.1: Data Cleaning Techniques](../microprojects/MICROPROJECT_2_1.md)**
   - Learn data cleaning and quality improvement
   - Duration: 1.5 weeks | Weight: 10%

2. **[Microproject 2.2: Handling Missing Data](../microprojects/MICROPROJECT_2_2.md)**
   - Master missing value treatment strategies
   - Duration: 1.5 weeks | Weight: 10%

3. **[Microproject 2.3: Dataset Splitting (Train/Test/Validation)](../microprojects/MICROPROJECT_2_3.md)**
   - Learn proper data partitioning techniques
   - Duration: 1.5 weeks | Weight: 10%

4. **[Microproject 2.4: Data Transformation & Normalization](../microprojects/MICROPROJECT_2_4.md)**
   - Apply scaling and normalization methods
   - Duration: 2 weeks | Weight: 12%

5. **[Microproject 2.5: Preprocessing Pipeline Implementation](../microprojects/MICROPROJECT_2_5.md)**
   - Build complete preprocessing workflows
   - Duration: 2 weeks | Weight: 12%

---

### 🔬 Practical Sessions for Unit II

Hands-on lab work to apply concepts:

- **[Unit II Practicals & Assignments](../practicals/overview.md)**

---

## Table of Contents
1. [Introduction to Data Preprocessing](#introduction-to-data-preprocessing)
2. [Importance of Data Preprocessing](#importance-of-data-preprocessing)
3. [Steps in Data Preprocessing](#steps-in-data-preprocessing)
4. [Handling Missing Values](#handling-missing-values)
   - 4.1 [Types of Missing Data](#types-of-missing-data)
   - 4.2 [Methods to Handle Missing Values](#methods-to-handle-missing-values)
   - 4.3 [Python Implementation](#python-implementation-missing-values)
5. [Outlier Detection and Treatment](#outlier-detection-and-treatment)
   - 5.1 [What are Outliers?](#what-are-outliers)
   - 5.2 [Detection Methods](#detection-methods)
   - 5.3 [Treatment Methods](#treatment-methods)
   - 5.4 [Python Implementation](#python-implementation-outliers)
6. [Data Normalization and Standardization](#data-normalization-and-standardization)
   - 6.1 [What is Normalization?](#what-is-normalization)
   - 6.2 [What is Standardization?](#what-is-standardization)
   - 6.3 [When to Use Which?](#when-to-use-which)
   - 6.4 [Python Implementation](#python-implementation-scaling)
7. [Encoding Categorical Variables](#encoding-categorical-variables)
   - 7.1 [Types of Categorical Data](#types-of-categorical-data)
   - 7.2 [Label Encoding](#label-encoding)
   - 7.3 [One-Hot Encoding](#one-hot-encoding)
   - 7.4 [Python Implementation](#python-implementation-encoding)
8. [Feature Scaling](#feature-scaling)
9. [Data Splitting](#data-splitting)
   - 9.1 [Train-Test Split](#train-test-split)
   - 9.2 [Cross-Validation](#cross-validation)
   - 9.3 [Python Implementation](#python-implementation-splitting)
10. [Common Mistakes in Data Preprocessing](#common-mistakes-in-data-preprocessing)
11. [Real-World Applications](#real-world-applications)
12. [Terminal Learning Objectives (TLOs) Mapping](#terminal-learning-objectives-tlos-mapping)
13. [Exam Questions and Practice](#exam-questions-and-practice)
14. [Summary](#summary)

---

## 1. Introduction to Data Preprocessing

Data preprocessing is the first and crucial step in any machine learning project. It involves transforming raw data into a clean, structured format that can be easily understood and used by machine learning algorithms.

### Definition
Data preprocessing refers to the techniques applied to raw data to make it suitable for machine learning models. It includes cleaning, normalizing, transforming, and reducing the data.

### Key Concepts
- **Raw Data**: Data collected from various sources in its original form
- **Clean Data**: Data that has been processed to remove errors, inconsistencies, and irrelevant information
- **Structured Data**: Data organized in a format suitable for analysis

### Flowchart of Data Preprocessing

```
Raw Data
    ↓
Data Collection
    ↓
Data Cleaning
    ↓
Data Integration
    ↓
Data Transformation
    ↓
Data Reduction
    ↓
Clean Data Ready for ML
```

---

## 2. Importance of Data Preprocessing

### Why is Data Preprocessing Important?

1. **Improves Model Accuracy**: Clean data leads to better model performance
2. **Reduces Training Time**: Efficient preprocessing speeds up model training
3. **Handles Real-World Data**: Real data is often messy and incomplete
4. **Prevents Overfitting**: Proper preprocessing helps in generalization
5. **Enables Feature Engineering**: Foundation for creating new features

### Real-World Example
Consider a dataset of house prices. Raw data might have:
- Missing values for some houses
- Different units (sq ft vs sq meters)
- Outliers (luxury mansions mixed with small apartments)
- Categorical data (location names)

Without preprocessing, the model cannot learn effectively.

---

## 3. Steps in Data Preprocessing

The typical steps in data preprocessing are:

1. **Data Collection**: Gathering data from various sources
2. **Data Cleaning**: Handling missing values, outliers, duplicates
3. **Data Integration**: Combining data from multiple sources
4. **Data Transformation**: Normalization, standardization, encoding
5. **Data Reduction**: Feature selection, dimensionality reduction
6. **Data Discretization**: Converting continuous to categorical data

### Detailed Flowchart

```
Start
    ↓
1. Data Collection
    ↓
2. Data Exploration (EDA)
    ↓
3. Data Cleaning
    ├── Handle Missing Values
    ├── Remove Duplicates
    └── Handle Outliers
    ↓
4. Data Transformation
    ├── Normalization/Standardization
    ├── Encoding Categorical Variables
    └── Feature Scaling
    ↓
5. Data Reduction
    ├── Feature Selection
    └── Dimensionality Reduction
    ↓
6. Data Splitting
    ├── Train-Test Split
    └── Cross-Validation
    ↓
End (Ready for Modeling)
```

---

\newpage

## 4. Handling Missing Values

Missing values are a common problem in real-world datasets. They can occur due to various reasons like data entry errors, equipment failures, or non-responses in surveys.

### 4.1 Types of Missing Data

1. **Missing Completely at Random (MCAR)**: No pattern in missing values
2. **Missing at Random (MAR)**: Missingness depends on observed data
3. **Missing Not at Random (MNAR)**: Missingness depends on unobserved data

### 4.2 Methods to Handle Missing Values

#### 1. Deletion Methods
- **Listwise Deletion**: Remove entire rows with missing values
- **Pairwise Deletion**: Use available data for each analysis

#### 2. Imputation Methods
- **Mean/Median/Mode Imputation**: Replace with central tendency
- **Forward/Backward Fill**: Use previous/next values
- **K-Nearest Neighbors (KNN) Imputation**: Use similar instances
- **Regression Imputation**: Predict missing values using regression

#### 3. Advanced Methods
- **Multiple Imputation**: Create multiple datasets with imputed values
- **Expectation-Maximization (EM)**: Statistical method for imputation

### Comparison Table

| Method | Advantages | Disadvantages | When to Use |
|--------|------------|---------------|-------------|
| Mean Imputation | Simple, fast | Reduces variance, may bias results | Numerical data, normally distributed |
| Median Imputation | Robust to outliers | May not preserve relationships | Numerical data with outliers |
| Mode Imputation | Simple for categorical | May introduce bias | Categorical data |
| KNN Imputation | Preserves relationships | Computationally expensive | Small to medium datasets |
| Deletion | Simple | Loss of information | Few missing values (<5%) |

### 4.3 Python Implementation

#### Example 1: Mean Imputation

```python
import pandas as pd
import numpy as np

# Sample data with missing values
data = {'Age': [25, 30, np.nan, 35, 40],
        'Salary': [50000, 60000, 55000, np.nan, 70000]}

df = pd.DataFrame(data)
print("Original Data:")
print(df)

# Mean imputation
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print("\nAfter Mean Imputation:")
print(df)
```

#### Example 2: KNN Imputation

```python
from sklearn.impute import KNNImputer

# Sample data
data = [[1, 2, np.nan, 3],
        [4, np.nan, 6, 5],
        [np.nan, 8, 9, 10]]

imputer = KNNImputer(n_neighbors=2)
imputed_data = imputer.fit_transform(data)

print("Original Data:")
print(np.array(data))
print("\nImputed Data:")
print(imputed_data)
```

#### Example 3: Handling Categorical Missing Values

```python
# Mode imputation for categorical data
df['Category'].fillna(df['Category'].mode()[0], inplace=True)
```

---

\newpage

## 5. Outlier Detection and Treatment

Outliers are data points that significantly differ from other observations. They can affect model performance and should be handled carefully.

### 5.1 What are Outliers?

- Data points that lie far from the central tendency
- Can be univariate (single variable) or multivariate (multiple variables)
- May represent genuine variations or measurement errors

### 5.2 Detection Methods

#### 1. Statistical Methods
- **Z-Score**: Values beyond 3 standard deviations
- **IQR Method**: Values beyond 1.5 * IQR from Q1/Q3
- **Modified Z-Score**: Robust to outliers

#### 2. Visualization Methods
- **Box Plot**: Visual representation of quartiles
- **Scatter Plot**: For bivariate outliers
- **Histogram**: Distribution analysis

#### 3. Machine Learning Methods
- **Isolation Forest**: Unsupervised algorithm
- **Local Outlier Factor (LOF)**: Density-based method

### 5.3 Treatment Methods

1. **Deletion**: Remove outlier observations
2. **Capping**: Set outliers to upper/lower bounds
3. **Transformation**: Log, square root transformations
4. **Imputation**: Replace with mean/median
5. **Separate Modeling**: Treat outliers as special cases

### 5.4 Python Implementation

#### Example 1: IQR Method for Outlier Detection

```python
import pandas as pd
import numpy as np

# Sample data
data = [10, 12, 14, 15, 16, 18, 20, 100]  # 100 is outlier
df = pd.DataFrame(data, columns=['Value'])

# Calculate Q1, Q3, IQR
Q1 = df['Value'].quantile(0.25)
Q3 = df['Value'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
print("Outliers:")
print(outliers)

# Remove outliers
df_clean = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
print("\nData after removing outliers:")
print(df_clean)
```

#### Example 2: Z-Score Method

```python
from scipy import stats

# Calculate z-scores
z_scores = stats.zscore(df['Value'])

# Identify outliers (|z| > 3)
outlier_indices = np.where(np.abs(z_scores) > 3)
print("Outlier indices:", outlier_indices[0])

# Remove outliers
df_clean = df.drop(outlier_indices[0])
```

#### Example 3: Capping Outliers

```python
# Cap outliers to upper/lower bounds
df['Value'] = np.where(df['Value'] > upper_bound, upper_bound, df['Value'])
df['Value'] = np.where(df['Value'] < lower_bound, lower_bound, df['Value'])
```

---

\newpage

## 6. Data Normalization and Standardization

These techniques bring all features to a similar scale, which is important for many machine learning algorithms.

### 6.1 What is Normalization?

Normalization scales data to a fixed range, usually [0,1].

**Formula:**
```
X_norm = (X - X_min) / (X_max - X_min)
```

**When to use:**
- When features have different units
- For algorithms like KNN, Neural Networks
- When data doesn't follow normal distribution

### 6.2 What is Standardization?

Standardization scales data to have mean 0 and standard deviation 1.

**Formula:**
```
X_std = (X - μ) / σ
```

**When to use:**
- When data follows normal distribution
- For algorithms like Linear Regression, Logistic Regression
- When features have different scales

### 6.3 When to Use Which?

| Technique | Use Case | Algorithm Examples |
|-----------|----------|-------------------|
| Normalization | Bounded data, image processing | KNN, Neural Networks |
| Standardization | Normally distributed data | Linear Regression, PCA |
| Both | Unknown distribution | SVM, Gradient Descent |

### 6.4 Python Implementation

#### Example 1: Min-Max Normalization

```python
from sklearn.preprocessing import MinMaxScaler

# Sample data
data = [[1, 2], [3, 4], [5, 6], [7, 8]]

scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(data)

print("Original Data:")
print(data)
print("\nNormalized Data:")
print(normalized_data)
```

#### Example 2: Standardization (Z-Score)

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
standardized_data = scaler.fit_transform(data)

print("Standardized Data:")
print(standardized_data)
```

#### Example 3: Manual Implementation

```python
import numpy as np

# Manual normalization
def normalize_data(X):
    X_min = np.min(X, axis=0)
    X_max = np.max(X, axis=0)
    return (X - X_min) / (X_max - X_min)

# Manual standardization
def standardize_data(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std

data = np.array([[1, 2], [3, 4], [5, 6]])
print("Normalized:", normalize_data(data))
print("Standardized:", standardize_data(data))
```

---

\newpage

## 7. Encoding Categorical Variables

Machine learning algorithms work with numerical data. Categorical variables need to be converted to numerical format.

### 7.1 Types of Categorical Data

1. **Nominal**: No order (e.g., colors: red, blue, green)
2. **Ordinal**: Has order (e.g., size: small, medium, large)

### 7.2 Label Encoding

Assigns integer values to categories.

**Example:**
- Red → 0
- Blue → 1
- Green → 2

**Limitations:**
- Implies order where none exists
- May affect algorithms that assume numerical relationships

### 7.3 One-Hot Encoding

Creates binary columns for each category.

**Example:**
For "Color" with values [Red, Blue, Green]:
- Red: [1, 0, 0]
- Blue: [0, 1, 0]
- Green: [0, 0, 1]

**Advantages:**
- No ordinal relationships assumed
- Works well with most algorithms

### 7.4 Python Implementation

#### Example 1: Label Encoding

```python
from sklearn.preprocessing import LabelEncoder

# Sample data
colors = ['Red', 'Blue', 'Green', 'Red', 'Blue']

encoder = LabelEncoder()
encoded_colors = encoder.fit_transform(colors)

print("Original:", colors)
print("Encoded:", encoded_colors)
print("Classes:", encoder.classes_)
```

#### Example 2: One-Hot Encoding

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = {'Color': ['Red', 'Blue', 'Green', 'Red'],
        'Size': ['Small', 'Medium', 'Large', 'Medium']}

df = pd.DataFrame(data)

# Using pandas get_dummies
encoded_df = pd.get_dummies(df, columns=['Color', 'Size'])
print("One-Hot Encoded Data:")
print(encoded_df)

# Using sklearn
encoder = OneHotEncoder()
encoded_array = encoder.fit_transform(df[['Color']]).toarray()
print("\nSklearn One-Hot Encoding:")
print(encoded_array)
```

#### Example 3: Ordinal Encoding

```python
from sklearn.preprocessing import OrdinalEncoder

sizes = [['Small'], ['Medium'], ['Large'], ['Small']]
ordinal_encoder = OrdinalEncoder()
encoded_sizes = ordinal_encoder.fit_transform(sizes)

print("Ordinal Encoded Sizes:", encoded_sizes.flatten())
```

---

\newpage

## 8. Feature Scaling

Feature scaling is a broader term that includes normalization and standardization. It ensures all features contribute equally to the model.

### Key Points

1. **Importance**: Prevents features with larger scales from dominating
2. **Algorithms that need scaling**: KNN, SVM, Neural Networks, PCA
3. **Algorithms that don't need scaling**: Decision Trees, Random Forest

### Additional Scaling Methods

1. **Robust Scaler**: Uses median and IQR, robust to outliers
2. **MaxAbs Scaler**: Scales by maximum absolute value
3. **Power Transformer**: Applies power transformations

### Python Implementation

```python
from sklearn.preprocessing import RobustScaler, MaxAbsScaler, PowerTransformer

# Robust Scaler
robust_scaler = RobustScaler()
robust_scaled = robust_scaler.fit_transform(data)

# MaxAbs Scaler
maxabs_scaler = MaxAbsScaler()
maxabs_scaled = maxabs_scaler.fit_transform(data)

print("Robust Scaled:", robust_scaled)
print("MaxAbs Scaled:", maxabs_scaled)
```

---

\newpage

## 9. Data Splitting

Proper data splitting ensures model evaluation is reliable and prevents overfitting.

### 9.1 Train-Test Split

- **Training Set**: Used to train the model (usually 70-80%)
- **Test Set**: Used to evaluate model performance (usually 20-30%)
- **Validation Set**: Optional, used for hyperparameter tuning

### 9.2 Cross-Validation

- **K-Fold CV**: Data divided into k folds, model trained k times
- **Stratified K-Fold**: Maintains class distribution
- **Leave-One-Out**: Each sample used as test set once

### 9.3 Python Implementation

#### Example 1: Train-Test Split

```python
from sklearn.model_selection import train_test_split

# Sample data
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training features:", X_train)
print("Test features:", X_test)
print("Training labels:", y_train)
print("Test labels:", y_test)
```

#### Example 2: K-Fold Cross-Validation

```python
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# Sample data
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [0, 0, 1, 1, 1]

# K-Fold CV
kf = KFold(n_splits=3, shuffle=True, random_state=42)
model = LogisticRegression()

scores = cross_val_score(model, X, y, cv=kf)
print("Cross-validation scores:", scores)
print("Mean CV score:", scores.mean())
```

#### Example 3: Stratified K-Fold

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf)

print("Stratified CV scores:", scores)
```

---

\newpage

## 10. Common Mistakes in Data Preprocessing

1. **Data Leakage**: Using test data information in training
2. **Over-preprocessing**: Applying unnecessary transformations
3. **Ignoring Data Types**: Treating categorical as numerical
4. **Not Handling Class Imbalance**: In classification problems
5. **Scaling Before Splitting**: Should scale after splitting
6. **Removing Outliers Blindly**: May lose important information

### Prevention Tips

- Always split data before preprocessing
- Use pipelines for consistent preprocessing
- Validate preprocessing steps
- Document all transformations

---

\newpage

## 11. Real-World Applications

### 1. Healthcare
- Preprocessing patient data for disease prediction
- Handling missing medical records
- Normalizing lab test results

### 2. Finance
- Credit scoring with mixed data types
- Fraud detection with outlier handling
- Stock price prediction with feature scaling

### 3. E-commerce
- Customer segmentation with categorical encoding
- Recommendation systems with data normalization
- Sales forecasting with time series preprocessing

### 4. Image Processing
- Pixel normalization for computer vision
- Data augmentation for training
- Feature extraction preprocessing

---

\newpage

## 12. Terminal Learning Objectives (TLOs) Mapping

### TLO 1: Understand data preprocessing concepts
- Covered in sections 1-3

### TLO 2: Handle missing values and outliers
- Covered in sections 4-5

### TLO 3: Apply normalization and standardization
- Covered in section 6

### TLO 4: Encode categorical variables
- Covered in section 7

### TLO 5: Perform data splitting and validation
- Covered in section 9

---

\newpage

## 13. Exam Questions and Practice

### Short Answer Questions

1. What is data preprocessing? Why is it important?
2. Explain the difference between normalization and standardization.
3. What are the methods to handle missing values?
4. Describe one-hot encoding with an example.
5. What is cross-validation and why is it used?

### Long Answer Questions

1. Explain the complete data preprocessing pipeline with examples.
2. Compare different methods for outlier detection and treatment.
3. Discuss the importance of feature scaling in machine learning algorithms.
4. Explain different techniques for encoding categorical variables.

### Practical Questions

1. Write Python code to handle missing values in a dataset using mean imputation.
2. Implement min-max normalization on a given dataset.
3. Perform train-test split on a dataset and explain the importance.
4. Apply one-hot encoding to categorical variables in a DataFrame.

### Numerical Problems

1. Given data [10, 20, 30, 40, 50], calculate normalized values.
2. For data with mean 50 and std 10, calculate standardized values.
3. Calculate IQR and identify outliers in a dataset.

---

\newpage

## 14. Summary

Data preprocessing is the foundation of successful machine learning projects. Key takeaways:

1. **Always preprocess data** before feeding to ML algorithms
2. **Handle missing values** appropriately based on data type and pattern
3. **Detect and treat outliers** carefully to avoid losing information
4. **Scale features** when using distance-based algorithms
5. **Encode categorical variables** properly
6. **Split data correctly** to prevent data leakage
7. **Use cross-validation** for reliable model evaluation

Mastering these techniques will significantly improve your machine learning model performance and make you ready for real-world applications.

---

*This completes the detailed notes for Unit II: Data Preprocessing. These notes are aligned with MSBTE K-Scheme syllabus and designed for diploma-level understanding with practical examples and code snippets.*