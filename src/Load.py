import pandas as pd
from sqlalchemy import create_engine

def Load_Data(data_transform,table_name, db_user, db_password, db_name, db_host, db_port):
    
    """
    Upload a pandas DataFrame to a PostgreSQL table in Google Cloud SQL.
    Args:
    df (pd.DataFrame): The DataFrame to upload.
    table_name (str): Name of the destination table in the database.
    db_user (str): Database username.
    db_password (str): Database password.
    db_name (str): Database name.
    instance_connection_name (str): Instance connection name (project:region:instance).
    """
    try:
        engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        data_transform.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Tabla '{table_name}' subida correctamente.")
    except Exception as e:
        print(f"Error al subir la tabla: {e}")

    return data_transform.to_csv('data/processed.csv', index=False)
