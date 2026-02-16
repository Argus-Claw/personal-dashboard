"""Database connection utilities"""
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import pandas as pd

# Configure logging to redact credentials
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_engine():
    """Get SQLAlchemy engine with connection pooling"""
    db_url = os.getenv('DATABASE_URL', 'sqlite:///data/app.db')
    
    # Validate URL format
    if not db_url.startswith(('sqlite:///', 'postgresql://', 'mysql://')):
        raise ValueError("Invalid DATABASE_URL format")
    
    # Redact credentials from logs
    safe_url = db_url.split('@')[-1] if '@' in db_url else db_url
    logger.info(f"Connecting to database: {safe_url}")
    
    try:
        # Connection pooling for performance
        engine = create_engine(
            db_url,
            poolclass=QueuePool,
            pool_size=5,
            max_overflow=10,
            pool_pre_ping=True,
            echo=False
        )
        # Test connection
        with engine.connect() as conn:
            pass
        return engine
    except Exception as e:
        logger.error(f"Database connection failed: {safe_url}")
        raise

def query_to_df(query):
    """Execute query and return DataFrame"""
    try:
        engine = get_engine()
        return pd.read_sql(query, engine)
    except Exception as e:
        logger.error(f"Query failed: {str(e)[:100]}")
        raise

def df_to_db(df, table_name, if_exists='replace'):
    """Write DataFrame to database"""
    # Validate table name to prevent SQL injection
    if not table_name.replace('_', '').isalnum():
        raise ValueError("Invalid table name")
    
    try:
        engine = get_engine()
        df.to_sql(table_name, engine, if_exists=if_exists, index=False)
    except Exception as e:
        logger.error(f"Write to {table_name} failed: {str(e)[:100]}")
        raise
