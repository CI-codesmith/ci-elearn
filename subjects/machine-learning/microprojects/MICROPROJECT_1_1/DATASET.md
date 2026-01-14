# Dataset Information - MICROPROJECT 1.1

## 📊 Available Datasets

For this introductory project, you'll work with simple, well-known datasets included in Scikit-learn.

### Option 1: Iris Dataset (Recommended for Beginners)

**Description:**
- Classic dataset with 150 flower samples
- 4 features: sepal length, sepal width, petal length, petal width
- 3 classes: Iris-setosa, Iris-versicolor, Iris-virginica

**How to Load:**
```python
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Display info
print(df.head())
print(df.shape)  # (150, 5)
```

**Why Use It:**
- ✅ Small and easy to understand
- ✅ Already clean (no missing values)
- ✅ Perfect for first visualization
- ✅ Great for learning pandas basics

---

### Option 2: Boston Housing Dataset

**Description:**
- 506 houses with 13 features
- Target: House prices
- Features: Number of rooms, age, location, etc.

**How to Load:**
```python
from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['target'] = boston.target

print(df.head())
print(df.shape)  # (506, 14)
```

**Why Use It:**
- ✅ Real-world application (housing prices)
- ✅ Slightly larger dataset
- ✅ Good for regression examples

---

### Option 3: Titanic Dataset (CSV from Kaggle)

**Description:**
- 891 passengers with 11 features
- Target: Survived (1) or Not (0)
- Features: Age, Sex, Fare, Class, etc.

**How to Load:**
```python
import pandas as pd

df = pd.read_csv('titanic.csv')
print(df.head())
print(df.shape)  # (891, 12)
```

**Download:**
- Website: https://www.kaggle.com/datasets/titanic
- Or use: https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv

**Why Use It:**
- ✅ Real historical data
- ✅ Has missing values (good for learning cleaning)
- ✅ Binary classification target

---

## 🎯 Recommendation for This Project

**Use the Iris Dataset** because:
1. It's built into Scikit-learn (no download needed)
2. Small and easy to visualize
3. Perfect for beginners
4. Has multiple features to explore

---

## 📥 Quick Loading Code

Copy-paste this to load any dataset:

```python
# For Iris
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
```

---

## 📋 Dataset Features Reference

### Iris
- **Sepal Length** (cm)
- **Sepal Width** (cm)
- **Petal Length** (cm)
- **Petal Width** (cm)

### Boston Housing
- **CRIM** - Crime rate
- **ZN** - Residential land proportion
- **INDUS** - Industrial land proportion
- **CHAS** - Charles River dummy
- **NOX** - Nitrogen oxide level
- **RM** - Average rooms per house
- **AGE** - Proportion of old buildings
- **DIS** - Distance to employment centers
- **RAD** - Highway accessibility
- **TAX** - Property tax rate
- **PTRATIO** - Student-teacher ratio
- **B** - Proportion of Black residents
- **LSTAT** - % lower status population

### Titanic
- **PassengerId**
- **Survived** (Target)
- **Pclass** - Ticket class
- **Name**
- **Sex**
- **Age**
- **SibSp** - Siblings/spouses
- **Parch** - Parents/children
- **Ticket**
- **Fare**
- **Cabin**
- **Embarked** - Port

---

## ✅ Dataset Quality

All datasets are:
- ✅ Clean and verified
- ✅ No major data issues
- ✅ Well-documented
- ✅ Used in ML education worldwide

---

## 🚀 Next Step

Once you've loaded a dataset, proceed to the next steps in `HOW_TO_DO.md`!
