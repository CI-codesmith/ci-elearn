# MICROPROJECT 1.2: Python ML Libraries Mastery

**Course:** 316316 - Machine Learning  
**Unit:** 1 (Introduction to Machine Learning)  
**Group Size:** 3 students  
**Duration:** 1 week  
**Weight:** 8% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Library installation, environment setup
- **ML Engineer:** Code implementation, debugging
- **Analyst:** Documentation, examples creation

---

## 🎯 Objective
Master Python's core ML libraries through hands-on implementation of data manipulation, numerical computing, and visualization tasks.

---

## 📋 Requirements

### Libraries to Master
- **NumPy:** Array operations, mathematical functions
- **Pandas:** DataFrame operations, data manipulation
- **Matplotlib/Seaborn:** Data visualization, plotting

### Tasks to Complete
1. **NumPy Operations** (Data Engineer lead)
   - Array creation and manipulation
   - Mathematical operations
   - Random number generation
   - Linear algebra operations

2. **Pandas Data Handling** (ML Engineer lead)
   - DataFrame/Series creation
   - Data cleaning and preprocessing
   - Grouping and aggregation
   - Merging and joining

3. **Data Visualization** (Analyst lead)
   - Basic plots (line, bar, scatter)
   - Statistical plots (histogram, boxplot)
   - Advanced visualizations (heatmaps, pair plots)

### Dataset
- Use **multiple small datasets** (Iris, Boston Housing, sample sales data)
- Create synthetic data for demonstrations

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (60% weight)
- **File:** `MP1_2_Group[ID]_Libraries.ipynb`
- **Structure:**
  - NumPy section with examples
  - Pandas section with data operations
  - Visualization gallery
  - Best practices and tips

### 2. Code Library (20% weight)
- **File:** `ml_libraries.py`
- **Content:** Reusable functions for each library

### 3. Tutorial Document (20% weight)
- **File:** `MP1_2_Group[ID]_Tutorial.pdf`
- **Content:** Step-by-step guide for each library

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **NumPy Mastery** | Advanced operations, efficient code | Good array manipulation | Basic operations | Poor understanding |
| **Pandas Proficiency** | Complex data operations, optimization | Solid data handling | Basic operations | Errors in code |
| **Visualization Skills** | Professional plots, multiple types | Good variety of plots | Basic plots | Poor quality |
| **Code Quality** | Clean, documented, modular | Mostly clean | Functional | Messy code |
| **Collaboration** | Excellent teamwork, clear roles | Good coordination | Basic collaboration | Poor teamwork |
| **Documentation** | Comprehensive tutorial | Good documentation | Basic guide | Poor docs |

**Total:** /30 per group (peer-adjusted)

---

## 📝 Code Template

```python
# MICROPROJECT 1.2: Python ML Libraries
# Group: [ID]
# Members: [Names]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. NUMPY SECTION
print("=== NUMPY OPERATIONS ===")

# Array creation
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# Mathematical operations
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))

# Matrix operations
matrix = np.random.rand(3, 3)
print("Matrix:\n", matrix)
print("Determinant:", np.linalg.det(matrix))

# 2. PANDAS SECTION
print("\n=== PANDAS OPERATIONS ===")

# Create sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

print("DataFrame:\n", df)
print("Summary statistics:\n", df.describe())

# Grouping
print("Average salary by age group:\n", df.groupby(pd.cut(df['Age'], 2))['Salary'].mean())

# 3. VISUALIZATION SECTION
print("\n=== VISUALIZATIONS ===")

# Set style
plt.style.use('seaborn-v0_8')
sns.set_palette('husl')

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Histogram
axes[0,0].hist(df['Age'], bins=4, alpha=0.7)
axes[0,0].set_title('Age Distribution')

# Scatter plot
axes[0,1].scatter(df['Age'], df['Salary'])
axes[0,1].set_title('Age vs Salary')

# Bar plot
axes[1,0].bar(df['Name'], df['Salary'])
axes[1,0].set_title('Salary by Person')

# Box plot
axes[1,1].boxplot(df['Salary'])
axes[1,1].set_title('Salary Distribution')

plt.tight_layout()
plt.show()

# Seaborn plots
plt.figure(figsize=(10, 6))
sns.pairplot(df, diag_kind='kde')
plt.suptitle('Pair Plot of All Variables', y=1.02)
plt.show()
```

---

## 🆘 Resources & Tips

### Getting Started
- Install libraries: `pip install numpy pandas matplotlib seaborn`
- Use official documentation for reference
- Practice with small examples first

### Best Practices
- Use vectorized operations in NumPy
- Chain operations in Pandas
- Customize plots with matplotlib parameters
- Use seaborn for statistical plots

### Common Challenges
- NumPy broadcasting rules
- Pandas indexing and slicing
- Matplotlib figure management

---

## 📞 Group Coordination

### Weekly Schedule
- **Day 1-2:** NumPy focus (Data Engineer)
- **Day 3-4:** Pandas focus (ML Engineer)
- **Day 5-7:** Visualization focus (Analyst)

### Communication
- Daily stand-ups via chat
- Shared Google Doc for notes
- GitHub for code collaboration

---

**Deadline:** [Date]  
**Peer Evaluation Due:** [Date + 2 days]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_1_2.md