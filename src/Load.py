import pandas as pd
from sqlalchemy import create_engine

def Load_Data(data_transform,table_name, db_user, db_password, db_name, db_host, db_port):
    
    """
    Upload a pandas DataFrame to a PostgreSQL table in Google Cloud SQL.
    Args:
    data_transform: The DataFrame to upload.
    table_name (str): Name of the destination table in the database.
    db_user (str): Database username.
    db_password (str): Database password.
    db_name (str): Database name.
    db_host (int): the public IP.
    db_port (int): 5432
    """
    try:
        engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        data_transform.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Tabla '{table_name}' subida correctamente.")
    except Exception as e:
        print(f"Error al subir la tabla: {e}")

    return print("successful upload")



def Load_Local(Tickers,data_transform):
    processed_files = []
    
    # Iterate over the Tickers and save the file
    for T in Tickers:
        file_name = f'data/processed_{T}.csv'
        data_transform.to_csv(file_name, index=False)
        processed_files.append(file_name)  # Save the name of the processed file
    
    return processed_files