import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import dash_table
import sqlite3


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__ , external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H1(children="Twimbit NLP Preprocessor"),
    html.H1(children="Dashboard"),
    html.Label('Question' ),
    dcc.Input(id='q',value=' ',type='text'),


    html.Label('Answer' ),
    dcc.Input(id='a',value=' ',type='text'),
    html.Label('Content' ),

    dcc.Input(id='c',value=' ',type='text'),
    
   html.Button(id='submit-button', n_clicks=0, children='Submit'),
   html.Div(id='my-q'),
          
    

    
])

@app.callback(
    Output(component_id='my-q', component_property='children'),
    
    [Input('submit-button', 'n_clicks')],
    [State(component_id='q', component_property='value'),
    State(component_id='a', component_property='value'),
    State(component_id='c', component_property='value')])




def create_table():
  conn = sqlite3.connect('example.db')
  c=conn.cursor()
  c.execute('''CREATE TABLE  IF NOT EXISTS twimm( questions TEXT ,answers TEXT, content TEXT)''')

def update_output_div(n_click,q,a,c):
  print(q)
  
  c.execute("INSERT INTO twimm (questions,answers,content) VALUES (?,?,?)",(q,a,c))
  conn.commit()
  return '''
        The Button has been pressed {} times,
        Question is "{}",
        and Answer  is "{}"
        and Contents  is "{}"
    '''.format(q, a,c)
  
create_table()


if __name__ == '__main__':
  app.run_server(debug=True)
    
