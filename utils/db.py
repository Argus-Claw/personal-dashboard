"""Database connection utilities - simplified version"""
import os
import pandas as pd

def query_to_df(query):
    """Placeholder for database queries"""
    # Currently using CSV/data files instead of database
    pass

def save_to_csv(df, filename):
    """Save DataFrame to CSV in data folder"""
    filepath = f"data/{filename}.csv"
    df.to_csv(filepath, index=False)
    return filepath

def load_from_csv(filename):
    """Load DataFrame from CSV"""
    filepath = f"data/{filename}.csv"
    if os.path.exists(filepath):
        return pd.read_csv(filepath)
    return None
