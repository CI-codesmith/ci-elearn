
# MICROPROJECT 1.3: Traditional Programming vs Machine Learning (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 1 (Introduction to Machine Learning)  
**Group Size:** 3 students  
**Duration:** 1 week  
**Weight:** 8% of course assessment

---

## 🎯 Objective
Understand the difference between traditional programming and machine learning by solving a simple problem both ways. Learn when ML is useful and why.

---

## 📋 Requirements

### Task 1: Choose a Simple Problem
- Example: Predict if a number is even or odd, or classify fruit by color (apple vs banana).

### Task 2: Traditional Approach
- Write Python code using if/else statements or rules to solve the problem.
- Explain your logic in a markdown cell.

### Task 3: ML Approach
- Use a simple ML algorithm (e.g., Decision Tree or Logistic Regression from Scikit-learn) to solve the same problem.
- Show how the model learns from data instead of rules.
- Explain the difference in a markdown cell.

---

## 📤 Deliverables
- Jupyter Notebook with both approaches and explanations
- Short PDF summary (1 page) comparing the two methods

---

## 📝 Tips for Beginners
- Keep your code simple and well-commented
- Focus on understanding, not complexity
- Ask for help if you’re unsure about ML code
   - Handle generalization automatically

3. **Comparative Analysis** (Analyst lead)
   - Performance metrics comparison
   - Scalability assessment
   - Maintenance considerations
   - Real-world applicability

### Evaluation Criteria
- **Accuracy:** How well each approach solves the problem
- **Scalability:** How well it handles new data/cases
- **Maintenance:** Ease of updating and improving
- **Resource Usage:** Computational requirements

---

## 📤 Group Deliverables

### 1. Comparative Analysis Report (50% weight)
- **File:** `MP1_3_Group[ID]_Comparison.pdf`
- **Sections:**
  - Problem description
  - Traditional approach implementation
  - ML approach implementation
  - Head-to-head comparison
  - Conclusions and recommendations

### 2. Code Implementation (30% weight)
- **Files:** `traditional_approach.py`, `ml_approach.py`
- **Content:** Complete implementations for both methods

### 3. Demonstration Video (20% weight)
- **File:** `MP1_3_Group[ID]_Demo.mp4`
- **Content:** 3-5 minute explanation of approaches and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Traditional Implementation** | Robust rule-based solution | Solid implementation | Basic approach | Incomplete/incorrect |
| **ML Implementation** | Appropriate algorithm, good performance | Working ML solution | Basic ML approach | Poor implementation |
| **Comparative Analysis** | Deep insights, balanced evaluation | Good comparison | Surface-level analysis | Biased/incomplete |
| **Code Quality** | Clean, well-documented code | Mostly clean | Functional | Messy/error-prone |
| **Presentation** | Clear, engaging demonstration | Good explanation | Basic demo | Poor communication |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /30 per group

---

## 📝 Implementation Template

```python
# MICROPROJECT 1.3: Traditional vs ML Comparison
# Group: [ID]
# Problem: [Chosen Problem]

# TRADITIONAL APPROACH
def traditional_spam_detector(email_text):
    """
    Rule-based spam detection
    """
    spam_keywords = ['free', 'win', 'urgent', 'click here', 'buy now']
    score = 0

    # Convert to lowercase
    text = email_text.lower()

    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in text:
            score += 1

    # Length-based rules
    if len(text) > 500:
        score += 0.5

    # Capitalization rules
    caps_ratio = sum(1 for c in text if c.isupper()) / len(text)
    if caps_ratio > 0.3:
        score += 0.5

    # Threshold decision
    return score > 2  # Spam if score > 2

# ML APPROACH
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

def ml_spam_detector(X_train, y_train, X_test):
    """
    ML-based spam detection using Naive Bayes
    """
    # Feature extraction
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Model training
    model = MultinomialNB()
    model.fit(X_train_vec, y_train)

    # Prediction
    predictions = model.predict(X_test_vec)
    probabilities = model.predict_proba(X_test_vec)

    return predictions, probabilities

# COMPARISON ANALYSIS
def compare_approaches(traditional_results, ml_results, y_true):
    """
    Compare performance of both approaches
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score

    # Traditional metrics
    trad_acc = accuracy_score(y_true, traditional_results)
    trad_prec = precision_score(y_true, traditional_results)
    trad_rec = recall_score(y_true, traditional_results)

    # ML metrics
    ml_acc = accuracy_score(y_true, ml_results)
    ml_prec = precision_score(y_true, ml_results)
    ml_rec = recall_score(y_true, ml_results)

    print("Traditional Approach:")
    print(f"  Accuracy: {trad_acc:.3f}")
    print(f"  Precision: {trad_prec:.3f}")
    print(f"  Recall: {trad_rec:.3f}")

    print("\nML Approach:")
    print(f"  Accuracy: {ml_acc:.3f}")
    print(f"  Precision: {ml_prec:.3f}")
    print(f"  Recall: {ml_rec:.3f}")

    return {
        'traditional': {'acc': trad_acc, 'prec': trad_prec, 'rec': trad_rec},
        'ml': {'acc': ml_acc, 'prec': ml_prec, 'rec': ml_rec}
    }
```

---

## 🆘 Example Problems

### Spam Detection
- **Traditional:** Keyword matching, length checks, sender analysis
- **ML:** Naive Bayes, SVM with TF-IDF features
- **Dataset:** SpamAssassin or custom labeled emails

### Weather Prediction
- **Traditional:** Statistical models, trend analysis
- **ML:** Regression models with multiple features
- **Dataset:** Historical weather data

---

## 📞 Group Tips

### Division of Work
- **Data Engineer:** Set up problem, prepare datasets
- **ML Engineer:** Implement both approaches
- **Analyst:** Run comparisons, create visualizations

### Success Factors
- Choose a problem where both approaches are feasible
- Use same evaluation dataset for fair comparison
- Consider edge cases and limitations of each approach

---

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_1_3.md