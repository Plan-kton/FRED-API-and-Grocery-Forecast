This code does a few things...
1) Connects with the FRED database (Federal Reserve Bank, St. Louis) to download the data via API
2) Merges the data which is a combination of daily, weekly, monthly and quarterly data
3) Data is normalized into monthly buckets.  Some of the aggregated data is summed and some is averaged based on the data
4) Then the data is explored for missing data, duplicates, and outliers.
5) The data is also visualized and explored to understand relationships
6) Finally, feature engineering is applied to create lags and dummy variables
7) Then three regression models are run to forecast U.S. Grocery Sales - OLS, Ridge, and ARIMA
8) They the results are compiled and visualized to see which version performed the best
