import numpy as np
import pandas as pd

from core.functions import GeneralFunctions as general, Dates

data_sources = dict(
    daily_report_url="https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/"
                     "data-sources/daily_report_data.csv"
)


def get_daily_data():
    url = data_sources['daily_report_url']
    df = pd.read_csv(filepath_or_buffer=url, header='infer', delimiter=";")
    return df


def daily_new_cases():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily new cases']
    if len(df.values) is not 0:
        return df.values[0]
    else:
        return "Unable to load data"


def daily_tests_performed():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily tests performed']
    if len(df.values) is not 0:
        return df.values[0]
    else:
        return "Unable to load data"


def daily_deaths():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily deaths'].astype(np.int64)
    if len(df.values) is not 0:
        return df.values[0]
    else:
        return "Unable to load data"


def new_cases_rate_compared_yesterday_date():
    yesterday = Dates.get_yesterday_date()
    two_dates_before = Dates.get_two_dates_before()
    df = get_daily_data()
    df = df.fillna(0)
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')

    yesterday_res = (df['day'] == yesterday)
    yesterday_df = df.loc[yesterday_res]['daily new cases'].astype(np.int64)

    yesterday_value = None

    if len(yesterday_df.values) is not 0:
        yesterday_value = yesterday_df.values[0]

    two_dates_before_df_res = (df['day'] == two_dates_before)
    two_dates_before_df = df.loc[two_dates_before_df_res]['daily new cases'].astype(np.int64)

    two_dates_before_value = None

    if len(yesterday_df.values) is not 0:
        two_dates_before_value = two_dates_before_df.values[0]

    res = general.percentage_difference_calculator(old_value=yesterday_value, new_value=two_dates_before_value)
    if res:
        return res
    else:
        return False


def get_current_month_data():
    pass
