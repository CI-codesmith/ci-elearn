# Practical 5: Regression Algorithms
## Submission Template

**Course:** 316316 - Machine Learning  
**Practical Number:** 5 of 15  
**Academic Year:** 2025-2026

---

## Student Information

| Field | Value |
|-------|-------|
| Student Name | [Your Name] |
| Roll Number | [Your Roll Number] |
| College | [Your College] |
| Date | [DD/MM/YYYY] |

---

## Learning Outcomes Achievement

| LO | Outcome | Status |
|----|---------|--------|
| 1 | Linear Regression Theory | ☐ Yes |
| 2 | Simple Regression | ☐ Yes |
| 3 | Multiple Regression | ☐ Yes |
| 4 | Coefficient Analysis | ☐ Yes |
| 5 | Evaluation Metrics | ☐ Yes |
| 6 | Residual Analysis | ☐ Yes |
| 7 | Overfitting Detection | ☐ Yes |
| 8 | Feature Scaling | ☐ Yes |
| 9 | Visualization | ☐ Yes |
| 10 | Model Comparison | ☐ Yes |

---

## Test Results

| Test | Result | Details |
|------|--------|---------|
| 1: Data Prep | ✅ PASSED | Train: [__], Test: [__] |
| 2: Simple Regression | ✅ PASSED | R²: [__] |
| 3: Multiple Regression | ✅ PASSED | R²: [__] |
| 4: Metrics | ✅ PASSED | All valid |
| 5: Residuals | ✅ PASSED | Mean ≈ 0 |

**Score: 5/5 PASSED ✅**

---

## Performance Summary

### Simple Linear Regression
- **Feature:** BMI
- **MSE:** [__]
- **RMSE:** [__]
- **MAE:** [__]
- **R² Score:** [__]

### Multiple Linear Regression
- **Features:** All 10
- **MSE:** [__]
- **RMSE:** [__]
- **MAE:** [__]
- **R² Score:** [__]

### Improvement
- **R² Gain:** [__]%
- **RMSE Reduction:** [__]%

---

## Evaluation Metrics

### Key Metrics Explained

**MSE (Mean Squared Error)**
- Penalizes large errors more
- Formula: Σ(yi - ŷi)² / n

**RMSE (Root Mean Squared Error)**
- Same units as target
- Better interpretability
- Formula: √MSE

**MAE (Mean Absolute Error)**
- Average absolute error
- Robust to outliers
- Formula: Σ|yi - ŷi| / n

**R² Score**
- Proportion of variance explained
- Range: 0 to 1 (higher is better)
- Formula: 1 - (SS_res / SS_tot)

---

## Residual Diagnostics

### Residual Statistics
- Mean: [__] (should be ≈ 0)
- Std Dev: [__]
- Min: [__]
- Max: [__]

### Normality Test
- Shapiro-Wilk p-value: [__]
- Normal Distribution: [Yes/No]

### Fit Status
- Overfitting: [Yes/No]
- Underfitting: [Yes/No]
- Overall: [Good/Fair/Poor]

---

## Feature Coefficients

| Feature | Coefficient | Interpretation |
|---------|-------------|-----------------|
| [Feat1] | [__] | [+/- influence] |
| [Feat2] | [__] | [+/- influence] |
| [Feat3] | [__] | [+/- influence] |
| ... | ... | ... |

---

## Key Findings

### Simple vs Multiple Regression
- Multiple regression performs better
- Improvement in R²: [__]%
- Additional features help

### Feature Importance
- Most important: [Feature name]
- Least important: [Feature name]

### Model Quality
- Training R²: [__]
- Testing R²: [__]
- Generalization: [Good/Fair/Poor]

---

## Code Summary

### Simple Regression
```python
simple_model = LinearRegression()
simple_model.fit(X_train_simple, y_train)
predictions = simple_model.predict(X_test_simple)
```

### Multiple Regression
```python
model = LinearRegression()
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)
```

### Metrics Calculation
```python
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## Troubleshooting

### Issue 1: [If encountered]
**Problem:** [Description]
**Solution:** [Your fix]
**Status:** ✅ Resolved

---

## Conclusions

### Learning Summary
1. Linear regression works well for [dataset]
2. Multiple features improve model
3. Residual analysis shows [findings]
4. Model achieves R² of [__]

### Practical Application
Regression used in:
- Price prediction
- Sales forecasting
- Stock prediction
- House value estimation

---

## Submission Files

- [ ] Practical_5_Complete_Notebook.ipynb
- [ ] SUBMISSION_TEMPLATE_Practical_5.md
- [ ] PDF export of notebook
- [ ] All visualizations visible

---

**Status:** ✅ COMPLETE

**Next:** Practical 6 - Clustering

