#from pyngrok import ngrok

#ngrok.kill()

# Set your ngrok authtoken
#ngrok.set_auth_token("2f5UKKBSHXSOAgtBDaWxNWdmBda_5H6XLeApTZgFAdtNWVydb")

# Start an HTTP tunnel on port 80
#tunnel = ngrok.connect(addr='http://127.0.0.1:8050/') #127.0.0.1:8000, http://127.0.0.1:80, localhost:8080

#print(tunnel,"To go to the dashboard please click the link web site .ngrok-free.app.")


#from jupyter_dash import JupyterDash
#import dash_cytoscape as cyto
import dash
from dash import dcc #import dash_core_components as dcc 
from dash import html #import dash_html_components as html 
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
#from dash import no_update

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = JupyterDash(__name__) #, external_stylesheets=external_stylesheets, server_url=tunnel.public_url)

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("D:\\01. March to dec 2024\\00. Body of Knowledge\\01. Courses\\01. IBM Applied Data Science Specialization\\05. Applied Data Science Capstone\\Week 5\\Notebook\\spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Add a dropdown list to enable Launch Site selection
    # The default select value is for ALL sites
    # dcc.Dropdown(id='site-dropdown',...)
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'Cape Canaveral Launch Complex 40 (CAFS LC-40)', 'value': 'CCAFS LC-40'},
            {'label': 'Cape Canaveral Space Launch Complex 40 (CCAFS SLC-40)', 'value': 'CCAFS SLC-40'},
            {'label': 'Kennedy Space Center Launch Complex 39A (KSC LC-39A)', 'value': 'KSC LC-39A'},
            {'label': 'Vandenberg Air Force Base Space Launch Complex (VAFB SLC-4E)', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True
    ),

    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    # If a specific launch site was selected, show the Success vs. Failed counts for the site
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Add a slider to select payload range
    # dcc.RangeSlider(id='payload-slider',...)

    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    # marks={0: '0', 100: '100'},
                    value=[min_payload, max_payload]),

    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
    ])


# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
# Place to add @app.callback Decorator
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        filtered_df = spacex_df.groupby(['Launch Site']).size().reset_index(name='counts')
        filtered_df['outcome'] = filtered_df['counts'].apply(lambda x: 'Success' if x > 0 else 'Failure')
        return px.pie(filtered_df, values='counts', names='outcome', title='Launch Success Rate For All Sites')
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        filtered_df['outcome'] = filtered_df['class'].apply(lambda x: 'Success' if x == 1 else 'Failure')
        filtered_df = filtered_df.groupby('outcome').size().reset_index(name='counts')
        return px.pie(filtered_df, values='counts', names='outcome', title='Launch Success Rate For ' + entered_site)



# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(entered_site, slider):
    filtered_df = spacex_df[
        (slider[0] <= spacex_df['Payload Mass (kg)']) & (spacex_df['Payload Mass (kg)'] <= slider[1])
    ]
    if entered_site == 'ALL':
        return px.scatter(filtered_df,
                          x='Payload Mass (kg)', y='class',
                          color='Booster Version Category',
                          title='Launch Success Rate For All Sites')
    # return the outcomes in pie chart for a selected site
    filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
    filtered_df['outcome'] = filtered_df['class'].apply(lambda x: 'Success' if (x == 1) else 'Failure')
    filtered_df['counts'] = 1
    return px.scatter (filtered_df,
                       x='Payload Mass (kg)', y='class',
                       color='Booster Version Category',
                       title='Launch Success Rate For ' + entered_site)


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
#print(tunnel,"To go to the dashboard please click the link web site .ngrok-free.app.")