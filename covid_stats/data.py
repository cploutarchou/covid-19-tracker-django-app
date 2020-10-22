import datetime

import numpy as np
import pandas as pd

data_sources = dict(
    daily_report_url="https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/"
                     "data-sources/daily_report_data.csv"
)


def daily_report_df():
    url = data_sources['daily_report_url']
    df = pd.read_csv(filepath_or_buffer=url, header='infer')
    return df


def daily_new_cases():
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    df = daily_report_df()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily new cases']
    return df.values[0]


def daily_tests_performed():
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    df = daily_report_df()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily tests performed']
    return df.values[0]


def daily_deaths():
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    df = daily_report_df()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily deaths'].astype(np.int64)
    return df.values[0]


def new_cases_rate_compared_yesterday_date(): pass
