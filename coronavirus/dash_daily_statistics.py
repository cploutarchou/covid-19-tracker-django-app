import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from django_plotly_dash import DjangoDash
from app.config import daily_stats


def date_parse(x):
    return pd.datetime.strptime(x, '%d/%m/%y')


idx = pd.date_range('2020-08-1', periods=30, freq='D')
df = pd.read_csv(daily_stats, encoding="UTF-8", parse_dates=['date'], date_parser=date_parse, infer_datetime_format=True
                 , error_bad_lines=False)
df = df.loc[df['date'] >= '2020-07-25']

# Important: Define Id for Plotly Dash integration in Django
app = DjangoDash('dash_daily_statistics')

app.layout = html.Div([
    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                {'x': df['date'], 'y': df['daily new cases'], 'type': 'char', 'name': 'SF'}
            ],
            'layout': {
                'title': 'Current month daily stats'
            }
        }
    )
], className='col')
