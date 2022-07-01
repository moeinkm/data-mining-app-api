import numpy as np
from scipy.stats import zscore

from common import prepare_data


def outlier_detection(serializer_data):
    """Call outlier detection methods in order to add method columns"""
    df_data, config = prepare_data(serializer_data)
    zscore_outlier_detection(df_data)
    iqr_outlier_detection(df_data)
    return df_data.to_dict()


def zscore_outlier_detection(df_data):
    """Outlier detection using z-score"""
    THRESHOLD = 3
    df_data['zscore'] = zscore(df_data['feature'])
    df_data['method1'] = np.where(abs(df_data['zscore']) > THRESHOLD, True, False)
    del df_data['zscore']


def iqr_outlier_detection(df_data):
    """Outlier detection using IQR distance from median"""
    q1 = df_data['feature'].quantile(0.25)
    q3 = df_data['feature'].quantile(0.75)
    iqr = q3 - q1
    df_data['method2'] = np.where(
        (df_data['feature'] < (q1 - (1.5 * iqr))) | (df_data['feature'] > (q3 + (1.5 * iqr))),
        True,
        False
    )
