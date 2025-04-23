This personal project implements an ETL (Extract, Transform, Load) pipeline that allows for the collection, transformation, and storage of historical financial data from Yahoo Finance. It is designed to facilitate exploratory analysis and financial visualizations.

The project performs the following tasks:
Extraction: Obtains historical data on stock prices or other financial assets from Yahoo Finance using its public API or libraries such as yfinance.

Transformation: Data cleansing, date standardization, data type conversion, and calculation of basic financial indicators (for example, moving averages, daily returns, etc.).

Load: Stores the transformed data in a CSV file, a local database, or a remote Google Cloud database, as required.

Technologies Used

    -pandas                    2.2.3
    
    -yfinance                  0.2.55
    
    -typing_extensions         4.13.2
    
    -SQLAlchemy                2.0.40

project execution

    1.  git clone https://github.com/anamariaSemanate/ETLProject.git
        cd ETLProject

    2.  pip install -r requirements.txt

    3.  python src/main.py


