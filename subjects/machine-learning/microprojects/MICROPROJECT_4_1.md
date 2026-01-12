# MICROPROJECT 4.1: Neural Network Implementation

**Course:** 316316 - Machine Learning  
**Unit:** 4 (Advanced Topics)  
**Duration:** 2 weeks  
**Submission:** Jupyter Notebook + Model + Report  
**Weight:** 20% of unit assessment

---

## 🎯 Objective
Design, implement, and train a neural network for a classification task. Students will understand deep learning fundamentals and apply them to solve real problems.

---

## 📋 Requirements

### Dataset Selection
Choose **one** dataset:
- **MNIST** (handwritten digits, 70k images)
- **CIFAR-10** (10 classes, 60k images)
- **Fashion MNIST** (clothing classification)
- **Custom image dataset** (with approval)

### Technical Requirements
- **Framework:** TensorFlow/Keras or PyTorch
- **Network Architecture:** Minimum 3 layers (input, hidden, output)
- **Features:** Include dropout, batch normalization
- **Training:** Proper train/validation/test split
- **Optimization:** Adam optimizer, learning rate scheduling

### Implementation Requirements
1. **Data Preprocessing** (normalization, augmentation)
2. **Model Architecture** (design and justify)
3. **Training Process** (monitor loss/accuracy, prevent overfitting)
4. **Evaluation** (test accuracy, confusion matrix, misclassifications)
5. **Hyperparameter Tuning** (experiment with parameters)

---

## 📤 Deliverables

### 1. Jupyter Notebook (70% weight)
- **File:** `MP4_1_[Name]_[Dataset].ipynb`
- **Include:** Complete implementation, training logs, evaluation

### 2. Saved Model (15% weight)
- **File:** `trained_model.h5` (Keras) or `model.pth` (PyTorch)
- **Include:** Model weights and architecture

### 3. PDF Report (15% weight)
- **File:** `MP4_1_[Name]_Report.pdf`
- **Content:** Architecture explanation, training analysis, results

---

## 📊 Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Preprocessing** | Proper normalization, augmentation | Good preprocessing | Basic prep | Inadequate |
| **Model Architecture** | Well-designed network, justified choices | Good architecture | Basic network | Poor design |
| **Training Process** | Proper training, handles overfitting | Good training | Basic training | Poor training |
| **Evaluation** | Comprehensive metrics, analysis | Good evaluation | Basic metrics | No evaluation |
| **Code Quality** | Clean, modular, documented | Mostly clean | Functional | Messy |
| **Innovation** | Creative approaches, experiments | Some experiments | Standard approach | No creativity |

**Total:** /30

**Grade Scale:** 24-30:A, 18-23:B, 12-17:C, <12:F

---

## 📝 Template Code (Keras)

```python
# MICROPROJECT 4.1: Neural Network
# Student: [Name]
# Dataset: [Chosen]

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt

# 1. DATA LOADING
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 2. PREPROCESSING
# x_train = x_train.astype('float32') / 255.0
# x_test = x_test.astype('float32') / 255.0

# 3. MODEL ARCHITECTURE
# model = keras.Sequential([
#     layers.Flatten(input_shape=(28, 28)),
#     layers.Dense(128, activation='relu'),
#     layers.Dropout(0.2),
#     layers.Dense(64, activation='relu'),
#     layers.Dense(10, activation='softmax')
# ])

# 4. COMPILATION
# model.compile(optimizer='adam',
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])

# 5. TRAINING
# history = model.fit(x_train, y_train, epochs=10, validation_split=0.2)

# 6. EVALUATION
# test_loss, test_acc = model.evaluate(x_test, y_test)
# print(f"Test accuracy: {test_acc}")

# 7. SAVE MODEL
# model.save('trained_model.h5')
```

---

## 🆘 Resources
- TensorFlow/Keras documentation
- Practical 12-13 reference
- Coursera Deep Learning courses

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_4_1.md