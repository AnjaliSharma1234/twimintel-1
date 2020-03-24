import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import dash_table





external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__ , external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1(children="Twimbit NLP Preprocessor"),
    html.H1(children="Dashboard"),
    html.Label('Question' ),
    dcc.Input(id='q',value=' ',type='text'),
    
    html.Div(id='my-q'),


    html.Label('Answer' ),
    dcc.Input(id='a',value=' ',type='text'),
    
    html.Div(id='my-a'),

    html.Label('Content' ),
    dcc.Input(id='c',value=' ',type='text'),
    
    html.Div(id='my-c'),
    
    html.Div([
    	html.Button('Prepare Book', id="prepare")]),
                    
    dash_table.DataTable(
    	id="data",
    	columns=[{
    	"id":"q",
    	"name":"Questions",
    	"type":"text"
    	},{
    	"id":"a",
    	"name":"Answers",
    	"type":"text"
    	},{
    	"id":"c",
    	"name":"Contents",
    	"type":"text"
    	}],
    	editable=True)
    			
    

    
])

@app.callback(
    Output(component_id='my-q', component_property='children'),
    
    [Input(component_id='q', component_property='value')],
    
)

@app.callback(
    Output(component_id='my-a', component_property='children'),
    
    [Input(component_id='a', component_property='value')],
    
)

@app.callback(
    Output(component_id='my-c', component_property='children'),
    
    [Input(component_id='c', component_property='value')],
    
)



def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
    