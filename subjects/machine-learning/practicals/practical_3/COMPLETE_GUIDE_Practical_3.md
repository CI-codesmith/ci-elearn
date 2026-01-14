# Practical 3: Reading Datasets from Multiple Formats
## Complete How-To Guide

**Course:** 316316 - Machine Learning | **Practical:** 3 of 15 | **Duration:** 2 Hours  
**CO:** CO3 - Read and process datasets from different formats (CSV, JSON, XML, Excel, SQL)

---

## Learning Outcomes

1. Read datasets from CSV files using Pandas
2. Parse JSON formatted data
3. Extract data from XML files
4. Read Excel spreadsheets (.xlsx, .xls)
5. Connect and query SQL databases
6. Handle different delimiters and encodings
7. Validate data after loading
8. Create reusable data loading functions
9. Compare different file formats
10. Optimize loading performance

---

## Pre-Practical Requirements

- **Prerequisites:** Practical 1 & 2 completed
- **Time:** 1.5-2 hours
- **Libraries:** pandas, openpyxl, sqlite3, sqlalchemy, lxml

---

## Step-by-Step Procedure

### Phase 1: Environment Setup

```bash
# Activate virtual environment
source ml_env/bin/activate  # macOS/Linux
ml_env\Scripts\activate     # Windows

# Install additional libraries if needed
pip install openpyxl sqlalchemy lxml

# Create workspace
mkdir -p practicals/practical_3/{data,scripts,notebooks}
cd practicals/practical_3
jupyter notebook
```

---

### Phase 2: Reading CSV Files

**Step 2.1:** Basic CSV Loading

```python
import pandas as pd
import numpy as np

# Basic CSV reading
df = pd.read_csv('data.csv')

# With parameters
df = pd.read_csv(
    'data.csv',
    delimiter=',',           # Delimiter (,;|\t etc)
    header=0,                # Row index for column names
    encoding='utf-8',        # File encoding
    dtype={'age': int},      # Column data types
    skiprows=2,              # Skip first 2 rows
    nrows=1000               # Read only first 1000 rows
)

print(f"Shape: {df.shape}")
print(df.head())
```

**Step 2.2:** Handling Encoding Issues

```python
# Try different encodings
encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

for enc in encodings:
    try:
        df = pd.read_csv('data.csv', encoding=enc)
        print(f"✅ Successfully loaded with {enc}")
        break
    except UnicodeDecodeError:
        continue
```

---

### Phase 3: Reading JSON Files

**Step 3.1:** Parse JSON data

```python
# From file
df_json = pd.read_json('data.json')

# With parameters
df_json = pd.read_json(
    'data.json',
    orient='records',    # records, split, index, columns, values
    encoding='utf-8'
)

# From JSON string
json_str = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}]'
df = pd.read_json(json_str, orient='records')
```

**Step 3.2:** Nested JSON handling

```python
import json

# Load nested JSON
with open('nested.json', 'r') as f:
    data = json.load(f)

# Normalize nested JSON
df_normalized = pd.json_normalize(data['records'])
print(df_normalized.head())
```

---

### Phase 4: Reading XML Files

**Step 4.1:** XML parsing

```python
import xml.etree.ElementTree as ET

# Parse XML
tree = ET.parse('data.xml')
root = tree.getroot()

# Extract data into list
data_list = []
for item in root.findall('record'):
    record = {
        'id': item.find('id').text,
        'name': item.find('name').text,
        'value': item.find('value').text
    }
    data_list.append(record)

df_xml = pd.DataFrame(data_list)
```

**Step 4.2:** Using pandas to read XML

```python
# Method 1: Using read_xml (pandas 1.3+)
df_xml = pd.read_xml('data.xml', xpath='//record')

# Method 2: Using lxml
df_xml = pd.read_xml('data.xml', xpath='//item')
```

---

### Phase 5: Reading Excel Files

**Step 5.1:** Reading Excel spreadsheets

```python
# Read entire file
df_excel = pd.read_excel('data.xlsx')

# Read specific sheet
df_sheet = pd.read_excel('data.xlsx', sheet_name='Sheet1')

# Read multiple sheets
df_dict = pd.read_excel('data.xlsx', sheet_name=None)  # All sheets
for sheet_name, df in df_dict.items():
    print(f"Sheet: {sheet_name}, Shape: {df.shape}")

# With parameters
df = pd.read_excel(
    'data.xlsx',
    sheet_name=0,
    header=0,
    usecols='A:D',          # Select columns A-D
    dtype={'ID': str}
)
```

**Step 5.2:** Handling multiple sheets

```python
# Read specific sheet by name
df = pd.read_excel('data.xlsx', sheet_name='Sales')

# Read sheet by index
df = pd.read_excel('data.xlsx', sheet_name=2)

# Combine multiple sheets
xls = pd.ExcelFile('data.xlsx')
dfs = []
for sheet in xls.sheet_names:
    df_temp = pd.read_excel('data.xlsx', sheet_name=sheet)
    dfs.append(df_temp)

df_combined = pd.concat(dfs, ignore_index=True)
```

---

### Phase 6: Reading SQL Databases

**Step 6.1:** SQLite Database

