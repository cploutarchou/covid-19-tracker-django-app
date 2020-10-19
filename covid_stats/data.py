import datetime
import platform

import pandas as pd

if platform.system() == 'Linux':
    DATE_DATA_FRAME_FORMAT: str = '%-m/%-d/%y'
elif platform.system() == 'Windows':
    DATE_DATA_FRAME_FORMAT: str = '%#m/%#d/%y'
else:
    DATE_DATA_FRAME_FORMAT: str = '%-m/%-d/%y'


def daily_new_cases():
    url = "https://raw.githubusercontent.com/cploutarchou/covid-19-tracker-django-app/master/data-sources" \
          "/daily_report_data.csv "
    yesterday = datetime.date.today() - datetime.timedelta(days=2)
    yesterday = yesterday.strftime('%Y-%m-%d')
    df = pd.read_csv(filepath_or_buffer=url, header='infer')
    df['day'] = pd.to_datetime(df['date'].str.strip(), format='%d/%m/%Y')
    result = (df['day'] == yesterday)
    df = df.loc[result]['daily new cases']
    return df


res = daily_new_cases()
