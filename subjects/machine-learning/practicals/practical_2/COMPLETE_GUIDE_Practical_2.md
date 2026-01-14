# Practical 2: Data Preprocessing
## Complete How-To Guide

**Course:** 316316 - Machine Learning  
**Practical Number:** 2 of 15  
**Duration:** 2 Hours  
**Prerequisites:** Practical 1 (Installation) MUST be completed  
**CO (Course Outcome):** CO2 - Apply preprocessing techniques on datasets to clean and transform data

---

## Table of Contents

1. [Learning Outcomes](#learning-outcomes)
2. [Pre-Practical Requirements](#pre-practical-requirements)
3. [Step-by-Step Procedure](#step-by-step-procedure)
4. [Practical Tests](#practical-tests)
5. [Expected Results](#expected-results)
6. [Troubleshooting](#troubleshooting)
7. [Code Explanations](#code-explanations)
8. [Key Concepts](#key-concepts)
9. [Submission Requirements](#submission-requirements)
10. [Additional Resources](#additional-resources)

---

## Learning Outcomes

After completing this practical, you will be able to:

1. **LO1:** Identify different types of data quality issues (missing values, duplicates, outliers, inconsistencies)
2. **LO2:** Handle missing values using various strategies (deletion, imputation, forward-fill)
3. **LO3:** Detect and treat outliers using statistical methods (IQR, Z-score)
4. **LO4:** Normalize and scale numerical features using StandardScaler and MinMaxScaler
5. **LO5:** Encode categorical variables using One-Hot Encoding and Label Encoding
6. **LO6:** Transform data distributions using Log transformation and Box-Cox transformation
7. **LO7:** Handle imbalanced datasets using resampling techniques
8. **LO8:** Create preprocessing pipelines using scikit-learn Pipeline
9. **LO9:** Validate preprocessing quality and measure data quality improvements
10. **LO10:** Document preprocessing steps and create reproducible preprocessing workflows

---

## Pre-Practical Requirements

### System Requirements
- **OS:** Windows 10+, macOS 10.14+, or Ubuntu 18.04+
- **RAM:** Minimum 4 GB (8 GB recommended)
- **Disk Space:** 2 GB free
- **Python Version:** 3.9 or higher

### Software Prerequisites
- Python 3.9+ installed and configured
- Virtual environment created (from Practical 1)
- All ML libraries installed: NumPy, Pandas, Matplotlib, Scikit-learn
- Jupyter Notebook installed and working

### Knowledge Prerequisites
- Completed Practical 1 (Installation)
- Basic Python programming knowledge
- Understanding of NumPy arrays and Pandas DataFrames
- Familiarity with basic statistics (mean, median, std, quartiles)

### Time Required
- **Minimum:** 1.5 hours
- **Recommended:** 2-3 hours (including experimentation)

### Files You Will Need
- Sample dataset: `house_price_raw_data.csv` (provided in practical_2 folder)
- OR download from: https://github.com/yourrepo/sample-datasets

---

## Step-by-Step Procedure

### Phase 1: Activate Environment & Set Up Workspace

**Step 1.1:** Open Terminal/Command Prompt and navigate to your ML course folder

```bash
# macOS/Linux
cd ~/ml_course
source ml_env/bin/activate

# Windows
cd C:\Users\YourName\ml_course
ml_env\Scripts\activate
```

**Step 1.2:** Verify activation (you should see `(ml_env)` in terminal)

```bash
python --version
pip list | grep pandas
```

**Step 1.3:** Create practical_2 workspace

```bash
mkdir -p practicals/practical_2/data
mkdir -p practicals/practical_2/notebooks
mkdir -p practicals/practical_2/scripts
cd practicals/practical_2
```

**Step 1.4:** Start Jupyter Notebook

```bash
jupyter notebook
```

This will open http://localhost:8888 in your browser.

---

### Phase 2: Load and Explore Raw Data

**Step 2.1:** Create a new notebook file called `Practical_2_Data_Preprocessing.ipynb`

**Step 2.2:** In the first code cell, import required libraries

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import warnings
warnings.filterwarnings('ignore')

print("✅ All libraries imported successfully!")
```

**Step 2.3:** Load the raw dataset

```python
# Load the raw data
df_raw = pd.read_csv('house_price_raw_data.csv')

# Display basic information
print("Dataset Shape:", df_raw.shape)
print("\nFirst 5 rows:")
print(df_raw.head())
print("\nData Types:")
print(df_raw.dtypes)
print("\nDataset Info:")
print(df_raw.info())
```

**Step 2.4:** Analyze data quality issues

```python
# Check for missing values
print("Missing Values:")
print(df_raw.isnull().sum())
print("\nMissing Values Percentage:")
print((df_raw.isnull().sum() / len(df_raw) * 100).round(2))

# Check for duplicates
print(f"\nDuplicate Rows: {df_raw.duplicated().sum()}")

# Check for outliers (statistical summary)
print("\nStatistical Summary:")
print(df_raw.describe())
```

---

### Phase 3: Data Cleaning & Preprocessing

**Step 3.1:** Handle missing values

```python
# Method 1: Drop rows with missing values (CAUTIOUS - loss of data)
# df_cleaned = df_raw.dropna()

# Method 2: Drop rows if missing in critical columns
df_cleaned = df_raw.dropna(subset=['price', 'square_feet'])

# Method 3: Impute missing values
imputer = SimpleImputer(strategy='mean')  # For numerical
numerical_cols = df_raw.select_dtypes(include=[np.number]).columns
df_cleaned[numerical_cols] = imputer.fit_transform(df_cleaned[numerical_cols])

# Method 4: Forward fill (for time series)
# df_cleaned = df_cleaned.fillna(method='ffill')

print(f"Cleaned dataset shape: {df_cleaned.shape}")
print(f"Remaining missing values: {df_cleaned.isnull().sum().sum()}")
```

**Step 3.2:** Remove duplicates

```python
# Identify duplicates
duplicates = df_cleaned.duplicated()
print(f"Duplicate rows found: {duplicates.sum()}")

# Remove duplicates
df_cleaned = df_cleaned.drop_duplicates()
print(f"Dataset shape after removing duplicates: {df_cleaned.shape}")
```

**Step 3.3:** Detect and treat outliers

```python
# Method 1: IQR (Interquartile Range) Method
def remove_outliers_iqr(data, column, multiplier=1.5):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    return data[(data[column] >= lower_bound) & (data[column] <= upper_bound)]

# Method 2: Z-Score Method
def remove_outliers_zscore(data, column, threshold=3):
    z_scores = np.abs((data[column] - data[column].mean()) / data[column].std())
    return data[z_scores < threshold]

# Apply outlier treatment
outliers_before = len(df_cleaned)
df_cleaned = remove_outliers_iqr(df_cleaned, 'price', multiplier=1.5)
outliers_removed = outliers_before - len(df_cleaned)
print(f"Outliers removed: {outliers_removed}")
```

**Step 3.4:** Handle inconsistent data

```python
# Convert data types
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'], errors='coerce')

# Standardize categorical values
if 'city' in df_cleaned.columns:
    df_cleaned['city'] = df_cleaned['city'].str.lower().str.strip()

# Remove invalid rows after conversion
df_cleaned = df_cleaned.dropna(subset=['date'])

print("Data consistency check completed!")
```

---

### Phase 4: Feature Scaling & Normalization

**Step 4.1:** Identify numerical and categorical columns

```python
numerical_features = df_cleaned.select_dtypes(include=[np.number]).columns.tolist()
categorical_features = df_cleaned.select_dtypes(include=['object']).columns.tolist()

print(f"Numerical features: {numerical_features}")
print(f"Categorical features: {categorical_features}")
```

**Step 4.2:** Scale numerical features

```python
# StandardScaler (mean=0, std=1) - Good for normal distribution
scaler_standard = StandardScaler()
df_scaled_standard = df_cleaned.copy()
df_scaled_standard[numerical_features] = scaler_standard.fit_transform(
    df_cleaned[numerical_features]
)

print("StandardScaler Applied:")
print(df_scaled_standard[numerical_features].describe())

# MinMaxScaler (range 0-1) - Good for bounded ranges
scaler_minmax = MinMaxScaler()
df_scaled_minmax = df_cleaned.copy()
df_scaled_minmax[numerical_features] = scaler_minmax.fit_transform(
    df_cleaned[numerical_features]
)

print("\nMinMaxScaler Applied (sample):")
print(df_scaled_minmax[numerical_features].head())
```

**Step 4.3:** Encode categorical features

```python
# Label Encoding (for ordinal categories)
label_encoders = {}
df_encoded = df_cleaned.copy()

for col in categorical_features:
    le = LabelEncoder()
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
    label_encoders[col] = le
    print(f"Label Encoded {col}:")
    for i, label in enumerate(le.classes_):
        print(f"  {label} → {i}")

# One-Hot Encoding (for nominal categories - creates dummy variables)
df_onehot = pd.get_dummies(df_cleaned, columns=categorical_features, drop_first=True)
print(f"\nShape after One-Hot Encoding: {df_onehot.shape}")
```

---

### Phase 5: Data Transformation

**Step 5.1:** Apply log transformation (for skewed data)

```python
# Check skewness before transformation
print("Skewness before transformation:")
for col in numerical_features:
    skewness = df_cleaned[col].skew()
    print(f"  {col}: {skewness:.3f}")

# Apply log transformation to right-skewed columns
df_transformed = df_cleaned.copy()
for col in numerical_features:
    if df_transformed[col].min() > 0:  # Log only works for positive values
        skewness = df_transformed[col].skew()
        if skewness > 1:  # Right-skewed
            df_transformed[col + '_log'] = np.log(df_transformed[col])

print("\nLog transformation applied!")
```

**Step 5.2:** Box-Cox transformation (advanced)

```python
from scipy.stats import boxcox

# Box-Cox requires positive values
df_boxcox = df_cleaned.copy()
for col in numerical_features:
    if df_boxcox[col].min() > 0:
        df_boxcox[col + '_boxcox'], lambda_param = boxcox(df_boxcox[col])
        print(f"Box-Cox applied to {col} (λ={lambda_param:.3f})")
```

---

### Phase 6: Create Preprocessing Pipeline

**Step 6.1:** Define preprocessing pipeline

```python
# Create column transformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)

# Create complete pipeline
preprocessing_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])

print("Preprocessing pipeline created!")
```

**Step 6.2:** Apply pipeline

```python
# Fit and transform data
X_processed = preprocessing_pipeline.fit_transform(df_cleaned)

# Convert back to DataFrame
feature_names = (
    numerical_features + 
    list(preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features))
)
df_pipeline = pd.DataFrame(X_processed, columns=feature_names)

print(f"Processed dataset shape: {df_pipeline.shape}")
print("\nFirst 5 rows of processed data:")
print(df_pipeline.head())
```

---

### Phase 7: Quality Validation & Visualization

**Step 7.1:** Compare before and after preprocessing

```python
# Create comparison visualization
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Distribution before preprocessing
axes[0, 0].hist(df_cleaned['price'], bins=30, color='red', alpha=0.7, edgecolor='black')
axes[0, 0].set_title('Price Distribution - BEFORE Preprocessing')
axes[0, 0].set_xlabel('Price')
axes[0, 0].set_ylabel('Frequency')

# Distribution after scaling
axes[0, 1].hist(df_scaled_standard['price'], bins=30, color='green', alpha=0.7, edgecolor='black')
axes[0, 1].set_title('Price Distribution - AFTER Scaling')
axes[0, 1].set_xlabel('Scaled Price (StandardScaler)')
axes[0, 1].set_ylabel('Frequency')

# Box plot before
axes[1, 0].boxplot(df_cleaned[numerical_features], labels=numerical_features)
axes[1, 0].set_title('Numerical Features - BEFORE Preprocessing')
axes[1, 0].tick_params(axis='x', rotation=45)

# Box plot after
axes[1, 1].boxplot(df_scaled_standard[numerical_features], labels=numerical_features)
axes[1, 1].set_title('Numerical Features - AFTER Scaling')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
```

**Step 7.2:** Validate data quality improvements

```python
# Create quality report
print("=" * 60)
print("DATA QUALITY REPORT - BEFORE vs AFTER")
print("=" * 60)

print(f"\nOriginal Dataset:")
print(f"  Shape: {df_raw.shape}")
print(f"  Missing Values: {df_raw.isnull().sum().sum()}")
print(f"  Duplicates: {df_raw.duplicated().sum()}")
print(f"  Memory Usage: {df_raw.memory_usage(deep=True).sum() / 1024:.2f} KB")

print(f"\nCleaned Dataset:")
print(f"  Shape: {df_cleaned.shape}")
print(f"  Missing Values: {df_cleaned.isnull().sum().sum()}")
print(f"  Duplicates: {df_cleaned.duplicated().sum()}")
print(f"  Memory Usage: {df_cleaned.memory_usage(deep=True).sum() / 1024:.2f} KB")

print(f"\nPreprocessed Dataset:")
print(f"  Shape: {df_pipeline.shape}")
print(f"  Missing Values: {df_pipeline.isnull().sum().sum()}")
print(f"  Data Type: Numerical (standardized)")

print("\n" + "=" * 60)
```

---

### Phase 8: Save Processed Data

**Step 8.1:** Save cleaned and preprocessed datasets

```python
# Save cleaned data
df_cleaned.to_csv('house_price_cleaned.csv', index=False)
print("✅ Cleaned dataset saved: house_price_cleaned.csv")

# Save preprocessed data
df_pipeline.to_csv('house_price_preprocessed.csv', index=False)
print("✅ Preprocessed dataset saved: house_price_preprocessed.csv")

# Save preprocessing objects for future use
import pickle
with open('preprocessing_pipeline.pkl', 'wb') as f:
    pickle.dump(preprocessing_pipeline, f)
print("✅ Pipeline saved: preprocessing_pipeline.pkl")
```

---

## Practical Tests

### Test 1: Data Loading & Exploration
```python
# EXPECTED: Dataset loads, shape displays, info shown
assert df_raw.shape[0] > 0, "No data loaded!"
assert df_raw.shape[1] > 0, "No features found!"
print("✅ Test 1 PASSED: Data loading successful")
```

### Test 2: Missing Value Handling
```python
# EXPECTED: Missing values reduced to 0 or acceptable level
missing_after = df_cleaned.isnull().sum().sum()
assert missing_after == 0, f"Still {missing_after} missing values!"
print("✅ Test 2 PASSED: Missing values handled")
```

### Test 3: Outlier Detection
```python
# EXPECTED: Outliers identified and removed
print(f"✅ Test 3 PASSED: {outliers_removed} outliers removed")
```

### Test 4: Feature Scaling
```python
# EXPECTED: Scaled features have mean ≈ 0, std ≈ 1
for col in numerical_features:
    mean = df_scaled_standard[col].mean()
    std = df_scaled_standard[col].std()
    assert abs(mean) < 1e-10, f"{col} mean not 0!"
    assert abs(std - 1) < 1e-10, f"{col} std not 1!"
print("✅ Test 4 PASSED: Feature scaling verified")
```

### Test 5: Categorical Encoding
```python
# EXPECTED: No object/categorical dtypes remain
assert df_pipeline.dtypes.unique()[0] == np.float64, "Not all columns numeric!"
print("✅ Test 5 PASSED: Categorical encoding successful")
```

---

## Expected Results

### Data Quality Metrics

| Metric | Before | After | Status |
|--------|--------|-------|--------|
| Total Rows | 300 | 285 | ✅ Cleaned |
| Missing Values | 45 | 0 | ✅ Handled |
| Duplicates | 12 | 0 | ✅ Removed |
| Outliers | ~24 | 0 | ✅ Treated |
| Numerical Features | Scaled: No | Yes | ✅ Scaled |
| Categorical Features | Encoded: No | Yes | ✅ Encoded |

### Console Output Expected

```
✅ All libraries imported successfully!

Dataset Shape: (300, 8)

Missing Values:
price       15
square_feet  10
rooms        20
age          0
city         0
...

Outliers removed: 24

✅ Test 1 PASSED: Data loading successful
✅ Test 2 PASSED: Missing values handled
✅ Test 3 PASSED: Outliers detected and removed
✅ Test 4 PASSED: Feature scaling verified
✅ Test 5 PASSED: Categorical encoding successful
```

---

## Troubleshooting

### Issue 1: "No module named 'pandas'" or "No module named 'sklearn'"
**Solution:**
```bash
# Activate your virtual environment
source ml_env/bin/activate  # macOS/Linux
# or
ml_env\Scripts\activate  # Windows

# Install missing packages
pip install pandas scikit-learn
```

### Issue 2: "ModuleNotFoundError: No module named 'scipy'"
**Solution:**
```bash
pip install scipy
```

### Issue 3: Dataset file not found
**Solution:**
- Ensure CSV file is in the same directory as your notebook
- Use absolute path: `pd.read_csv('/full/path/to/house_price_raw_data.csv')`
- Check current working directory: `import os; print(os.getcwd())`

### Issue 4: "SettingWithCopyWarning" warning
**Solution:**
```python
# Add this at the top of your notebook
import warnings
warnings.filterwarnings('ignore')
```

### Issue 5: Memory error with large datasets
**Solution:**
```python
# Load data in chunks
chunk_size = 10000
chunks = []
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    chunks.append(chunk)
df = pd.concat(chunks, ignore_index=True)
```

### Issue 6: ValueError in preprocessing pipeline
**Solution:**
- Check that all features are numeric or properly encoded
- Verify column names match between fit and transform
- Use `df.info()` to check data types

---

## Code Explanations

### Understanding Missing Value Strategies

```python
# STRATEGY 1: Delete rows (df.dropna())
# ❌ PRO: Simple, removes uncertainty
# ❌ CON: Loss of data, may reduce model performance
df_deleted = df.dropna()

# STRATEGY 2: Mean/Median Imputation
# ✅ PRO: Preserves data count, works for MCAR data
# ❌ CON: Reduces variance, doesn't handle MNAR well
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
df_imputed = imputer.fit_transform(df[numeric_cols])

# STRATEGY 3: Forward Fill (time series)
# ✅ PRO: Preserves temporal patterns
# ❌ CON: Only for time-ordered data
df_filled = df.fillna(method='ffill')

# STRATEGY 4: KNN Imputation (uses nearby values)
# ✅ PRO: Context-aware imputation
# ❌ CON: Computationally expensive
from sklearn.impute import KNNImputer
imputer_knn = KNNImputer(n_neighbors=5)
```

### Understanding Scaling Methods

```
STANDARDIZATION (StandardScaler):
Formula: X_new = (X - mean) / std
Range: -∞ to +∞ (usually -3 to +3)
Use When: Data normally distributed, using algorithms like Linear Regression, SVM
Visual:
  Before: [1, 2, 3, 4, 5, 100]
  After:  [-1.2, -0.9, -0.6, -0.3, 0, 2.4]

NORMALIZATION (MinMaxScaler):
Formula: X_new = (X - min) / (max - min)
Range: Always 0 to 1
Use When: Data not normally distributed, bounded ranges needed
Visual:
  Before: [1, 2, 3, 4, 5, 100]
  After:  [0, 0.04, 0.08, 0.12, 0.16, 1]
```

### Understanding Encoding Methods

```python
LABEL ENCODING (for ordinal data):
Original: ['low', 'medium', 'high']
Encoded:  [0, 1, 2]
✅ Use for: Tree-based models, ordinal relationships
❌ Avoid for: Linear models (implies ordering)

ONE-HOT ENCODING (for nominal data):
Original: ['red', 'blue', 'green']
Encoded:
  red:   [1, 0, 0]
  blue:  [0, 1, 0]
  green: [0, 0, 1]
✅ Use for: Nominal categories, linear models
❌ Avoid for: Tree-based models (curse of dimensionality)
```

---

## Key Concepts

### Data Quality Dimensions

1. **Completeness:** % of non-null values
   - Target: >95% complete
   - Handle: Delete or impute

2. **Accuracy:** Correctness of values
   - Check: Domain ranges, logical relationships
   - Handle: Validate, correct, delete

3. **Consistency:** Uniform representation
   - Check: Data types, units, formats
   - Handle: Standardize

4. **Uniqueness:** No unintended duplicates
   - Check: Identify duplicates
   - Handle: Remove or flag

5. **Timeliness:** Currency of data
   - Check: Date ranges
   - Handle: May need temporal handling

### Types of Missing Data

- **MCAR (Missing Completely At Random):** Mechanism unrelated to data → Safe to delete or impute
- **MAR (Missing At Random):** Mechanism related to other observed variables → Imputation preferred
- **MNAR (Missing Not At Random):** Mechanism depends on unobserved values → Complex handling needed

### Outlier Detection Methods

```
IQR METHOD:
- Q1 = 25th percentile
- Q3 = 75th percentile
- IQR = Q3 - Q1
- Lower bound = Q1 - 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR
- Outliers: Values < lower or > upper

Z-SCORE METHOD:
- Z = (X - mean) / std
- Threshold: |Z| > 3
- More sensitive than IQR
- Assumes normal distribution
```

---

## Submission Requirements

Your submission must include:

### Format A: Jupyter Notebook
1. **Student Details** (Markdown cell)
2. **Learning Outcomes Checklist** (Markdown cell)
3. **Environment Setup** (Code cell with imports)
4. **Phase 1-3: Data Loading & Cleaning** (Code cells)
5. **Phase 4-5: Scaling & Encoding** (Code cells)
6. **Phase 6: Pipeline** (Code cells)
7. **Phase 7: Validation** (Code cells with visualizations)
8. **Results Summary** (Markdown + Code)
9. **Reflections & Learnings** (Markdown cell)
10. **Submission Checklist** (Markdown cell)

### Format B: PDF Report
1. Title page (Course, Practical, Student info)
2. Objective & Theory (1-2 pages)
3. Procedure & Steps Followed (3-4 pages with screenshots)
4. Results & Output (2-3 pages with visualizations)
5. Troubleshooting Faced (1 page)
6. Conclusions & Learning Outcomes (1 page)
7. Appendix (Code listings)

### Files to Submit
- ☐ `Practical_2_Data_Preprocessing.ipynb`
- ☐ `house_price_cleaned.csv`
- ☐ `house_price_preprocessed.csv`
- ☐ `SUBMISSION_TEMPLATE_Practical_2.md` (filled)
- ☐ `preprocessing_pipeline.pkl` (serialized pipeline)
- ☐ Screenshots of output (3-4 images)

---

## Additional Resources

### Official Documentation
- Pandas Documentation: https://pandas.pydata.org/docs/
- Scikit-learn Preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- NumPy Missing Data: https://numpy.org/doc/stable/reference/generated/numpy.nan.html

### Tutorials & Guides
- Data Cleaning with Pandas: https://www.youtube.com/watch?v=XR_4qb8FAkU
- Feature Scaling in ML: https://www.youtube.com/watch?v=_Iq6x7EjkXs
- Handling Outliers: https://towardsdatascience.com/outlier-detection-and-removal-in-machine-learning-c86a0e20bb3f

### Sample Datasets
- Kaggle Datasets: https://www.kaggle.com/datasets
- UCI Machine Learning: https://archive.ics.uci.edu/ml/
- Government Data: https://data.gov.in

---

## Common Pitfalls to Avoid

1. ❌ **Fitting scalers/encoders on entire dataset including test set** 
   → ✅ Always fit on training data only, transform test data

2. ❌ **Applying transformations before train-test split**
   → ✅ Split first, then fit and transform on training data

3. ❌ **Deleting too many rows due to missing values**
   → ✅ Use imputation if <30% missing

4. ❌ **Encoding target variable the same as features**
   → ✅ Keep target variable separate from feature engineering

5. ❌ **Not removing outliers in some cases, creating biased models**
   → ✅ Carefully analyze outliers - some may be legitimate

6. ❌ **Forgetting to handle test data with saved pipeline**
   → ✅ Always save and reuse preprocessing pipeline for prediction

---

## Quick Reference Commands

```python
# Data Exploration
df.head()                              # First 5 rows
df.info()                              # Data types & non-null counts
df.describe()                          # Statistical summary
df.isnull().sum()                      # Missing values count
df.duplicated().sum()                  # Duplicate rows count

# Handling Missing Values
df.dropna()                            # Drop rows with NaN
df.fillna(value)                       # Fill with value
df.fillna(method='ffill')              # Forward fill
SimpleImputer(strategy='mean')         # Statistical imputation

# Outlier Detection
df[col].quantile(0.25)                 # Q1
df[col].quantile(0.75)                 # Q3
(df[col] - df[col].mean()) / df[col].std()  # Z-score

# Scaling
StandardScaler()                       # Mean 0, std 1
MinMaxScaler()                         # Range 0-1

# Encoding
LabelEncoder()                         # Ordinal encoding
OneHotEncoder()                        # Nominal encoding
pd.get_dummies()                       # Quick one-hot encoding

# Pipeline
Pipeline([('step1', transformer1), ('step2', transformer2)])
ColumnTransformer(transformers=[...]) # Apply different transformers
```

---

**Version:** 1.0  
**Last Updated:** December 2025  
**Course:** 316316 - Machine Learning  
**Practical:** 2 of 15  

---

**Next Practical:** Practical 3 - Reading Datasets (CSV, JSON, XML, Excel, SQL)

