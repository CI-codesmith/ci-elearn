
# MICROPROJECT 4.3: Recurrent Neural Networks

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Advanced Topics)  
**Group Size:** 3 students  
**Duration:** 2 weeks  
**Weight:** 12% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Sequence data preprocessing and preparation
- **ML Engineer:** RNN/LSTM model implementation and tuning
- **Analyst:** Evaluation, visualization, and reporting

---

## 🎯 Objective
Design, train, and evaluate a Recurrent Neural Network (RNN/LSTM) for sequence modeling tasks. Explore the impact of architecture choices and sequence length.

---

## 📋 Requirements

### Dataset Selection
Choose **one** sequence dataset:
- **IMDB Reviews** (sentiment analysis)
- **Airline Passenger Data** (time series forecasting)
- **Shakespeare Text** (character-level prediction)

### Technical Requirements
- Build an RNN/LSTM using TensorFlow/Keras (or PyTorch)
- Experiment with different architectures (layers, units, dropout)
- Evaluate with metrics: accuracy, loss curves, RMSE (for regression)
- Visualize training progress and predictions

### Model Requirements
1. **Data Preprocessing** (tokenization, padding, normalization)
2. **Model Building** (RNN/LSTM architecture)
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