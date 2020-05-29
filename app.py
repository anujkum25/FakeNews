import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
import dash_table
import pandas as pd
from evaluation import evaluate_model

'''
Many stuff in this file is hard-coded, to be chnaged later
'''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df= pd.read_csv(".\Data\confusion_matrix.csv")

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
            
            html.Button('Submit', id='submit-val', type='submit')
            ]),
            
            dcc.Tab(label='ResultPage', children=[
                html.Div(id='textarea-output', style={'whiteSpace': 'pre-line'})
            ]),
            
            dcc.Tab(label='Visualization', children=[
                
                html.Br(),
                
                dcc.Markdown('''
                             Comparison between Roberta_most_accurate and Roberta_standard
                             '''),
            
                dcc.Graph(
                figure={
                    'data': [
                        {'x': ["Accuracy", "Precision", "Recall"], 'y': [0.99, 0.95, .88],
                            'type': 'bar', 'name': 'Roberta_most_accurate'},
                        {'x': ["Accuracy", "Precision", "Recall"], 'y': [0.98,0.9, 0.84],
                         'type': 'bar', 'name': 'Roberta_standard'},
                    ]
                }
            ),
                dcc.Markdown('''
                             Confusion Matrix for Roberta_standard
                             '''),
            
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                    )


            ])
    ])
])

@app.callback(
    Output('textarea-output', 'children'),
    [Input('textarea1', 'value')]
)
def update_output(value):
    return("input text \n",value, "\n result processing..will be available shortly \n", "Result:",evaluate_model([value]))



if __name__ == '__main__':
    app.run_server(debug=True)