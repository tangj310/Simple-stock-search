from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date, timedelta
from stock_report import __get_stock_data, __period_metric_perc

app = FastAPI()

@app.get('/')
def index():
    return {
        'data': 'stock_list'
    }


@app.get('/stock/{ticker}')
def show(ticker: str):
    return {'data': ticker}