import pandas as pd
from config import PATH
from scripts.objects.logger import logger
from sqlalchemy import create_engine


class PSQLClient:
    """
    Class for working with PostgreSQL database

    Attributes:
        engine: SQLAlchemy engine
    """

    def __init__(self, conn_str: str):
        self.engine = create_engine(conn_str)

    def _is_sql_file(self, sql: str) -> str:
        """
        Checks if query is a SQL file

        Params:
            sql: Path to the SQL file
        """
        if sql.endswith(".sql"):
            with open(f"{PATH}{sql}", "r", encoding="utf-8") as file:
                return file.read()
        return sql

    def select(self, sql: str) -> pd.DataFrame:
        """
        Selects data from database

        Params:
            query: SQL SELECT query
        """
        logger.info("Selecting data from database...")
        data = pd.read_sql(sql=self._is_sql_file(sql), con=self.engine)

        logger.info(f"Data has been extracted successfully. Shape: {data.shape}")
        return data
