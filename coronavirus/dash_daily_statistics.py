import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from django_plotly_dash import DjangoDash
from app.manage_sources import get_files
from datetime import datetime


files = get_files()


def date_parse(x):
    return datetime.strptime(x, '%d/%m/%y')


idx = pd.date_range('2020-08-1', periods=30, freq='D')

csv_file = None
for file in files:
    if "cy_covid_19_daily_stats" in file:
        print("file found")
        csv_file = file


df = pd.read_csv(csv_file,
                 encoding="UTF-8")

df['date'] = df['date'].astype('datetime64[ns]')
df['total tests'] = pd.to_numeric(df['total tests'], errors='coerce')
# df['total tests'] = df['total tests'].astype('int64')
# df.fillna(0)

app = DjangoDash('dash_daily_statistics')

app.layout = html.Div([
    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                {'x': df['date'], 'y': df['daily new cases'], 'type': 'bar', 'name': 'CY DAILY'}
            ],
            'layout': {
                'title': 'Current month daily stats'
            }
        }
    )
], className='col')
