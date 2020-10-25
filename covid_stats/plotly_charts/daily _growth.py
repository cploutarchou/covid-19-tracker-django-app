import plotly.express as px
import plotly.graph_objects as go

from covid_stats.data import get_daily_data

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
fig.show()
