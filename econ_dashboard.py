import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from FRED_API import fetch_fred_data  

# 📅 Define available years
years = list(range(2000, 2026))

# 🏁 Streamlit UI
st.set_page_config(page_title="Economic Dashboard", layout="wide")

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
with col2:
    secondary_variable = st.selectbox("Select Secondary Indicator (Right Axis)", available_variables, index=1)

if primary_variable == secondary_variable:
    st.error("⚠ Please select two different indicators for comparison.")
    st.stop()

df_yoy = df.ffill().pct_change(periods=12) * 100  # YoY percentage change

# 🎨 Dual-Chart Layout
col1, col2 = st.columns(2)

# 📊 Absolute Values Chart
with col1:
    st.subheader("📊 Absolute Values Comparison")

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df.index, y=df[primary_variable], name=primary_variable, mode="lines"))
    fig1.add_trace(go.Scatter(x=df.index, y=df[secondary_variable], name=secondary_variable, mode="lines", yaxis="y2"))

    fig1.update_layout(
        title=f"{primary_variable} vs {secondary_variable} Over Time",
        xaxis=dict(title="Date", type="date"),
        yaxis=dict(title=primary_variable, side="left", showgrid=False),
        yaxis2=dict(title=secondary_variable, side="right", overlaying="y", showgrid=False),
        legend=dict(x=0, y=1),
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig1, use_container_width=True)

# 📊 YoY % Change Chart
with col2:
    st.subheader("📈 Year-over-Year (YoY) Change Comparison")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_yoy.index, y=df_yoy[primary_variable], name=f"{primary_variable} YoY % Change", mode="lines"))
    fig2.add_trace(go.Scatter(x=df_yoy.index, y=df_yoy[secondary_variable], name=f"{secondary_variable} YoY % Change", mode="lines", yaxis="y2"))

    fig2.update_layout(
        title=f"YoY % Change: {primary_variable} vs {secondary_variable}",
        xaxis=dict(title="Date", type="date"),
        yaxis=dict(title=f"{primary_variable} YoY %", side="left", showgrid=False),
        yaxis2=dict(title=f"{secondary_variable} YoY %", side="right", overlaying="y", showgrid=False),
        legend=dict(x=0, y=1),
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)

# 📥 Download data button
st.download_button(
    label="📥 Download Monthly Data as CSV",
    data=df.to_csv(index=True),
    file_name="economic_data_monthly.csv",
    mime="text/csv"
)

st.write("Data source: [FRED API](https://fred.stlouisfed.org/)")
