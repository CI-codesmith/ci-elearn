
# MICROPROJECT 4.2: Convolutional Neural Networks

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Advanced Topics)  
**Group Size:** 3 students  
**Duration:** 2 weeks  
**Weight:** 12% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Data preprocessing and augmentation
- **ML Engineer:** CNN model implementation and tuning
- **Analyst:** Evaluation, visualization, and reporting

---

## 🎯 Objective
Design, train, and evaluate a Convolutional Neural Network (CNN) for image classification. Explore the impact of architecture choices and data augmentation.

---

## 📋 Requirements

### Dataset Selection
Choose **one** image dataset:
- **MNIST** (handwritten digits)
- **CIFAR-10** (object recognition)
- **Fashion-MNIST** (clothing images)

### Technical Requirements
- Build a CNN using TensorFlow/Keras (or PyTorch)
- Apply data augmentation (rotation, flipping, etc.)
- Experiment with different architectures (layers, filters, dropout)
- Evaluate with metrics: accuracy, confusion matrix, loss curves
- Visualize feature maps and training progress

### Model Requirements
1. **Data Preprocessing** (normalization, augmentation)
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