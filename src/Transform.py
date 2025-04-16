def Transform_Data(historical_data):
    #delete duplicated data
    historical_data = historical_data.loc[:, ~historical_data.columns.duplicated()]

    #delete rows with null values
    historical_data = historical_data.dropna()

    #correct format
    #historical_data['Date'] = historical_data.to_datetime(historical_data['Date'])
    #historical_data['Close'] = historical_data.to_numeric(historical_data['Close'], errors='coerce')

    #calculation of daily return 
    historical_data['Daily Return'] = historical_data['Close'].pct_change()

    #standard deviation
    historical_data['Volatility_7'] = historical_data['Close'].rolling(window=7).std()

    #Cumulative performance
    historical_data['Cumulative Return'] = (1 + historical_data['Daily Return']).cumprod()

    #maximum and minimum price in the period
    historical_data['Max_30'] = historical_data['High'].rolling(window=30).max()
    historical_data['Min_30'] = historical_data['Low'].rolling(window=30).min()

    return historical_data