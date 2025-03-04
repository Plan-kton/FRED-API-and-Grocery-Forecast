# Import packages
from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv(r'C:\Users\erick\OneDrive\Desktop\Python\Data\StockData.csv')

# Ensure the date column is formatted correctly
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Sort data by date
df = df.sort_values(by='date')

# Initialize the Dash app
app = Dash()

# Create a list of stock options for the dropdown
options_list = [{'label': stock, 'value': stock} for stock in df['stock'].unique()]

# App layout WITHOUT the table
app.layout = html.Div([
    html.H1(children='Stock Data Dashboard'),  # Title
    html.Hr(),
    
    # Dropdown for selecting multiple stocks
    dcc.Dropdown(
        options=options_list, 
        value=[df['stock'].iloc[0]],  # Default selection: First stock in dataset
        id='stock-selector',
        multi=True  # Enable multiple selections
    ),
    
    # Graph to display stock price trends
    dcc.Graph(figure={}, id='stock-price-graph')
])
              
# Callback to update the graph based on stock selection
@callback(
    Output('stock-price-graph', 'figure'),
    Input('stock-selector', 'value')
)
def update_graph(selected_stocks):
    # Filter data for selected stocks
    filtered_df = df[df['stock'].isin(selected_stocks)].copy()

    # Debugging: Print filtered data in the terminal
    print(f"Filtered data for stocks {selected_stocks}: {len(filtered_df)} rows")
    print(filtered_df.head())  # Show first few rows

    # Convert date format for Plotly
    filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

    # Create a line chart with multiple stocks
    fig = px.line(
        filtered_df, x='date', y='price', color='stock',  # Differentiate stocks by color
        title=f'Stock Price Trends for {", ".join(selected_stocks)}'
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
