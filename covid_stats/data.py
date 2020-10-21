import datetime

import pandas as pd


def daily_new_cases():
    url = "https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/data-sources" \
          "/daily_report_data.csv "
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    df = pd.read_csv(filepath_or_buffer=url, header='infer')
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily new cases']
    if df.values:
        return df.values[0]
    return "Updating Data...."
