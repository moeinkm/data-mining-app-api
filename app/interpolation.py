import pandas as pd

from common import to_gregorian

TIMEFRAME_TRANSLATION = {
    'daily': 'D',
    'monthly': 'M',
    'hourly': 'H',
    'minutes': 'T',
    '5 minutes': '5T',
    '5minutes': '5T',
    'five minutes': '5T',
}


def interpolation(df_data, config):
    if config['type'].lower() == 'shamsi':
        to_gregorian(df_data)

    df_data['time'] = pd.to_datetime(df_data['time'], utc=True)
    df_data.index = df_data['time']

    try:
        df_data = df_data.resample(
            TIMEFRAME_TRANSLATION.get(
                config.get('time').lower()
            )
        ).mean()
    except Exception:
        raise ValueError('config time value not recognized')

    if config.get('interpolation') == 'linear':
        df_data['vol'] = df_data['vol'].interpolate(method='linear')
    elif config.get('interpolation') == 'spline':
        df_data['vol'] = df_data['vol'].interpolate(method='polynomial', order=2)
    else:
        raise ValueError('method not supported')

    return to_dictionary(df_data)


def to_dictionary(df_data):
    df_data['index'] = range(len(df_data))
    df_data['time'] = df_data.index
    df_data.index = df_data['index']
    del df_data['index']

    return df_data.to_dict()
