"""Database connection utilities"""
import os
from sqlalchemy import create_engine
import pandas as pd

def get_engine():
    """Get SQLAlchemy engine from environment"""
    db_url = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    return create_engine(db_url)

def query_to_df(query):
    """Execute query and return DataFrame"""
    engine = get_engine()
    return pd.read_sql(query, engine)

def df_to_db(df, table_name, if_exists='replace'):
    """Write DataFrame to database"""
    engine = get_engine()
    df.to_sql(table_name, engine, if_exists=if_exists, index=False)
