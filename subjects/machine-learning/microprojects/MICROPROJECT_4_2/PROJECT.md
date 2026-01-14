

# MICROPROJECT 4.2: Basic Regression Algorithms (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Supervised Learning)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to use simple regression algorithms (Linear Regression) to predict continuous values and interpret results.

---

## 📋 Requirements

### Task 1: Load a Dataset
- Use pandas to load a small dataset suitable for clustering (e.g., Iris, Mall Customers, or any CSV)

### Task 2: Apply Both Algorithms
- Use Scikit-learn to perform K-Means and Hierarchical Clustering
- Show cluster assignments for each sample

### Task 3: Compare Methods
- Write a markdown cell comparing K-Means and Hierarchical Clustering (how they work, strengths/weaknesses, when to use each)

---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step
2. **Model Building** (CNN architecture)
3. **Training & Evaluation** (metrics, visualizations)
4. **Analysis** (architecture impact, overfitting/underfitting)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP4_2_Group[ID]_CNN.ipynb`
- **Sections:** Preprocessing → Model → Training → Evaluation → Analysis

### 2. Model Report (20% weight)
- **File:** `MP4_2_Group[ID]_Report.pdf`
- **Content:** Architecture, results, analysis

### 3. Visualizations (15% weight)
- **File:** `MP4_2_Group[ID]_Visualizations.pdf`
- **Content:** Loss/accuracy curves, feature maps

### 4. Presentation (15% weight)
- **File:** `MP4_2_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Proper normalization, augmentation | Good preprocessing | Basic | Poor/none |
| **Model Architecture** | Well-designed, justified | Good architecture | Basic | Poor/none |
| **Training/Evaluation** | Excellent metrics, visualized | Good metrics | Basic | Poor/none |
| **Visualization** | Feature maps, curves, clear | Good plots | Basic plots | Poor quality |
| **Analysis** | Insightful, architecture impact | Good analysis | Basic | Poor/none |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 4.2: Convolutional Neural Networks
# Group: [ID]
# Dataset: [Chosen]

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 1. DATA LOADING & AUGMENTATION
# ...

# 2. MODEL BUILDING
# model = models.Sequential([...])

# 3. TRAINING
# history = model.fit(...)

# 4. EVALUATION
# ...

# 5. VISUALIZATION
# ...
```

---

## 🆘 Resources
- TensorFlow/Keras CNN guides
- Data augmentation tutorials
- Course practicals 10 reference

**Deadline:** [Date]