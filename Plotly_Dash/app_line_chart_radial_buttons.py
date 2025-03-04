# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv(r'C:\Users\erick\OneDrive\Desktop\Python\Data\StockData.csv')

# Ensure the date column is formatted as a date
df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y', errors='coerce')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

#sort data
df = df.sort_values(by='date')

# Initialize the app
app = Dash()

#create list for the radio options
options_list = []
for stock in df['stock'].unique():            # outputs a unique list of stock tickers to loop through
    option = {'label': stock, 'value':stock}  # option requires a label and value which are the dictionary inputs
    options_list.append(option)               # appends the dictionaries back into the options_list dictionary

# App layout represents the app components that will be displayed in the web browser
# dcc is needed for both the Radio Items and the Graph
app.layout = html.Div([
    html.H1(children='Stock Data Dashboard'),  # Title
    html.Hr(),
    
    # Radio buttons for selecting stock ticker
    dcc.RadioItems(
        options=options_list, 
        value=df['stock'].iloc[0],  # Default selection: first ticker in dataset
        id='controls-and-radio-item'
    ),
    
    # Data Table displaying stock data
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    
    # Graph to display stock price trend
    dcc.Graph(figure={}, id='control-and-graph')
])
              
# Add controls to build the interaction. Input is the data which is the value property labeled as controls and radio item.  
# Output is the figure property of the component id control and groph.  The fig is currently empty.
# Callback function's argument is stock_selected and refers to value=AAPL above (AAPL is the default)
@callback(
    Output('control-and-graph', 'figure'),
    Input('controls-and-radio-item', 'value')
)
def update_graph(stock_selected):
    # Filter data
    filtered_df = df[df['stock'] == stock_selected].copy()

    # Debugging: Print filtered data in the terminal
    print(f"Filtered data for {stock_selected}: {len(filtered_df)} rows")
    print(filtered_df.head())  # Show first few rows

    # Ensure 'date' is formatted correctly for Plotly
    filtered_df['date'] = filtered_df['date'].dt.strftime('%Y-%m-%d')

    # Create the Plotly line chart
    fig = px.line(
        filtered_df, x='date', y='price',
        title=f'Stock Price of {stock_selected}'
    )

    return fig


# Run the app.  This will be the same for almast all dash boards created
if __name__ == '__main__':
    app.run(debug=True)
