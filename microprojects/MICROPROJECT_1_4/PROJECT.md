
# MICROPROJECT 1.4: Building Your First ML Model (Beginner)

**Course:** 316316 - Machine Learning  
**Unit:** 1 (Introduction to Machine Learning)  
**Duration:** 1 week  
**Submission:** Jupyter Notebook (.ipynb) + CSV + PDF Summary  
**Weight:** 8% of unit assessment

---

## 🎯 Objective
Learn how to collect a small dataset and perform basic cleaning and inspection. Focus on handling missing values and understanding your data.

---

## 📋 Requirements

### Task 1: Data Collection
- Download a small public dataset (e.g., Iris, Titanic, or any CSV with at least 50 samples)
- Briefly describe the dataset in a markdown cell (source, number of samples, features)

### Task 2: Data Inspection
- Use pandas to load the dataset
- Show the first few rows, column names, and basic statistics (mean, min, max)

### Task 3: Handle Missing Values
- Check for missing values and show how to fill or drop them using pandas
- Explain your choices in markdown

### Task 4: Save Cleaned Data
- Save the cleaned dataset as a new CSV file

---

## 📤 Deliverables
- Jupyter Notebook with code and markdown explanations
- Cleaned CSV file
- Short PDF summary (1 page) describing your process

---

## 📝 Tips for Beginners
- Focus on simple, clear steps
- Use comments to explain your code
- Ask for help if you’re unsure about any step

3. **Feature Engineering** (Analyst lead)
   - Feature creation/transformation
   - Encoding categorical variables
   - Normalization/scaling
   - Feature selection

### Quality Assurance
- **Completeness:** <5% missing values
- **Consistency:** No conflicting data
- **Accuracy:** Valid data ranges
- **Relevance:** Features useful for ML

---

## 📤 Group Deliverables

### 1. Curated Dataset (40% weight)
- **Files:** `raw_data.[format]`, `cleaned_data.csv`, `processed_data.csv`
- **Format:** CSV with proper headers and data types

### 2. Data Documentation (30% weight)
- **File:** `MP1_4_Group[ID]_Documentation.pdf`
- **Content:** Data dictionary, collection methodology, cleaning decisions

### 3. EDA Report (30% weight)
- **File:** `MP1_4_Group[ID]_EDA.pdf`
- **Content:** Statistical analysis, visualizations, insights

---

## 📊 Group Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Data Collection** | Creative sourcing, comprehensive data | Good data acquisition | Basic collection | Poor/inadequate data |
| **Data Cleaning** | Thorough cleaning, smart imputation | Good data quality | Basic cleaning | Messy data |
| **Feature Engineering** | Innovative features, proper preprocessing | Solid feature work | Basic processing | Poor features |
| **Documentation** | Complete data dictionary, clear methodology | Good documentation | Basic docs | Poor/missing docs |
| **Analysis Quality** | Deep insights, excellent visualizations | Good analysis | Basic stats | Poor analysis |
| **Collaboration** | Excellent teamwork, clear division | Good coordination | Basic collaboration | Poor teamwork |

**Total:** /30 per group

---

## 📝 Project Template

```python
# MICROPROJECT 1.4: Dataset Curation
# Group: [ID]
# Dataset: [Description]

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. DATA COLLECTION
def collect_data():
    """
    Collect data from chosen source
    """
    # Example: API collection
    # response = requests.get('https://api.example.com/data')
    # data = response.json()

    # Example: CSV loading
    # df = pd.read_csv('raw_data.csv')

    # Example: Web scraping
    # url = 'https://example.com/data'
    # response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'html.parser')

    return df

# 2. DATA CLEANING
def clean_data(df):
    """
    Clean and preprocess the data
    """
    print("Original shape:", df.shape)
    print("Missing values:\n", df.isnull().sum())

    # Handle missing values
    df_clean = df.copy()

    # Numerical columns - median imputation
    num_cols = df.select_dtypes(include=[np.number]).columns
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            df_clean[col].fillna(df[col].median(), inplace=True)

    # Categorical columns - mode imputation
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            df_clean[col].fillna(df[col].mode()[0], inplace=True)

    # Remove duplicates
    df_clean.drop_duplicates(inplace=True)

    # Outlier treatment (IQR method for numerical columns)
    for col in num_cols:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

    print("Cleaned shape:", df_clean.shape)
    return df_clean

# 3. FEATURE ENGINEERING
def engineer_features(df):
    """
    Create and transform features
    """
    df_processed = df.copy()

    # Encode categorical variables
    le = LabelEncoder()
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        df_processed[col + '_encoded'] = le.fit_transform(df_processed[col])

    # Scale numerical features
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=[np.number]).columns
    df_processed[num_cols] = scaler.fit_transform(df_processed[num_cols])

    return df_processed, scaler

# 4. EXPLORATORY DATA ANALYSIS
def perform_eda(df):
    """
    Generate EDA report
    """
    # Basic statistics
    print("Dataset Overview:")
    print(df.info())
    print("\nStatistical Summary:")
    print(df.describe())

    # Visualizations
    plt.figure(figsize=(12, 8))

    # Histogram for numerical columns
    num_cols = df.select_dtypes(include=[np.number]).columns[:4]  # First 4 numerical
    df[num_cols].hist(bins=30, figsize=(12, 8))
    plt.tight_layout()
    plt.savefig('numerical_distributions.png')
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
    plt.title('Feature Correlation Matrix')
    plt.savefig('correlation_heatmap.png')
    plt.show()

# MAIN EXECUTION
if __name__ == "__main__":
    # Collect data
    raw_data = collect_data()

    # Clean data
    cleaned_data = clean_data(raw_data)

    # Engineer features
    processed_data, scaler = engineer_features(cleaned_data)

    # Perform EDA
    perform_eda(processed_data)

    # Save processed data
    processed_data.to_csv('processed_dataset.csv', index=False)
    print("Dataset curation complete!")
```

---

## 🆘 Data Sources & Tips

### Data Collection Ideas
- **APIs:** OpenWeatherMap, Twitter API, GitHub API
- **Web Scraping:** BeautifulSoup for public websites
- **Surveys:** Google Forms for custom data collection
- **Public Datasets:** Kaggle, UCI ML Repository

### Quality Checklist
- [ ] Data is representative of real-world scenarios
- [ ] Features are relevant to potential ML tasks
- [ ] No personally identifiable information
- [ ] Proper licensing and attribution

### Common Challenges
- API rate limits and authentication
- Web scraping legal and ethical considerations
- Handling different data formats
- Dealing with messy real-world data

---

## 📞 Group Coordination

### Timeline
- **Week 1:** Data collection and initial cleaning
- **Week 1.5:** Feature engineering and final EDA

### Best Practices
- Document all decisions and assumptions
- Version control your data processing scripts
- Test your pipeline on sample data first
- Validate results at each step

---

**Deadline:** [Date]</content>
<parameter name="filePath">/Users/akashchatake/Downloads/Work/College/📁_ORGANIZED_COLLEGE/AY_2025_2026/2026_Summer_Work/Machine_Learning/Microprojects/MICROPROJECT_1_4.md