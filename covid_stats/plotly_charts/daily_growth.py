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
trace1 = go.Bar(x=df["id"], y=df['daily new cases'], name='New cases')
trace2 = go.Bar(x=df["id"], y=df['daily tests performed'], name='Test performed')
trace3 = go.Bar(x=df["id"], y=df['daily deaths'], name='Deaths')

app.layout = html.Div(children=[
    dcc.Graph(
        id='DailyGrowth_graph',
        figure={
            'data': [trace1, trace2, trace3],
            'layout':
                go.Layout(barmode='stack')
        },
    )
])
