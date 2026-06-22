import warnings
import pyodbc
import pandas as pd

warnings.filterwarnings(
    "ignore",
    message="pandas only supports SQLAlchemy"
)

from config import SERVER, DATABASE, TABLE_NAME


def get_connection():
    return pyodbc.connect(
        f"""
        DRIVER={{ODBC Driver 17 for SQL Server}};
        SERVER={SERVER};
        DATABASE={DATABASE};
        Trusted_Connection=yes;
        """
    )


def fetch_data():
    conn = get_connection()

    query = f"""
    SELECT *
    FROM {TABLE_NAME}
    ORDER BY Id
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df