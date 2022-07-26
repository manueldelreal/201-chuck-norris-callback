######### Import your libraries #######
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import os

###### Set up variables
list_of_choices=[
    {
        "label": "Bulbasaur",
        "action": "https://c.tenor.com/6GYLcQPTRHgAAAAi/bulbizarre-bulbasaur.gif"
    },
    {
        "label": "Squirtle",
        "action": "https://c.tenor.com/8HPP7RwhVjgAAAAi/pok%C3%A9mon-happy.gif"
    },
    {
        "label": "Charmander",
        "action": "https://giffiles.alphacoders.com/257/257.gif"
    }
]
githublink = 'https://github.com/manueldelreal/201-chuck-norris-callback'
heading1='Choose your starter'
image1='https://www.serebii.net/pokemonmasters/syncpairs/professoroak.png'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Pokemon starters'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=image1, style={'width': 'auto', 'height': 'auto'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i["label"], 'value': choi} for choi,i in enumerate(list_of_choices)],
                value=0,
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Img(src='', style={'width': '50%', 'height':'50%'}, id='action'),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback([Output('your-output-here', 'children'), Output('action', 'src')],
              [Input('your-input-here', 'value')])
def display_value(choice):
    label = list_of_choices[choice]["label"]
    action = list_of_choices[choice]["action"]
    return f'Great choice going with a {label}.', action


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)