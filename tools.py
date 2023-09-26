import pandas as pd
import numpy as np
from scipy import stats

def mean(df):
    return df.mean()

def std(df):
    return df.std()


def var(df):
    return df.var()

def mean_ad(df):
    mads = {}
    for col in df.columns:
        mads[col] = np.mean(np.absolute(df[col] - np.mean(df[col])))
    return pd.Series(mads)


def median_ad(df):
    mads = {}
    for col in df.columns:
        mads[col] = stats.median_abs_deviation(df[col])
    return pd.Series(mads)


def iqr(df):
    iqrs = {}
    for col in df.columns:
        iqrs[col] = stats.iqr(df[col], interpolation='midpoint')
    return pd.Series(iqrs)


def qd(df):
    qds = {}
    for col in df.columns:
        qds[col] = (np.percentile(df[col], 75) - np.percentile(df[col], 25))/2
    return pd.Series(qds)
