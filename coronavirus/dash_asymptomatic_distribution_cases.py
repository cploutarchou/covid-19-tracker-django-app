import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table
from django_plotly_dash import DjangoDash
from app.manage_sources import get_files
from datetime import datetime as d
import plotly.graph_objs as go
from coronavirus.common import *
from coronavirus.models import DailyStats
import dash

files = get_files()
current_month = CurrentMonth()


def date_parse(x):
    return d.strptime(x, '%d/%m/%Y')


csv_file = None
for file in files:
    if "cases-by-province" in file:
        csv_file = file

df = pd.read_csv(
    csv_file,
    parse_dates=['Date'],
    date_parser=date_parse,
    infer_datetime_format=True
)

app = DjangoDash('dash_asymptomatic_distribution_cases')  # replaces dash.Dash

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    style_cell_conditional=[
        {
            'if': {'column_id': c},
            'textAlign': 'left'
        } for c in ['Date', 'Region']
    ],
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ],
    style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
    }
)
