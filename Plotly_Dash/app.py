from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

# Sample static data
df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Close': [100 + i for i in range(10)],
    'Stock': ['AAPL'] * 10
})

# Initialize Dash
app = Dash()

app.layout = html.Div([
    html.H1("Test Line Chart"),
    dcc.Graph(id='test-graph'),
])

# Simple callback to display the graph
@app.callback(
    Output('test-graph', 'figure'),
    Input('test-graph', 'id')  # Dummy input to trigger callback
)
def update_graph(_):
    fig = px.line(df, x='Date', y='Close', title="Test Stock Data")
    return fig

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)