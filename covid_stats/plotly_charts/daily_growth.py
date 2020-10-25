import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

from covid_stats.data import get_daily_data

app = dash.Dash(__name__)

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

app.layout = html.Div([
    html.H1('Square Root Slider Graph'),
    dcc.Graph(id='slider-graph', figure={'data': [fig]}, animate=True,
              style={"backgroundColor": "#1a2d46", 'color': '#ffffff'},
              ),
    dcc.Dropdown(id='demo-dropdown',
                 options=[
                     {'label': 'Daily', 'value': 'daily'},
                     {'label': 'Weekly', 'value': 'weekly'},
                     {'label': 'Monthly', 'value': 'monthly'}
                 ],
                 value='weekly'),
    html.Div(id='display-value')
])
