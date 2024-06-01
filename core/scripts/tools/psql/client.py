import os
from typing import List, Union

import pandas as pd
from config import PATH
from psycopg2 import connect
from psycopg2.extras import execute_batch
from scripts.objects.logger import logger
from sqlalchemy import create_engine


class PSQLClient:
    """
    Class for working with PostgreSQL database

    Attributes:
        conn_str: Connection string.
            Format: 'postgresql://<user>:<password>@<host>:<port>/<database>'
        engine: SQLAlchemy engine
    """

    def __init__(self, conn_str: str):
        self.conn_str = conn_str
        self.engine = create_engine(conn_str)

    def select(self, sql: str) -> pd.DataFrame:
        """
        Selects data from database

        Params:
            sql: SQL SELECT query
        """
        logger.info("Selecting data from database...")
        data = pd.read_sql(sql=self._is_file(sql), con=self.engine)

        logger.info(f"Data has been extracted successfully. Shape: {data.shape}")
        return data

    def insert(
        self, schema: str, table: str, data: Union[List[dict], pd.DataFrame], **kwargs
    ) -> None:
        """
        Inserts data into database

        Params:
            schema: Schema name
            table: Table name
            data: Data to insert

            **kwargs
                for DataFrames:
                    if_exists → {'fail', 'replace', 'append'}, default 'append'
                        index → Write row labels (index) of DataFrames, default False
                for List[dict]:
                    on_conflict → ON CONFLICT clause {'update', 'nothing'}
                    constraint → Constraint name for the ON CONFLICT clause, default None
                    pkeys → List of primary keys for the ON CONFLICT clause, default None
        """
        logger.info(f"Inserting data into {schema}.{table}...")

        if isinstance(data, pd.DataFrame):
            data.to_sql(
                schema=schema,
                name=table,
                con=self.engine,
                if_exists=kwargs.get("if_exists", "append"),
                index=kwargs.get("index", False),
            )

            logger.info("Data has been inserted successfully")
            return

        with connect(self.conn_str) as conn:
            with conn.cursor() as cur:
                SQL = self._iquery(schema=schema, table=table, data=data, **kwargs)
                execute_batch(cur=cur, sql=SQL, argslist=data, page_size=1000)
                conn.commit()

        logger.info("Data has been inserted successfully")

    def _is_file(self, sql: str) -> str:
        """
        Checks if query is a SQL file

        Params:
            sql: Path to the SQL file
        """
        if sql.endswith(".sql"):
            with open(os.path.join(PATH, sql), "r", encoding="utf-8") as file:
                return file.read()

        return sql

    def _iquery(self, schema: str, table: str, data: List[dict], **kwargs) -> str:
        """
        Returns insert query

        Params:
            schema: Schema name
            table: Table name
            data: Data to insert
        """
        columns = list(data[0].keys())
        attributes = ",".join(columns)

        values = ["%({0})s".format(column) for column in columns]
        values = ",".join(values)

        if kwargs.get("on_conflict") is None:
            return f"INSERT INTO {schema}.{table} ({attributes}) VALUES ({values})"
        elif kwargs.get("on_conflict") == "nothing":
            pkeys = kwargs.get("pkeys")
            constraint = kwargs.get("constraint")

            on_conflict_clause = (
                f"({','.join(pkeys)})" if pkeys else f"ON CONSTRAINT {constraint}"
            )
            return f"""
                INSERT INTO {schema}.{table} ({attributes})
                VALUES ({values})
                ON CONFLICT {on_conflict_clause} DO NOTHING;
                """
        elif kwargs.get("on_conflict") == "update":
            pkeys = kwargs.get("pkeys")
            constraint = kwargs.get("constraint")

            updates = ["{0}=%({0})s".format(column) for column in columns]
            updates = ", ".join(updates)

            on_conflict_clause = (
                f"({','.join(pkeys)})" if pkeys else f"ON CONSTRAINT {constraint}"
            )

            return f"""
                INSERT INTO {schema}.{table} ({attributes})
                VALUES ({values})
                ON CONFLICT {on_conflict_clause} DO UPDATE SET {updates};
                """
