

# MICROPROJECT 5.2: Compare K-Means and Hierarchical Clustering (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 5 (Unsupervised Learning)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn the basics of deploying a machine learning model. Practice saving a trained model and writing simple instructions for how it could be used in production.

---

## 📋 Requirements

### Task 1: Save a Trained Model
- Train a simple model (e.g., Decision Tree or Linear Regression) on a small dataset
- Save the trained model using pickle or joblib

### Task 2: Write Deployment Instructions
- Write a markdown cell explaining how someone could use the saved model to make predictions
- List any requirements (Python version, libraries)

### Task 3: Discuss Real-World Use
- Write a markdown cell describing one real-world scenario where model deployment is important (e.g., predicting loan approval, spam detection)

---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step

---

## 📤 Group Deliverables

### 1. Jupyter Notebook (40% weight)
- **File:** `MP5_2_Group[ID]_Deployment.ipynb`
- **Sections:** Model packaging → API → Testing

### 2. API Code (30% weight)
- **File:** `app.py`, `requirements.txt`, `Dockerfile` (optional)

### 3. Deployment Report (20% weight)
- **File:** `MP5_2_Group[ID]_Report.pdf`
- **Content:** Deployment steps, API usage, testing

### 4. Presentation (10% weight)
- **File:** `MP5_2_Group[ID]_Presentation.pdf`
- **Content:** 5-7 slides on deployment workflow

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Model Packaging** | Correct, reproducible | Good packaging | Basic | Poor/none |
| **API Development** | Robust, well-documented | Good API | Basic | Poor/none |
| **Testing** | Comprehensive, automated | Good tests | Basic | Poor/none |
| **Documentation** | Clear, complete | Good docs | Basic | Poor/none |
| **Presentation** | Clear, engaging slides | Good slides | Basic presentation | Poor slides |
| **Collaboration** | Excellent teamwork | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /30 per group

---

## 📝 Template Code

```python
# app.py (Flask example)
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
	data = request.get_json()
	prediction = model.predict([data['features']])
	return jsonify({'prediction': prediction.tolist()})

@app.route('/health', methods=['GET'])
def health():
	return 'OK', 200

if __name__ == '__main__':
	app.run(debug=True)
```

---

## 🆘 Resources
- Flask/FastAPI deployment guides
- Docker documentation (optional)
- Course practicals 14 reference

**Deadline:** [Date]