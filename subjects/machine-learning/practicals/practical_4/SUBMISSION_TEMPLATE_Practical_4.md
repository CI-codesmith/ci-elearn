# Practical 4: Classification Algorithms
## Submission Template

**Course:** 316316 - Machine Learning  
**Practical Number:** 4 of 15  
**Academic Year:** 2025-2026  

---

## Student Information

| Field | Details |
|-------|---------|
| **Student Name** | [Your Full Name] |
| **Roll Number** | [Your Roll Number] |
| **College Name** | [Your College Name] |
| **Date of Submission** | [DD/MM/YYYY] |

---

## Learning Outcomes Status

| LO# | Learning Outcome | Achieved | Evidence |
|-----|------------------|----------|----------|
| LO1 | Train-Test Split | ☐ Yes | Split completed: Train 80%, Test 20% |
| LO2 | Decision Tree | ☐ Yes | Model trained, accuracy: [___%] |
| LO3 | KNN Classifier | ☐ Yes | Model trained, optimal K found |
| LO4 | Logistic Regression | ☐ Yes | Model trained, accuracy: [___%] |
| LO5 | Confusion Matrix | ☐ Yes | Generated for all models |
| LO6 | Evaluation Metrics | ☐ Yes | Precision, Recall, F1-Score calculated |
| LO7 | Model Comparison | ☐ Yes | Compared all 3 models |
| LO8 | Hyperparameter Tuning | ☐ Yes | K optimization completed |
| LO9 | Visualization | ☐ Yes | Plots generated |
| LO10 | Model Selection | ☐ Yes | Best model identified |

---

## Test Results Summary

| Test # | Test Name | Result | Details |
|--------|-----------|--------|---------|
| 1 | Train-Test Split | ✅ PASSED | Train: [__], Test: [__] |
| 2 | Decision Tree | ✅ PASSED | Accuracy: [___%] |
| 3 | KNN Classifier | ✅ PASSED | Accuracy: [___%] |
| 4 | Logistic Regression | ✅ PASSED | Accuracy: [___%] |
| 5 | Metrics Comparison | ✅ PASSED | All metrics valid |

**Overall Score:** 5/5 TESTS PASSED ✅

---

## Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Decision Tree | [___%] | [___%] | [___%] | [___%] |
| KNN (k=5) | [___%] | [___%] | [___%] | [___%] |
| Logistic Regression | [___%] | [___%] | [___%] | [___%] |

### Best Performing Model
**Model:** [Decision Tree / KNN / Logistic Regression]  
**Reason:** [Explain why]

---

## Confusion Matrices

### Decision Tree
|        | Predicted: 0 | Predicted: 1 | Predicted: 2 |
|--------|:------------:|:------------:|:------------:|
| Actual: 0 | [__] | [__] | [__] |
| Actual: 1 | [__] | [__] | [__] |
| Actual: 2 | [__] | [__] | [__] |

### KNN (k=5)
|        | Predicted: 0 | Predicted: 1 | Predicted: 2 |
|--------|:------------:|:------------:|:------------:|
| Actual: 0 | [__] | [__] | [__] |
| Actual: 1 | [__] | [__] | [__] |
| Actual: 2 | [__] | [__] | [__] |

### Logistic Regression
|        | Predicted: 0 | Predicted: 1 | Predicted: 2 |
|--------|:------------:|:------------:|:------------:|
| Actual: 0 | [__] | [__] | [__] |
| Actual: 1 | [__] | [__] | [__] |
| Actual: 2 | [__] | [__] | [__] |

---

## Algorithm Details

### 1. Decision Tree
- **Max Depth:** 5
- **Min Samples Split:** 2
- **Min Samples Leaf:** 1
- **Feature Importance:**
  - Feature 1: [___%]
  - Feature 2: [___%]
  - Feature 3: [___%]
  - Feature 4: [___%]

### 2. K-Nearest Neighbors
- **Initial K:** 5
- **Optimal K:** [__]
- **Optimal K Accuracy:** [___%]
- **Distance Metric:** Euclidean
- **Weights:** Uniform

### 3. Logistic Regression
- **Max Iterations:** 200
- **Multi-class:** Multinomial
- **Convergence:** [Yes/No]
- **Coefficients:** [Documented]

---

## Key Findings

### Algorithm Strengths & Weaknesses

**Decision Tree:**
- ✓ Interpretable, good for feature importance
- ✗ Prone to overfitting, requires pruning

**KNN:**
- ✓ Simple, no training phase
- ✗ Slow for large datasets, sensitive to K value

**Logistic Regression:**
- ✓ Fast, provides probability estimates
- ✗ Assumes linear boundary, less interpretable

---

## Troubleshooting Faced

### Issue 1: [If Any]
**Problem:** [Description]  
**Solution:** [What you did]  
**Status:** ✅ Resolved

---

## Code Explanations

### Train-Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```
**Explanation:** [Your explanation]

### Decision Tree Training
```python
dt_model = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_model.fit(X_train, y_train)
```
**Explanation:** [Your explanation]

---

## Evaluation Metrics Explained

**Accuracy:** Percentage of correct predictions
Formula: (TP + TN) / (TP + TN + FP + FN)
Value: [___%]

**Precision:** Of predicted positive, how many are actually positive
Formula: TP / (TP + FP)
Value: [___%]

**Recall (Sensitivity):** Of actual positive, how many are identified
Formula: TP / (TP + FN)
Value: [___%]

**F1-Score:** Harmonic mean of Precision and Recall
Formula: 2 × (Precision × Recall) / (Precision + Recall)
Value: [___%]

---

## Conclusion

### What You Learned

1. How to prepare data for classification tasks
2. How to implement 3 different classification algorithms
3. How to evaluate models using multiple metrics
4. How to compare and select the best model
5. Importance of train-test split and cross-validation

### Practical Insights

- [Add your insights]

### Real-World Application

This practical demonstrates classification techniques used in:
- Email spam detection
- Customer churn prediction
- Disease diagnosis
- Image recognition
- Sentiment analysis

---

## Submission Checklist

- [ ] Notebook executed without errors
- [ ] All 5 tests passed
- [ ] Student information filled
- [ ] Learning outcomes marked
- [ ] Confusion matrices included
- [ ] Metrics comparison completed
- [ ] Reflections written
- [ ] Code is well-commented
- [ ] All visualizations visible

---

## Evaluator Comments

[To be filled by evaluator]

---

**Practical Status:** ✅ COMPLETE & SUBMITTED

**Next Practical:** Practical 5 - Regression Algorithms

