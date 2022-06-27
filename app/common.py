import pandas as pd
from jdatetime import datetime


def to_df(serializer_data):
    data = pd.DataFrame.from_dict(serializer_data.get('data').get('data'))
    config = serializer_data.get('data').get('config')

    return data, config


def to_gregorian(df_data):
    for index, time in df_data['time'].items():
        df_data['time'][index] = datetime.strptime(
            df_data['time'][index],
            '%Y-%m-%d'
        ).togregorian()