```python
import sqlite3

# Connect to database
conn = sqlite3.connect('database.db')

# Read data from SQL query
df_sql = pd.read_sql_query('SELECT * FROM users', conn)

# Specify data types
df_sql = pd.read_sql_query(
    'SELECT * FROM users',
    conn,
    dtype={'id': int, 'name': str}
)

conn.close()
```

**Step 6.2:** Using SQLAlchemy (more flexible)

```python
from sqlalchemy import create_engine

# Create engine
engine = create_engine('sqlite:///database.db')

# Read from database
df_sql = pd.read_sql_table('users', engine)

# From SQL query
df_sql = pd.read_sql_query('SELECT * FROM users WHERE age > 25', engine)

# Get all table names
table_names = engine.table_names()
print(f"Available tables: {table_names}")
```

---

### Phase 7: Data Validation & Comparison

**Step 7.1:** Validate loaded data

```python
def validate_data(df, name):
    print(f"\n📊 Validation Report for {name}:")
    print(f"  Shape: {df.shape}")
    print(f"  Data Types: {df.dtypes.unique()}")
    print(f"  Missing Values: {df.isnull().sum().sum()}")
    print(f"  Duplicates: {df.duplicated().sum()}")
    print(f"  Memory Usage: {df.memory_usage(deep=True).sum() / 1024:.2f} KB")
    
# Compare files loaded from different formats
validate_data(df_csv, "CSV")
validate_data(df_json, "JSON")
validate_data(df_xml, "XML")
```

**Step 7.2:** Performance comparison

```python
import time

formats = {
    'CSV': ('data.csv', pd.read_csv),
    'JSON': ('data.json', pd.read_json),
    'Excel': ('data.xlsx', pd.read_excel)
}

results = {}
for format_name, (file_path, read_func) in formats.items():
    start = time.time()
    df_temp = read_func(file_path)
    elapsed = time.time() - start
    results[format_name] = {
        'Time (s)': elapsed,
        'Size (MB)': df_temp.memory_usage(deep=True).sum() / (1024*1024)
    }

print(pd.DataFrame(results).T)
```

---

### Phase 8: Practical Examples

**Step 8.1:** Real-world example - Multiple format loading

```python
# Load data from different sources
df_sales_csv = pd.read_csv('sales_data.csv')
df_customers_json = pd.read_json('customers.json')
df_inventory_excel = pd.read_excel('inventory.xlsx')

# Merge datasets
df_merged = df_sales_csv.merge(
    df_customers_json[['customer_id', 'name']],
    on='customer_id'
).merge(
    df_inventory_excel[['product_id', 'stock']],
    on='product_id'
)

print(f"Combined dataset shape: {df_merged.shape}")
```

**Step 8.2:** Create reusable data loader

```python
def load_dataset(file_path):
    \"\"\"Automatically detect and load dataset\"\"\"
    ext = file_path.split('.')[-1].lower()
    
    if ext == 'csv':
        return pd.read_csv(file_path)
    elif ext == 'json':
        return pd.read_json(file_path)
    elif ext in ['xlsx', 'xls']:
        return pd.read_excel(file_path)
    elif ext == 'xml':
        return pd.read_xml(file_path)
    else:
        raise ValueError(f"Unsupported format: {ext}")

# Usage
df = load_dataset('data.csv')
```

---

## Practical Tests

### Test 1: CSV Loading
```python
assert df_csv.shape[0] > 0
assert df_csv.isnull().sum().sum() < len(df_csv)
print("✅ CSV Test PASSED")
```

### Test 2: JSON Parsing
```python
assert df_json.shape == df_csv.shape
print("✅ JSON Test PASSED")
```

### Test 3: Excel Reading
```python
assert len(df_excel.columns) > 0
print("✅ Excel Test PASSED")
```

### Test 4: Data Consistency
```python
assert df_csv.shape[0] == df_json.shape[0]
print("✅ Consistency Test PASSED")
```

### Test 5: SQL Query
```python
assert len(df_sql) > 0
print("✅ SQL Test PASSED")
```

---

## Expected Results

| Format | Read Time | Memory | Status |
|--------|-----------|--------|--------|
| CSV | Fast | Low | ✅ |
| JSON | Medium | Medium | ✅ |
| XML | Slow | High | ✅ |
| Excel | Medium | Medium | ✅ |
| SQL | Medium | Depends | ✅ |

---

## Troubleshooting

### Issue: "UnicodeDecodeError"
**Solution:** Try different encodings (utf-8, latin-1, iso-8859-1)

### Issue: "ModuleNotFoundError: openpyxl"
**Solution:** `pip install openpyxl`

### Issue: "No such table" (SQL)
**Solution:** Check database name and table names using `engine.table_names()`

### Issue: JSON not nested correctly
**Solution:** Use `pd.json_normalize()` for nested JSON

### Issue: "XML element not found"
**Solution:** Verify XML structure with `xmllint` or pretty print the XML

---

## Submission Files

- [ ] `Practical_3_Complete_Notebook.ipynb`
- [ ] `SUBMISSION_TEMPLATE_Practical_3.md`
- [ ] Sample datasets (CSV, JSON, XML, Excel)
- [ ] Screenshots (3-4)

---

**Version:** 1.0 | **Course:** 316316 - Machine Learning | **Next:** Practical 4 - Classification

