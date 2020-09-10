import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from django_plotly_dash import DjangoDash
from app.manage_sources import get_files
from datetime import datetime as d
import plotly.graph_objs as go
from .common import CurrentMonth
from coronavirus.models import DailyStats

files = get_files()
current_month = CurrentMonth()



def date_parse(x):
    return d.strptime(x, '%d/%m/%Y')


csv_file = None
for file in files:
    if "cy_covid_19_daily_stats" in file:
        csv_file = file

df = pd.read_csv(
    csv_file,
    parse_dates=['date'],
    date_parser=date_parse,
    infer_datetime_format=True
)

df['date'] = df['date'].astype('datetime64[ns]')
df['day'] = pd.DatetimeIndex(df['date']).day

df['month'] = pd.DatetimeIndex(df['date']).month
df['year'] = pd.DatetimeIndex(df['date']).year
df['total tests'] = pd.to_numeric(df['total tests'], errors='coerce')
df['total tests'] = df['total tests'].fillna(0)
df['total tests'] = df['total tests'].astype('int64')
df['daily tests performed'] = pd.to_numeric(df['daily tests performed'], errors='coerce')

df = df.fillna(0)
df['daily tests performed'] = df['daily tests performed'].astype('int64')
df['daily deaths'] = pd.to_numeric(df['daily deaths'], errors='coerce')

df['daily deaths'] = df['daily deaths'].astype('int64')
daily_cases_df = df[[
    'daily new cases',
    'daily deaths',
    'daily tests performed',
    'month',
    'day',
    'year'
]]

for index, row in df.iterrows():
    res = DailyStats(
        date=f"{row['year']}-{row['month']}-{row['day']}",

    )
    if res:
        continue

today = d.today()
current_date = d(today.year, today.month, 1)
month = current_date.month
year = current_date.year
filtered_df = daily_cases_df[daily_cases_df['month'] == current_month.get_current_month_int()]
app = DjangoDash('dash_daily_statistics')
fig = go.Figure(
    data=[
        go.Scatter(x=filtered_df['day'], y=filtered_df['daily new cases'], name="Positive", ),
        go.Scatter(x=filtered_df['day'], y=filtered_df['daily deaths'], name="Deaths", mode='markers',
                   marker={'size': 10}),
    ])
fig.update_layout(
    title={
        'text': "COVID-19 Cyprus Daily Statistics",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis={
        'title': 'Dates'
    },
    yaxis={
        'title': 'New Cases'
    },
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )

)

app.layout = html.Div([

    dcc.Graph(
        id='bar-chart',
        figure=fig

    )])
