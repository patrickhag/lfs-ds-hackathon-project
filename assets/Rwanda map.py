import geopandas as gpd
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
# Load the shapefile
shapefile_path = r"C:\Users\user\OneDrive\Documents\python works\Rwanda.shp"
gdf = gpd.read_file(shapefile_path)
gdf.rename(columns={'ADM2_EN': 'Districts'}, inplace=True)

# Load the employment data
employment_data_path = r"C:\Users\user\OneDrive\Documents\python works\Districts.xlsx"
employment_df = pd.read_excel(employment_data_path)

# Merge the dataframes on the 'Districts' column
merged_df = pd.merge(gdf, employment_df, on='Districts', how='left')

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout
app.layout = html.Div([
    html.Div([
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3("Select Status:",style={'fontSize':'16px'})
                ],className='m-2'),
                # Dropdown for selecting the variable to display on the map
                dcc.Dropdown(
                    id='variable-dropdown',
                    options=[
                        {'label': 'Employed', 'value': 'Employed'},
                        {'label': 'Unemployed', 'value': 'Unemployed'},
                        {'label': 'Outside Labour Force', 'value': 'Outside_labour_force'}
                    ],
                    value='Employed',
                    style={
                        'width': '50%',
                        'textAlign': 'center',
                        'fontSize': '15px',  # Adjust font size
                        'borderRadius': '8px',  # Add rounded corners 
                        },
                    clearable=False,
                    searchable=False,
                    className='m-2'
                ),
            ]),
        ]),
        # Map
    dcc.Graph(id='map'),
    ], style={'border': '2px solid #ccc', 'boxShadow': '0px 4px 8px rgba(0, 0, 0, 0.1)'}),
    
    
    
])

# Callback to update the map based on the selected variable
@app.callback(
    Output('map', 'figure'),
    [Input('variable-dropdown', 'value')]
)
def update_map(selected_variable):
    fig = px.choropleth_mapbox(
        merged_df,
        geojson=gdf.geometry,
        locations=merged_df.index,
        color=selected_variable,
        color_continuous_scale="Viridis",
        hover_name='Districts',
        mapbox_style="carto-positron",
        center={"lat": -1.9403, "lon": 29.8739},  # Set to a location within Rwanda
        # zoom=8,  # Adjust the zoom level as needed
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
