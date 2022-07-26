######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import os

###### Set up variables
list_of_choices=['Bulbasaur', 'Squirtle', 'Charmander']
githublink = 'https://github.com/manueldelreal/201-chuck-norris-callback'
image1='bulbasaur.png'
image2='squirtle.png'
image3='charmander.png'
heading1='Choose your starter'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Pokemon starters'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(src=app.get_asset_url(image1), style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices],
                value='Bulbasaur',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'Great choice going with a {whatever_you_chose}.'


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
