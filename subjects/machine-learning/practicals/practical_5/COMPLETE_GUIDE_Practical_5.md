# Practical 5: Regression Analysis
## Complete How-To Guide

**Course:** 316316 | **Practical:** 5 of 15 | **Duration:** 2 Hours | **CO:** CO5

---

## Learning Outcomes

1. Understand regression and prediction problems
2. Implement Linear Regression
3. Implement Multiple Regression
4. Evaluate regression models using MSE, RMSE, MAE, R²
5. Handle overfitting and underfitting
6. Perform feature selection for regression
7. Create residual plots and diagnostic visualizations
8. Compare simple vs complex regression models
9. Make predictions on new data
10. Interpret regression coefficients

---

## Dataset

Using Boston Housing dataset (506 samples, 13 features, price prediction) OR custom regression dataset

---

## Step-by-Step Procedure

### Phase 1: Environment & Data Loading

```bash
source ml_env/bin/activate
cd practicals/practical_5
jupyter notebook
```

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load Boston Housing dataset (alternative: custom dataset)
from sklearn.datasets import load_boston
boston = load_boston()
X = boston.data
y = boston.target
feature_names = boston.feature_names

df = pd.DataFrame(X, columns=feature_names)
df['price'] = y

print(f"Dataset shape: {df.shape}")
print(f"\nFeature names: {list(feature_names)}")
```

---

### Phase 2: Exploratory Analysis

```python
# Statistical summary
print(df.describe())

# Correlation with target
correlation = df.corr()['price'].sort_values(ascending=False)
print("\nFeature Correlations with Price:")
print(correlation)

