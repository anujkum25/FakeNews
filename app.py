import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='HomePage', children=[
            html.H2(children='Fake News Detection From Newspaper and Social Media'),

            dcc.Markdown('''
            Choose Input Type
            '''),  
            dcc.RadioItems(
                options=[
                    {'label': 'URL', 'value': 'url'},
                    {'label': 'Text', 'value': 'text'}],
                    value='text',labelStyle={'display': 'inline-block'}),
            
            html.Br(),
            
            dcc.Textarea(id='textarea1',
                    value='copy paste your text here to analyse',
                    style={'width': '80%', 'height': 200}),
            
            html.Div(id='textarea1_op', style={'whiteSpace': 'pre-line'}),
            
            html.Button('Submit', id='submit-val', n_clicks=0)
            ]),
            
            dcc.Tab(label='ResultPage', children=[
                
            ]),
            
            dcc.Tab(label='Visualization', children=[
                dcc.Graph(
                figure={
                    'data': [
                        {'x': ["Accuracy", "Precision", "Recall"], 'y': [0.99, 0.95, .84],
                            'type': 'bar', 'name': 'Roberta'},
                        {'x': ["Accuracy", "Precision", "Recall"], 'y': [0.98,0.9, 0.88],
                         'type': 'bar', 'name': 'Bert'},
                    ]
                }
            )

            ])
    ])
])



if __name__ == '__main__':
    app.run_server(debug=True)