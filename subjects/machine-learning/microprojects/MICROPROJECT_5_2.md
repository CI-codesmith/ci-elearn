
# MICROPROJECT 5.2: Model Deployment

**Course:** 316316 - Machine Learning  
**Unit:** 5 (Ethics, Production & Applications)  
**Group Size:** 3 students  
**Duration:** 1.5 weeks  
**Weight:** 10% of course assessment

---

## 👥 Group Roles
- **Data Engineer:** Model packaging and environment setup
- **ML Engineer:** API development and integration
- **Analyst:** Testing, documentation, and reporting

---

## 🎯 Objective
Deploy a trained machine learning model as a web service using Flask or FastAPI. Demonstrate the end-to-end workflow from model training to serving predictions via an API.

---

## 📋 Requirements

### Model Selection
Use a previously trained model (regression or classification):
- **Regression:** House price, MPG, etc.
- **Classification:** Titanic, Iris, etc.

### Technical Requirements
- Package the model using joblib or pickle
- Develop a REST API using Flask or FastAPI
- Implement endpoints for prediction and health check
- Test the API with sample requests (curl, Postman)
- (Optional) Containerize the service with Docker

### Model Requirements
1. **Model Packaging** (save model, requirements.txt)
2. **API Development** (Flask/FastAPI app)
3. **Testing** (unit tests, sample requests)
4. **Documentation** (API usage, setup)

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