# Visualize relationships
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
for idx, feature in enumerate(['RM', 'LSTAT', 'AGE', 'CRIM']):
    axes[idx//2, idx%2].scatter(df[feature], df['price'], alpha=0.5)
    axes[idx//2, idx%2].set_xlabel(feature)
    axes[idx//2, idx%2].set_ylabel('Price')
    axes[idx//2, idx%2].set_title(f'{feature} vs Price')
plt.tight_layout()
plt.show()
```

---

### Phase 3: Data Preparation

```python
# Separate features and target
X = df.drop('price', axis=1)
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Training set: {X_train_scaled.shape}")
print(f"Test set: {X_test_scaled.shape}")
```

---

### Phase 4: Simple Linear Regression (Single Feature)

```python
# Select one feature (RM - rooms)
X_train_single = X_train[['RM']].values
X_test_single = X_test[['RM']].values

# Train model
lr_simple = LinearRegression()
lr_simple.fit(X_train_single, y_train)

# Predictions
y_pred_train = lr_simple.predict(X_train_single)
y_pred_test = lr_simple.predict(X_test_single)

# Evaluation
mse_train = mean_squared_error(y_train, y_pred_train)
mse_test = mean_squared_error(y_test, y_pred_test)
rmse_test = np.sqrt(mse_test)
mae_test = mean_absolute_error(y_test, y_pred_test)
r2_test = r2_score(y_test, y_pred_test)

print(f"Simple Linear Regression (RM only):")
print(f"  MSE (train): {mse_train:.4f}")
print(f"  MSE (test): {mse_test:.4f}")
print(f"  RMSE (test): {rmse_test:.4f}")
print(f"  MAE (test): {mae_test:.4f}")
print(f"  R² (test): {r2_test:.4f}")
print(f"  Coefficient: {lr_simple.coef_[0]:.4f}")
print(f"  Intercept: {lr_simple.intercept_:.4f}")
```

---

### Phase 5: Multiple Linear Regression

```python
# Train model with all features
lr_multiple = LinearRegression()
lr_multiple.fit(X_train_scaled, y_train)

# Predictions
y_pred_train_multi = lr_multiple.predict(X_train_scaled)
y_pred_test_multi = lr_multiple.predict(X_test_scaled)

# Evaluation
mse_train_multi = mean_squared_error(y_train, y_pred_train_multi)
mse_test_multi = mean_squared_error(y_test, y_pred_test_multi)
rmse_test_multi = np.sqrt(mse_test_multi)
mae_test_multi = mean_absolute_error(y_test, y_pred_test_multi)
r2_test_multi = r2_score(y_test, y_pred_test_multi)

print(f"\nMultiple Linear Regression (All Features):")
print(f"  MSE (train): {mse_train_multi:.4f}")
print(f"  MSE (test): {mse_test_multi:.4f}")
print(f"  RMSE (test): {rmse_test_multi:.4f}")
print(f"  MAE (test): {mae_test_multi:.4f}")
print(f"  R² (test): {r2_test_multi:.4f}")
```

---

### Phase 6: Feature Importance & Coefficients

```python
# Get coefficients
coefficients = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': lr_multiple.coef_
}).sort_values('Coefficient', ascending=False)

print("\nFeature Coefficients (Multiple Regression):")
print(coefficients)

# Visualize
plt.figure(figsize=(10, 6))
plt.barh(coefficients['Feature'], coefficients['Coefficient'], color='steelblue')
plt.xlabel('Coefficient Value')
plt.title('Feature Importance in Multiple Regression')
plt.tight_layout()
plt.show()
```

---

### Phase 7: Model Comparison & Diagnostics

```python
# Residual analysis
residuals_test = y_test - y_pred_test_multi

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Actual vs Predicted
axes[0, 0].scatter(y_test, y_pred_test_multi, alpha=0.5)
axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
axes[0, 0].set_xlabel('Actual Price')
axes[0, 0].set_ylabel('Predicted Price')
axes[0, 0].set_title('Actual vs Predicted')

# Residuals
axes[0, 1].scatter(y_pred_test_multi, residuals_test, alpha=0.5)
axes[0, 1].axhline(y=0, color='r', linestyle='--')
axes[0, 1].set_xlabel('Predicted Price')
axes[0, 1].set_ylabel('Residuals')
axes[0, 1].set_title('Residual Plot')

# Residuals distribution
axes[1, 0].hist(residuals_test, bins=30, edgecolor='black')
axes[1, 0].set_xlabel('Residuals')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Residuals Distribution')

# Q-Q plot
from scipy import stats
stats.probplot(residuals_test, dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('Q-Q Plot')

plt.tight_layout()
plt.show()
```

---

### Phase 8: Evaluation Summary

```python
# Comparison table
results = pd.DataFrame({
    'Model': ['Simple Regression', 'Multiple Regression'],
    'MSE (train)': [mse_train, mse_train_multi],
    'MSE (test)': [mse_test, mse_test_multi],
    'RMSE (test)': [np.sqrt(mse_test), rmse_test_multi],
    'MAE (test)': [mae_test, mae_test_multi],
    'R² (test)': [r2_test, r2_test_multi]
})

print("\n" + "="*100)
print("REGRESSION MODEL COMPARISON")
print("="*100)
print(results.to_string(index=False))
print("="*100)
```

---

## Practical Tests

```python
assert y_pred_test_multi.shape == y_test.shape
assert r2_test_multi > 0.5, "R² too low"
assert rmse_test_multi < 10, "RMSE too high"
print("✅ All Regression Tests PASSED")
```

---

## Regression Metrics Explained

```
MSE (Mean Squared Error):
  - Average of squared errors
  - Penalizes large errors
  - Units: squared target units

RMSE (Root Mean Squared Error):
  - Square root of MSE
  - Same units as target
  - Easier to interpret

MAE (Mean Absolute Error):
  - Average absolute error
  - Less sensitive to outliers than MSE
  - Same units as target

R² (Coefficient of Determination):
  - Proportion of variance explained (0-1)
  - 1 = Perfect fit
  - 0 = Model explains nothing
```

---

## Expected Results

- **Simple Regression R²:** 0.45-0.55
- **Multiple Regression R²:** 0.70-0.75
- **RMSE:** 4-6 (thousand dollars)
- **MAE:** 3-4 (thousand dollars)

---

## Submission Files

- [ ] `Practical_5_Complete_Notebook.ipynb`
- [ ] `SUBMISSION_TEMPLATE_Practical_5.md`
- [ ] Diagnostic visualizations (4 plots)

---

**Version:** 1.0 | **Course:** 316316 - Machine Learning | **Next:** Practical 6 - Clustering

