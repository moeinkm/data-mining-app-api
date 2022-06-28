import logging

import pandas as pd
from jdatetime import datetime


def to_df(serializer_data):
    data = pd.DataFrame.from_dict(serializer_data.get('data').get('data'))
    config = serializer_data.get('data').get('config')

    return data, config


def to_gregorian(df_data):
    for index, time in df_data['time'].items():
        df_data['time'][index] = datetime.strptime(
            time,
            '%Y-%m-%d'
        ).togregorian()


def to_jalali(df_data):
    for index, time in df_data['time'].items():
        df_data['time'][index] = str(datetime.fromgregorian(datetime=time))


def to_dictionary(df_data, config, service_name):
    """Convert DataFrame to python dict"""
    df_data['index'] = range(len(df_data))
    df_data['time'] = df_data.index
    df_data.index = df_data['index']
    del df_data['index']

    if config.get('type') == 'shamsi' or service_name == 'service2':
        to_jalali(df_data)

    return df_data.to_dict()


def prepare_data(serializer_data):
    """Convert serializer data to pandas DataFrame, separate config
    and convert time string to pandas datetime type"""
    df_data, config = to_df(serializer_data)

    if config.get('type') == 'shamsi':
        to_gregorian(df_data)

    df_data['time'] = pd.to_datetime(df_data['time'], utc=True)

    df_data.index = df_data['time']
    return df_data, config
