import numpy as np
import pandas as pd
import os

from app.redis.redis_client import RedisClient

from app.functions import GeneralFunctions as General, Dates

redis = RedisClient(1)
client = redis.client
data_sources = dict(
    daily_report_url="https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/data-sources" +
                     "/daily_report_data.csv",
)


def save_daily_data_to_redis():
    key = "daily_stats"
    url = data_sources['daily_report_url']
    df = pd.read_csv(filepath_or_buffer=url, header='infer')
    df.index = [x for x in range(1, len(df.values) + 1)]
    df.index.name = 'id'
    df.fillna(0)
    data = df.to_json()
    res = redis.set_key(key=key, data=data, ttl=86400)
    return res


def get_daily_data():
    res = client.get("daily_stats")
    df = pd.read_json(res)
    df = df.fillna(0)
    return df


def convert_to_date(df) -> pd.DataFrame:
    df['day'] = pd.to_datetime(df['date'], errors='coerce')
    return df


def daily_new_cases():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = convert_to_date(df)
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily new cases']
    if len(df.values) != 0:
        return df.values[0]
    else:
        return "Unable to load data"


def daily_tests_performed():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = df.fillna(0)
    df = convert_to_date(df)
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily tests performed']
    if len(df.values) != 0:
        return df.values[0]
    else:
        return "Unable to load data"


def daily_deaths():
    yesterday = Dates.get_yesterday_date()
    df = get_daily_data()
    df = df.fillna(0)
    df = convert_to_date(df)
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily deaths'].astype(np.int64)
    if len(df.values) != 0:
        return df.values[0]
    else:
        return "Unable to load data"


def new_cases_rate_compared_yesterday_date():
    yesterday = Dates.get_yesterday_date()
    two_dates_before = Dates.get_two_dates_before()
    df = get_daily_data()
    df = df.fillna(0)
    df = convert_to_date(df)

    yesterday_res = (df['day'] == yesterday)
    yesterday_df = df.loc[yesterday_res]['daily new cases'].astype(np.int64)

    yesterday_value = None

    if len(yesterday_df.values) != 0:
        yesterday_value = yesterday_df.values[0]

    two_dates_before_df_res = (df['day'] == two_dates_before)
    two_dates_before_df = df.loc[two_dates_before_df_res]['daily new cases'].astype(np.int64)

    two_dates_before_value = None

    if len(yesterday_df.values) != 0:
        two_dates_before_value = two_dates_before_df.values[0]

    if yesterday_value and two_dates_before is not None:
        res = General.percentage_difference_calculator(old_value=yesterday_value, new_value=two_dates_before_value)
        if res:
            return res
        else:
            return False


def get_current_month_data():
    pass


save_daily_data_to_redis()
