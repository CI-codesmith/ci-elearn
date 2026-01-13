# MICROPROJECT 2.1: Dataset Collection and Basic Cleaning (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 2 (Data Preparation)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + CSV + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to clean a dataset and handle missing values using pandas. Practice basic techniques for preparing data for ML.

---

## 📋 Requirements

### Task 1: Data Cleaning
- Load a small dataset (e.g., Titanic, Iris, or any CSV)
- Identify and remove duplicate rows
- Check for and correct data types (e.g., convert strings to numbers)

### Task 2: Handling Missing Values
- Find missing values in the dataset
- Show how to fill missing values (mean, median, mode) or drop them
- Explain your choices in markdown

### Task 3: Save Cleaned Data
- Save the cleaned dataset as a new CSV file

---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Cleaned CSV file
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP2_1_Group[ID]_Regression.ipynb`
- **Sections:** Data loading → Preprocessing → Modeling → Evaluation → Conclusions

### 2. Trained Models (20% weight)
- **Files:** `best_model.pkl` (using joblib)
- **Include:** Model, scaler, feature selector if used

### 3. Group Report (20% weight)
- **File:** `MP2_1_Group[ID]_Report.pdf`
- **Content:** Model comparison, best model analysis, business insights

### 4. Presentation (10% weight)
- **File:** `MP2_1_Group[ID]_Presentation.pdf`
- **Content:** 5-7 slides summarizing approach and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Preprocessing** | Complete pipeline, handles all data issues | Good preprocessing, minor gaps | Basic preprocessing | Poor/inadequate |
| **Model Implementation** | 4+ models, proper tuning | 4 models, basic tuning | 3 models, minimal tuning | 1-2 models or broken |
| **Evaluation Metrics** | Comprehensive metrics, proper interpretation | Good metrics coverage | Basic metrics only | Incorrect metrics |
| **Model Comparison** | Detailed comparison, clear winner selection | Good comparison | Basic comparison | No comparison |
| **Code Quality** | Clean, modular, well-documented | Mostly clean | Functional | Messy/broken |
| **Report Quality** | Excellent analysis, insights | Good analysis | Basic summary | Poor documentation |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group (includes peer evaluation)

---

## 📝 Template Code

```python
# MICROPROJECT 2.1: Regression Modeling
# Group: [ID]
# Dataset: [Chosen]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 1. DATA LOADING
# df = pd.read_csv('housing.csv')

# 2. PREPROCESSING
# Handle missing values, encode categorical, scale features

# 3. TRAIN/TEST SPLIT
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. MODEL TRAINING
models = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(alpha=1.0),
    'Lasso Regression': Lasso(alpha=0.1),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    # Train model
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Metrics
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results[name] = {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R²': r2,
        'model': model
    }
    
    print(f"{name}:")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  R²: {r2:.4f}")
    print()

# 5. MODEL COMPARISON VISUALIZATION
model_names = list(results.keys())
r2_scores = [results[name]['R²'] for name in model_names]
rmse_scores = [results[name]['RMSE'] for name in model_names]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(model_names, r2_scores, color='skyblue')
ax1.set_title('R² Scores by Model')
ax1.set_ylabel('R² Score')
ax1.tick_params(axis='x', rotation=45)

ax2.bar(model_names, rmse_scores, color='lightcoral')
ax2.set_title('RMSE by Model')
ax2.set_ylabel('RMSE')
ax2.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('model_comparison.png')
plt.show()

# 6. BEST MODEL ANALYSIS
best_model_name = max(results.keys(), key=lambda x: results[x]['R²'])
best_model = results[best_model_name]['model']

print(f"Best Model: {best_model_name}")
print(f"R² Score: {results[best_model_name]['R²']:.4f}")

# Feature importance (for Random Forest)
if hasattr(best_model, 'feature_importances_'):
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': best_model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=feature_importance.head(10))
    plt.title('Top 10 Feature Importances')
    plt.savefig('feature_importance.png')
    plt.show()

# 7. SAVE BEST MODEL
joblib.dump(best_model, 'best_regression_model.pkl')
print("Best model saved as 'best_regression_model.pkl'")
```

---

## 🆘 Resources
- Scikit-learn regression guide
- Kaggle housing price competitions
- Course practicals 4-5 reference

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_2_1.md