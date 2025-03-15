# 📌 ARIMA Cheat Sheet: Time Series Forecasting in Python

## **1️⃣ Import Required Libraries**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima
from sklearn.metrics import mean_absolute_error, mean_squared_error
```

## **2️⃣ Load and Visualize the Time Series**
```python
# Load your dataset (assuming 'Date' is the index and 'grocery_sales' is the target)
df = pd.read_csv("your_data.csv", parse_dates=["Date"], index_col="Date")

# Plot the time series
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df["grocery_sales"], label="Grocery Sales", color="blue")
ax.set_xlabel("Month")
ax.set_ylabel("Grocery Sales (in units)")
ax.set_title("Grocery Sales Time Series")
ax.legend()
plt.show()
```

## **3️⃣ Check for Stationarity (ADF Test)**
```python
def adf_test(series):
    result = adfuller(series)
    print("ADF Statistic:", result[0])
    print("p-value:", result[1])
    print("Critical Values:", result[4])
    
    if result[1] < 0.05:
        print("The series is stationary (reject H0). No differencing needed.")
    else:
        print("The series is NOT stationary (fail to reject H0). Differencing is needed.")

# Run the ADF test
adf_test(df["grocery_sales"])
```

## **4️⃣ Apply First Differencing (if needed)**
```python
df["grocery_sales_diff"] = df["grocery_sales"].diff()
df.dropna(inplace=True)  # Remove NaNs after differencing

# Plot the first difference
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df["grocery_sales_diff"], label="First Difference", color="red", linestyle="dashed")
ax.set_xlabel("Month")
ax.set_ylabel("Grocery Sales First Difference")
ax.set_title("First Differenced Time Series")
ax.legend()
plt.show()

# Re-run ADF test to confirm stationarity
adf_test(df["grocery_sales_diff"])
```

## **5️⃣ Find the Best ARIMA Model with Auto-ARIMA**
```python
auto_model = auto_arima(df["grocery_sales_diff"], 
                        seasonal=False,  # We removed seasonality
                        trace=True, 
                        suppress_warnings=True)

# Print optimal (p, d, q)
print("Best ARIMA Order:", auto_model.order)
```

## **6️⃣ Split Data into Training & Testing Sets**
```python
# Define training (2004-2023) and test (2024) sets
train_diff = df.loc[:'2023-12-31', "grocery_sales_diff"]
test_diff = df.loc['2024-01-31':, "grocery_sales_diff"]

print(f"Training Size: {len(train_diff)}, Test Size: {len(test_diff)}")
```

## **7️⃣ Initialize and Fit ARIMA Model**
```python
# Fit ARIMA with optimal parameters (replace with best order from auto_arima)
model_diff = ARIMA(train_diff, order=(3,0,1))  # d=0 since we manually differenced
arima_result_diff = model_diff.fit()

# Print model summary
print(arima_result_diff.summary())
```

## **8️⃣ Analyze Model Residuals**
```python
# Plot residuals
residuals = arima_result_diff.resid
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(residuals, label="Residuals", color="black")
ax.axhline(0, linestyle="dashed", color="gray")
ax.set_xlabel("Month")
ax.set_ylabel("Residuals")
ax.set_title("ARIMA Model Residuals")
ax.legend()
plt.show()

# Residual diagnostics
arima_result_diff.plot_diagnostics(figsize=(12,8))
plt.show()
```

## **9️⃣ Extract Fitted Values (In-Sample Predictions)**
```python
# Compare fitted values with actual first differences
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(train_diff.index, train_diff, label="Actual First Difference", color="blue")
ax.plot(train_diff.index, arima_result_diff.fittedvalues, 
        label="Fitted First Difference", color="red", linestyle="dashed")

ax.set_xlabel("Month")
ax.set_ylabel("First Difference")
ax.set_title("ARIMA Fitted vs. Actual")
ax.legend()
plt.show()
```

## **🔟 Generate First-Difference Forecast for 2024**
```python
# Forecast first differences for 2024
forecast_result = arima_result_diff.get_forecast(steps=len(test_diff))

# Extract first-difference predictions
forecast_df = pd.DataFrame(forecast_result.predicted_mean, 
                           index=test_diff.index, 
                           columns=["Forecasted_Sales_Diff"])

# Print forecasted first differences
print(forecast_df.head())
```

## **1️⃣1️⃣ Plot First-Difference Forecast vs Actual**
```python
fig, ax = plt.subplots(figsize=(12, 6))

# Plot actual first differences (blue)
ax.plot(test_diff.index, test_diff, label="Actual First Difference", color="blue")

# Plot forecasted first differences (red, dashed)
ax.plot(forecast_df.index, forecast_df["Forecasted_Sales_Diff"], 
        label="Forecasted First Difference", color="red", linestyle="dashed")

# Plot confidence intervals
ax.plot(forecast_result.predicted_mean.index, forecast_result.conf_int().iloc[:, 0], 
        label="Lower Confidence Interval", color="black", linestyle="dotted")
ax.plot(forecast_result.predicted_mean.index, forecast_result.conf_int().iloc[:, 1], 
        label="Upper Confidence Interval", color="black", linestyle="dotted")

ax.set_xlabel("Month")
ax.set_ylabel("First Difference")
ax.set_title("First Difference Forecast vs Actual")
ax.legend()
plt.show()
```

## **1️⃣2️⃣ Convert First-Difference Forecast Back to Original Sales**
```python
# Get the last known actual value from 2023-12-31
last_actual_value = df.loc['2023-12-31', "grocery_sales"]

# Reverse differencing to restore actual sales values
forecast_df["Forecasted_Sales"] = last_actual_value + forecast_df["Forecasted_Sales_Diff"].cumsum()

# Print restored forecasted sales
print(forecast_df.head())
```

## **1️⃣3️⃣ Evaluate Forecast Accuracy**
```python
# Compute error metrics
mse = mean_squared_error(test_diff, forecast_df["Forecasted_Sales_Diff"])
mae = mean_absolute_error(test_diff, forecast_df["Forecasted_Sales_Diff"])

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
```

# 🎯 **Final Thoughts**
- ✅ This cheat sheet provides a structured workflow for **ARIMA-based time series forecasting**.
- ✅ Modify the code as needed for your dataset.
- ✅ Now you can confidently forecast grocery sales with ARIMA! 🚀
