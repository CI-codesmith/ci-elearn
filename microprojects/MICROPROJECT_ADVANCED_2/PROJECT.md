# MICROPROJECT ADVANCED 2: Deep Learning for Image Classification

**Course:** 316316 - Machine Learning  
**Level:** Advanced (For High-Performing Students)  
**Duration:** 3 weeks  
**Submission:** Jupyter Notebook + Training Code + Trained Model + Report  
**Weight:** 20% of course assessment

---

## 🎯 Objective
Develop a deep neural network for image classification using convolutional neural networks (CNNs). Learn transfer learning, data augmentation, and advanced model optimization techniques.

---

## 📋 Requirements

### Phase 1: Dataset Preparation & Analysis
- **Public dataset:** Use CIFAR-10, MNIST, STL-10, or similar (10,000+ images)
  - OR use a custom image dataset from your domain (e.g., plant disease, animal classification)
- **EDA:** Visualize sample images, class distribution, image properties
- **Data augmentation:** Implement rotation, zooming, flipping to increase diversity
- **Train-validation-test split:** 70-15-15 or similar proportions

### Phase 2: Model Architecture Development
- **Baseline CNN:** Build a simple CNN from scratch (3-5 conv layers)
  - Architecture: Conv → ReLU → MaxPool → Flatten → Dense → Softmax
  - Document layer specifications and parameters
  - Visualize architecture
- **Transfer Learning:** Use pre-trained models (VGG16, ResNet50, MobileNet)
  - Fine-tune last layers for your dataset
  - Compare performance vs. baseline CNN

### Phase 3: Model Training & Optimization
- **Loss function & optimizer:** Choose appropriate loss (CrossEntropyLoss) and optimizer (Adam, SGD)
- **Regularization:** Implement dropout, L1/L2 regularization to prevent overfitting
- **Learning rate scheduling:** Use learning rate decay or cyclic learning rates
- **Early stopping:** Monitor validation loss and stop when plateau occurs
- **Batch size & epochs:** Experiment and document choices

### Phase 4: Evaluation & Performance Analysis
- **Metrics:** Accuracy, Precision, Recall, F1-score, Confusion matrix
- **Learning curves:** Plot training vs. validation loss and accuracy
- **Per-class analysis:** Show which classes are easy/hard to classify
- **Visualize predictions:** Show correct and incorrect predictions with confidence scores
- **Error analysis:** Analyze misclassified examples

### Phase 5: Advanced Techniques (Choose 2+)
- **Ensemble methods:** Combine multiple models for better predictions
- **Attention mechanisms:** Implement or explain attention in CNNs
- **Grad-CAM visualization:** Visualize what model learned with saliency maps
- **Data augmentation strategies:** Compare different augmentation techniques
- **Adversarial robustness:** Test model with adversarial examples

### Phase 6: Model Deployment
- **Model saving:** Save trained model and weights
- **Inference script:** Create script for making predictions on new images
- **Performance optimization:** Model quantization or pruning for deployment
- **Documentation:** How to use the trained model

---

## 📤 Deliverables

### 1. Jupyter Notebook (35%)
- **File:** `MICROPROJECT_ADV2_CNN_Implementation.ipynb`
- Complete implementation with markdown explanations
- All visualizations and performance graphs
- Code is clean, modular, and well-commented
- Training/validation progress clearly shown

### 2. Training Code (20%)
- **File:** `MICROPROJECT_ADV2_train.py`
- Separate Python file with model classes and training loops
- Data loading and preprocessing functions
- Model definition using TensorFlow/PyTorch
- Checkpointing and model saving

### 3. Inference/Prediction Script (15%)
- **File:** `MICROPROJECT_ADV2_predict.py`
- Load trained model and make predictions
- Handle image input (file path or URL)
- Display predictions with confidence scores
- Include example usage

### 4. Comprehensive Report (20%)
- **File:** `MICROPROJECT_ADV2_Report.pdf` (5-10 pages)
- Problem statement and dataset description
- CNN architecture explanation with diagrams
- Training methodology and hyperparameters
- Results, graphs, and performance analysis
- Comparison of baseline vs. transfer learning
- Conclusions and limitations

### 5. Presentation Slides (10%)
- **File:** `MICROPROJECT_ADV2_Presentation.pdf`
- 15-20 slides with visualizations
- Architecture diagrams and results
- Key findings and insights

---

## 📊 Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Preparation** | Thorough EDA, good augmentation | Good preparation, clear choices | Basic setup | Insufficient |
| **CNN Architecture** | Well-designed, justified choices | Good architecture, reasonable | Basic CNN | Poor design |
| **Model Development** | Sophisticated approach, advanced techniques | Good training strategy | Basic training | Incomplete |
| **Evaluation** | Comprehensive analysis, insights | Good metrics and visualization | Basic evaluation | Incomplete |
| **Advanced Techniques** | 2+ advanced techniques well-implemented | 1-2 techniques | Mentioned but not deep | Missing |
| **Code Quality** | Production-ready, modular, documented | Good structure, well-commented | Functional | Messy/broken |
| **Report Quality** | Excellent analysis, clear communication | Good documentation | Basic summary | Poor docs |
| **Presentation** | Clear, engaging, compelling | Good delivery | Basic presentation | Poor quality |

**Total:** /40

---

## 🆘 Resources

### Frameworks & Libraries
- **Deep Learning:** TensorFlow/Keras or PyTorch
- **Image Processing:** OpenCV, Pillow
- **Visualization:** Matplotlib, TensorBoard
- **Utilities:** NumPy, Pandas

### Datasets
- [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html)
- [MNIST](http://yann.lecun.com/exdb/mnist/)
- [ImageNet](https://www.image-net.org/) (subset available)
- [Kaggle Image Datasets](https://www.kaggle.com/datasets?tags=images)

### Learning Resources
- TensorFlow/PyTorch documentation
- CNN architectures: VGG, ResNet, MobileNet papers
- Transfer learning tutorials
- Grad-CAM and visualization techniques

---

## 💡 Tips for Success

1. **Start with baseline:** Get a simple CNN working first
2. **Use pre-trained models:** Transfer learning often outperforms training from scratch
3. **Monitor overfitting:** Use validation set and early stopping
4. **Visualize learning:** Plot loss curves and example predictions
5. **Experiment systematically:** Change one hyperparameter at a time
6. **Document experiments:** Keep track of what you tried and results

---

## 📅 Milestone Timeline

- **Week 1:** Data preparation, EDA, basic CNN implementation
- **Week 2:** Model training, optimization, transfer learning experiments
- **Week 3:** Advanced techniques, evaluation, report and presentation

---

**Deadline:** 3 weeks from project start  
**Submission Platform:** Course portal (Jupyter + Code + Trained model + Report)
