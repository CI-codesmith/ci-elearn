# MICROPROJECT ADVANCED 3: Time Series Forecasting with ARIMA and LSTM

**Course:** 316316 - Machine Learning  
**Level:** Advanced (For High-Performing Students)  
**Duration:** 3 weeks  
**Submission:** Jupyter Notebook + Code + Trained Models + Report  
**Weight:** 20% of course assessment

---

## 🎯 Objective
Master time series analysis and forecasting using both traditional (ARIMA) and deep learning (LSTM) approaches. Compare methods and apply to real-world datasets like stock prices, weather, or energy consumption.

---

## 📋 Requirements

### Phase 1: Time Series Data Analysis
- **Real-world dataset:** Choose from stock prices, weather data, energy consumption, or cryptocurrency
  - Examples: Yahoo Finance, OpenWeatherMap, OpenPower, Kaggle time series datasets
  - Minimum 365+ data points for meaningful analysis
- **EDA:** Visualize time series, identify trends, seasonality, stationarity
- **Statistical tests:** 
  - Autocorrelation (ACF) and Partial Autocorrelation (PACF) plots
  - Augmented Dickey-Fuller (ADF) test for stationarity
  - Decomposition (trend, seasonal, residual)
- **Data preprocessing:** Handle missing values, normalize/scale data appropriately

### Phase 2: ARIMA Model Development
- **Stationarity:** Transform data if needed (differencing, log transformation)
- **Parameter selection:** Determine (p, d, q) using ACF/PACF plots and AIC/BIC
- **Model building:** Implement ARIMA using statsmodels
- **Diagnostics:** Check residuals for white noise properties
- **Baseline forecasting:** Generate forecasts for test period

### Phase 3: LSTM Neural Network Development
- **Architecture design:** 
  - Input layer → LSTM layers (1-3 layers) → Dense layer → Output
  - Add dropout and batch normalization for regularization
  - Visualize architecture
- **Sequence preparation:** Create sliding windows for time series
- **Training:** Implement with proper validation strategy
- **Hyperparameter tuning:** 
  - Number of LSTM units
  - Number of layers
  - Dropout rates
  - Learning rate scheduling

### Phase 4: Advanced Techniques (Choose 2+)
- **Ensemble methods:** Combine ARIMA and LSTM predictions
- **Multivariate forecasting:** Include exogenous variables (temperature → energy usage)
- **Attention mechanisms:** Implement attention-based LSTM
- **Bidirectional LSTM:** Use backward temporal information
- **Seasonal decomposition:** Separate seasonal component before forecasting

### Phase 5: Model Comparison & Evaluation
- **Forecasting metrics:**
  - MAE (Mean Absolute Error)
  - RMSE (Root Mean Squared Error)
  - MAPE (Mean Absolute Percentage Error)
  - Directional accuracy (correct trend prediction)
- **Visualization:** Plot actual vs. predicted with confidence intervals
- **Residual analysis:** Check for autocorrelation in residuals
- **Performance comparison:** ARIMA vs. LSTM vs. Ensemble
- **Benchmark:** Compare against naive baseline and moving average

### Phase 6: Deployment & Real-World Application
- **Production model:** Select best model based on evaluation
- **Inference pipeline:** Create script for continuous forecasting
- **Uncertainty quantification:** Provide confidence intervals with forecasts
- **Monitoring:** Plan for model retraining as new data arrives
- **Scalability:** Discuss how to scale to multiple time series

---

## 📤 Deliverables

### 1. Jupyter Notebook (35%)
- **File:** `MICROPROJECT_ADV3_TimeSeries_Forecasting.ipynb`
- Complete EDA with visualizations
- ARIMA and LSTM implementations
- Model comparison and performance analysis
- Well-documented code with markdown explanations

### 2. Model Code (20%)
- **File:** `MICROPROJECT_ADV3_models.py`
- ARIMA model class with fitting and forecasting
- LSTM model class using TensorFlow/PyTorch
- Data preprocessing and feature engineering functions
- Evaluation metrics implementation

