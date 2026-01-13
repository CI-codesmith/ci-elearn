

# MICROPROJECT 4.3: Model Evaluation and Metrics (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Supervised Learning)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to evaluate and compare machine learning models using metrics like accuracy, precision, recall, and F1-score.

---

## 📋 Requirements

### Task 1: Load a Dataset
- Use pandas to load a small dataset suitable for PCA (e.g., Iris, Wine, or any CSV)

### Task 2: Apply PCA
- Use Scikit-learn to perform PCA on the dataset
- Show how many components explain most of the variance
- Visualize the first two principal components in a scatter plot

### Task 3: Explain PCA
- Write a markdown cell explaining what PCA does and why it’s useful

---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step
3. **Training & Evaluation** (metrics, visualizations)
4. **Analysis** (architecture impact, sequence length)

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (50% weight)
- **File:** `MP4_3_Group[ID]_RNN.ipynb`
- **Sections:** Preprocessing → Model → Training → Evaluation → Analysis

### 2. Model Report (20% weight)
- **File:** `MP4_3_Group[ID]_Report.pdf`
- **Content:** Architecture, results, analysis

### 3. Visualizations (15% weight)
- **File:** `MP4_3_Group[ID]_Visualizations.pdf`
- **Content:** Loss/accuracy curves, prediction plots

### 4. Presentation (15% weight)
- **File:** `MP4_3_Group[ID]_Presentation.pdf`
- **Content:** 6-8 slides on methodology and results

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Preprocessing** | Proper tokenization, normalization | Good preprocessing | Basic | Poor/none |
| **Model Architecture** | Well-designed, justified | Good architecture | Basic | Poor/none |
| **Training/Evaluation** | Excellent metrics, visualized | Good metrics | Basic | Poor/none |
| **Visualization** | Prediction plots, curves, clear | Good plots | Basic plots | Poor quality |
| **Analysis** | Insightful, architecture impact | Good analysis | Basic | Poor/none |
| **Report Quality** | Clear analysis, insights | Good analysis | Basic summary | Poor docs |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /40 per group

---

## 📝 Template Code

```python
# MICROPROJECT 4.3: Recurrent Neural Networks
# Group: [ID]
# Dataset: [Chosen]

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

# 1. DATA LOADING & PREPROCESSING
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
- TensorFlow/Keras RNN/LSTM guides
- Sequence modeling tutorials
- Course practicals 11 reference

**Deadline:** [Date]