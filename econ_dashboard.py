import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from FRED_API import fetch_fred_data  

# 🏁 Streamlit UI
st.set_page_config(page_title="Economic Dashboard", layout="wide")

# 📅 Define available years
years = list(range(2000, 2026))

st.title("📊 Economic Indicator Dashboard")
st.write("Compare economic indicators over time and analyze Year-over-Year (YoY) trends.")

# 📌 User selects start and end year
col1, col2, _ = st.columns([1, 1, 8])  # Smaller dropdowns for year selection
with col1:
    start_year = st.selectbox("Start Year", years, index=0)
with col2:
    end_year = st.selectbox("End Year", years, index=len(years)-1)

# 🔄 Ensure start year is before end year
if start_year > end_year:
    st.error("⚠ Start year must be before end year.")
    st.stop()

# Convert years to full date format for API request
start_date = f"{start_year}-01-01"
end_date = f"{end_year}-12-31"

@st.cache_data
def get_fred_data(start_date, end_date):
    """Fetch and cache economic data from FRED."""
    return fetch_fred_data(start_date=start_date, end_date=end_date)

# Fetch data
df = get_fred_data(start_date, end_date)

# ❌ Stop if DataFrame is empty
if df.empty:
    st.error("⚠ No data retrieved. Try adjusting the year range.")
    st.stop()

df = df.sort_index()

# 📌 Dropdown for Selecting Two Variables
available_variables = df.columns.tolist()

st.subheader("📊 Compare Two Economic Indicators & YoY Trends")

col1, col2 = st.columns(2)
with col1:
    primary_variable = st.selectbox("Select Primary Indicator (Left Axis)", available_variables, index=0)
with col2
