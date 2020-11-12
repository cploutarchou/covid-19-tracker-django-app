import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from django import template
from covid_stats.data import get_daily_data
from django_plotly_dash import DjangoDash

df = get_daily_data()
df['id'] = df.index
df.index.name = "id"
colors = px.colors.qualitative.Plotly

fig = go.Figure()
app = DjangoDash('DailyGrowth')
register = template.Library()
trace1 = go.Bar(x=df["id"], y=df['daily deaths'], name='Declined')
trace2 = go.Bar(x=df["id"], y=df['daily tests performed'], name='Pending')
trace3 = go.Bar(x=df["id"], y=df['daily deaths'], name='Presented')

app.layout = html.Div(children=[
    html.H1(children='Sales Funnel Report'),
    html.Div(children='''National Sales Funnel Report.'''),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2, trace3],
            'layout':
                go.Layout(title='Order Status by Customer', barmode='stack')
        }, className='six columns')
])


@app.callback(
    dash.dependencies.Output("output-color", "children"),
    [dash.dependencies.Input("dropdown-color", "value")],
)
def callback_color(dropdown_value):
    return "The selected color is %s." % dropdown_value


@app.callback(
    dash.dependencies.Output("output-size", "children"),
    [
        dash.dependencies.Input("dropdown-color", "value"),
        dash.dependencies.Input("dropdown-size", "value"),
    ],
)
def callback_size(dropdown_color, dropdown_size):
    return "The chosen T-shirt is a %s %s one." % (dropdown_size, dropdown_color)
