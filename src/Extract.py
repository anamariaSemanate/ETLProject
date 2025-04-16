import pandas as pd
import yfinance as yf
from typing import List

def Extract_Data(list_tickers:List[str], start_date: str, end_date: str) -> pd.DataFrame:
    """extract historical data of stocks
    list_stocks: this are the list that contain the symbols to refer the actions
    time _star: time initial of the period of time ('YYYY-MM-DD')
    time_end: time end of the period of time ('YYYY-MM-DD')
    all_HistoricalData: Initialize a list to hold individual DataFrames
    """

    all_HistoricalData = []

    for ticker in list_tickers:
        print(f"descargando los datos de {list_tickers}...")

        try:
            historical_Data = yf.download(list_tickers,start=start_date,end=end_date) # Dowload data
            historical_Data.reset_index(inplace=True)                           # Convert the date column to a regular column
            historical_Data["Ticker"] = list_tickers                            # Add a column with the ticker name
            all_HistoricalData.append(historical_Data)
        except Exception as e:
            print(f"error al extraer los datos de  {list_tickers}: {e}")
        
        # concat all dataframes
        if all_HistoricalData:
            HistoricalData_Combine = pd.concat(all_HistoricalData, ignore_index=True)
            return HistoricalData_Combine
        else:
            print("No se extrajeron datos.")
            return pd.DataFrame()

