from Extract import Extract_Data
from Transform import Transform_Data
from Load import Load_Data

if __name__ == "__main__":
    Tickers = ['AAPL', 'MSFT','NVDA','AMZN']
    Start_date = "2023-01-01"
    End_date = "2025-03-31"

    for ticker in Tickers:
        #Extract data
        print(f"Extracting {ticker}...")
        Raw_HistoricalData = Extract_Data(ticker, Start_date, End_date)

        #Transform data
        print(f"Transforming {ticker}...")
        Transform_HistoricalData = Transform_Data(Raw_HistoricalData)
        
        #load_to_csv(transformed_df, ticker)
        print(f"Load data ...")
        data_transform = Transform_HistoricalData
        table_name = "Data_{}".format(ticker)
        db_user = "user"
        db_password = ""
        db_name = "DB"
        db_host = "x.x.x.x"
        Load_HistoricalData = Load_Data(data_transform,table_name, db_user, db_password, db_name, db_host, db_port=5432)
