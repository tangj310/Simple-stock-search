from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import date, timedelta
from stock_report import __get_stock_data, __period_metric_perc

app = FastAPI()


class StockAnalysisRequest(BaseModel):
    ticker_symbol: str
    time_period: int

@app.get("/")
def stock_analysis(request: StockAnalysisRequest):

    today_date = date.today()
    search_start_date = today_date - timedelta(request.time_period)
    search_end_date = today_date


    df = __get_stock_data(

        request.ticker_symbol
        ,search_end_date - timedelta(1)
        ,search_end_date
    )

    metric_name_list = [
        'Volume'
        ,'Close'
    ]

    metric_dict = __period_metric_perc(df, metric_name_list)

    return {
        'start_date': str(search_start_date)
        ,'end_date': str(search_end_date)
        ,'stock_symbol': request.ticker_symbol.upper()
        ,'date': df.to_dict(orient='records')
        ,'metrics': metric_dict
    }

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app
        ,host="127.0.0.1"
        ,port=8000
        )
