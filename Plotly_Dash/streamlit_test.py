import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="📈 Multi-Stock Price Dashboard", layout="wide")

# Title of the dashboard
st.title("📈 Multi-Stock Price Dashboard")

# Sidebar for stock selection
st.sidebar.header("Select Stocks")

# List of stock options
stock_list = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

# Multi-select dropdown for choosing stocks
selected_stocks = st.sidebar.multiselect("Choose stocks:", stock_list, default=["AAPL"])

# Function to fetch stock data from Yahoo Finance
@st.cache_data
def fetch_stock_data(symbols):
    stock_data = []
    for stock in symbols:
        df = yf.Ticker(stock).history(period="1y", interval="1d")  # 1 year of daily data
        df = df[['Close']].reset_index()  # Keep only Date and Close columns
        df['Stock'] = stock  # Add stock column
        stock_data.append(df)
    
    return pd.concat(stock_data, ignore_index=True) if stock_data else pd.DataFrame(columns=["Date", "Close", "Stock"])

# Fetch data for selected stocks
df = fetch_stock_data(selected_stocks)

# Display stock data table
st.subheader(f"📊 Latest Data for Selected Stocks")
st.dataframe(df.tail(10))  # Show last 10 rows

# Ensure Date column is formatted correctly
if not df.empty:
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

    # Create and display the line chart
    st.subheader(f"📉 Stock Price Trends")
    fig = px.line(df, x="Date", y="Close", color="Stock", title="Stock Price Trends for Selected Stocks")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ No data available. Please select at least one stock.")




