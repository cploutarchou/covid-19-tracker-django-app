import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
from django import template
from covid_stats.data import get_daily_data
from django_plotly_dash import DjangoDash

register = template.Library()
app = DjangoDash('SimpleExample')

df = get_daily_data()
df['id'] = df.index
colors = px.colors.qualitative.Plotly

fig = go.Figure()
# noinspection PyTypeChecker
fig.add_traces(go.Bar(x=df["id"], y=df["daily new cases"], marker=dict(color=colors[0])))
# noinspection PyTypeChecker
fig.add_traces(go.Bar(x=df['id'], y=df['daily tests performed'], marker=dict(color=colors[1])))
# noinspection PyTypeChecker
fig.add_traces(go.Bar(x=df['id'], y=df['daily deaths'], marker=dict(color=colors[2])))

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph',
        figure=fig
    )

],

    style={
        'width': '100%',
        'height': '100%',
        'fontFamily': 'Sans-Serif',
        'margin-left': '1cm',
        'margin-right': 'auto'
    }
)