### 3. Forecasting Script (15%)
- **File:** `MICROPROJECT_ADV3_forecast.py`
- Load trained models and generate forecasts
- Produce forecasts with confidence intervals
- Visualization of forecasts
- Example usage and documentation

### 4. Comprehensive Report (20%)
- **File:** `MICROPROJECT_ADV3_Report.pdf` (5-10 pages)
- Time series problem description and dataset details
- Statistical analysis and preprocessing approach
- ARIMA methodology and parameter selection
- LSTM architecture and training details
- Results, comparisons, and interpretation
- Advanced techniques employed
- Limitations and future improvements

### 5. Presentation Slides (10%)
- **File:** `MICROPROJECT_ADV3_Presentation.pdf`
- 15-20 slides with time series visualizations
- Model architectures and results
- Key findings and insights
- Business implications

---

## 📊 Evaluation Rubric

| Criteria | Excellent (5) | Good (4) | Satisfactory (3) | Poor (1-2) |
|----------|---------------|----------|------------------|------------|
| **Time Series Analysis** | Thorough, insights into patterns | Good EDA, clear understanding | Basic analysis | Insufficient |
| **ARIMA Implementation** | Proper parameter selection, diagnostics | Good model building | Basic implementation | Poor approach |
| **LSTM Architecture** | Sophisticated design, well-justified | Good architecture, reasonable | Basic LSTM | Poor design |
| **Model Training** | Proper validation, optimization | Good training strategy | Basic training | Incomplete |
| **Evaluation & Comparison** | Comprehensive analysis, clear insights | Good metrics and comparison | Basic evaluation | Incomplete |
| **Advanced Techniques** | 2+ techniques well-implemented | 1-2 techniques | Mentioned | Missing |
| **Code Quality** | Production-ready, modular, clear | Good structure, well-documented | Functional | Messy/broken |
| **Report Quality** | Excellent insights, professional | Good documentation | Basic summary | Poor docs |

**Total:** /40

---

## 🆘 Resources

### Libraries & Tools
- **Time Series:** Statsmodels (ARIMA, decomposition)
- **Deep Learning:** TensorFlow/Keras or PyTorch
- **Data:** Pandas, NumPy
- **Visualization:** Matplotlib, Plotly, Seaborn
- **Utilities:** Scikit-learn for preprocessing

### Datasets
- [Yahoo Finance](https://finance.yahoo.com/) - Stock prices
- [Kaggle Time Series](https://www.kaggle.com/datasets?tags=time-series)
- [OpenWeatherMap](https://openweathermap.org/) - Weather data
- [UCI Time Series](https://archive.ics.uci.edu/ml/)
- [Crypto datasets](https://www.coinbase.com/price/) - Cryptocurrency

### Learning Resources
- ARIMA/SARIMA documentation and tutorials
- LSTM for time series tutorials
- Statsmodels documentation
- Time series forecasting best practices

---

## 💡 Tips for Success

1. **Understand the data:** Spend time on EDA to understand patterns
2. **Check stationarity:** This is crucial for ARIMA success
3. **ACF/PACF plots:** Learn to read these to determine (p,d,q)
4. **Validate on test set:** Always hold out test data for unbiased evaluation
5. **Ensemble approach:** Combining ARIMA and LSTM often works best
6. **Document experiments:** Keep track of different parameter configurations
7. **Consider domain knowledge:** Incorporate business logic into your models

---

## 📅 Milestone Timeline

- **Week 1:** Data analysis, stationarity testing, ARIMA parameter selection
- **Week 2:** LSTM implementation, training, hyperparameter tuning
- **Week 3:** Model comparison, advanced techniques, report and presentation

---

**Deadline:** 3 weeks from project start  
**Submission Platform:** Course portal (Jupyter + Code + Trained models + Report)
