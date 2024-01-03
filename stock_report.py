import pandas as pd
import numpy as np

from datetime import datetime, timedelta
import yfinance as yf
from pandas_datareader import data as pdr


def __get_stock_data(ticker_symbol, search_start_date, search_end_date):
    """
    This fucntion retreive the stock data using yfinance library and clean the dataframe with requested column
    """
    yf.pdr_override()

    # download dataframe
    df = pdr.get_data_yahoo(
        ticker_symbol.upper(), start=search_start_date, end=search_end_date
    )

    # create calculation
    df["Volume % Change"] = df["Volume"].pct_change() * 100
    df["Close % Change"] = df["Close"].pct_change() * 100

    # clean dataframe with requested column
    df = df[["Close", "Volume", "Volume % Change", "Close % Change"]]

    # fill the NA with 0
    df = df.fillna(0)

    return df


def __period_metric_perc(df, metric_name_list):
    """
    This function calculate period percentage change through all requested metrics
    """

    metric_value_list = []

    for metric in metric_name_list:
        period_metric_perc_delta = round(
            ((df[metric].iloc[-1] - df[metric].iloc[0]) / df[metric].iloc[0]) * 100, 4
        )
        metric_value_list.append(period_metric_perc_delta)

    metric_dict = dict(zip(metric_name_list, metric_value_list))

    return metric_dict