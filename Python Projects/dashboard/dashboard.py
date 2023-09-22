import  dash
import dash_html_components as html
import dash_core_components as dcc

app  = dash.Dash()

app.layout = html.Div(children=[html.H1(children='Sample Dash Web App Dashboard'),
                      html.Div(children = '''Dash: a web based  app too show bar raph'''),
                      dcc.Graph(id='dash_graph',
                                figure= {'data':[{'x':[1,2,3,4,5], 'y':[4,6,3,8,1], 'type': 'bar','name':'Bread' },
                                                 {'x':[1,2,3,4,5], 'y':[1,2,9,8,6], 'type': 'bar','name':'Sugar' },
                                                 {'x':[1,2,3,4,5], 'y':[3,5,6,3,4], 'type': 'bar','name':'Bread' },],
                                                 'layout':{'title': 'Dash Example App'}})])

if __name__ == '__main__':
    app.runserver(debug = True)

