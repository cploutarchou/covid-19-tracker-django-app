import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from django_plotly_dash import DjangoDash
import dash_bootstrap_components as abc
from datetime import datetime, timedelta
from calendar import monthrange
from app.config import daily_stats
pandas_schemapandas_schema

def format_date():
    today = datetime.today()
    _date = datetime(today.year, today.month, 1).isoformat().split('T')[0]
    _date = _date.split("-")
    _date = f"{_date[2]}/{_date[1]}/{_date[0].replace('2020', '20')}"
    return _date


date = format_date()

schema = Schema([
    Column('date', [DateFormatValidation(), TrailingWhitespaceValidation()]),
    Column('daily new cases', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('daily deaths ', [InRangeValidation(0, 120)]),
    Column('daily recovered cases', [InListValidation(['Male', 'Female', 'Other'])]),
    Column('daily tests performed', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')])
])

df = pd.read_csv(daily_stats, encoding="UTF-8")
df = df.sort_values(by=['date'], ascending=False)
filtered_dates = df.loc('date' > date)

# Important: Define Id for Plotly Dash integration in Django
app = DjangoDash('dash_daily_statistics')

app.layout = html.Div([
    dcc.Graph(
        id='bar-chart',
        figure={
            'data': [
                {'x': filtered_dates['date'], 'y': filtered_dates['total tests'], 'type': 'bar', 'name': 'SF'}
            ],
            'layout': {
                'title': 'Current month daily stats'
            }
        }
    )

], className='col')
