from config import PADWH_CONN, WB_API_TOKENS
from scripts.objects.logger import logger
from scripts.tools.psql.client import PSQLClient
from scripts.wb.client import WBClient
from scripts.wb.statistics import STATISTICS_TABLES, Statistics
from scripts.wb.utils import SCHEMA


def import_statistics(seller_id: str, entity: str, **kwargs) -> None:
    """
    Imports statistics of a WB seller to the database

    Params:
        seller_id: ID of the customer
        entity: Statistics entity to import. Available: "incomes", "stocks", "orders", "sales"
        **kwargs: Additional parameters for the request
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
            flag (optional): 0 - all orders from date_from, 1 - only orders = date_from
    """
    logger.info(f"Importing {entity} statistics for customer {seller_id}")

    wb_client = WBClient(api_token=WB_API_TOKENS[seller_id])
    statistics = Statistics(client=wb_client)

    _, data = getattr(statistics, f"get_{entity}")(**kwargs)

    psql_client = PSQLClient(conn_str=PADWH_CONN)
    psql_client.insert(schema=SCHEMA, table=STATISTICS_TABLES[entity], data=data)

    logger.info("Statistics have been imported")


def import_sales_report(seller_id: str, date_from: str, date_to: str) -> None:
    """
    Imports sales report of a WB seller to the database

    Params:
        seller_id: ID of the customer
        date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
        date_to: Date to which to get data. Format: YYYY-MM-DDTHH:MM:SS
    """
    logger.info(f"Importing sales report for customer {seller_id}")

    wb_client = WBClient(api_token=WB_API_TOKENS[seller_id])
    statistics = Statistics(client=wb_client)

    _, data = statistics.get_sales_report(date_from=date_from, date_to=date_to)

    psql_client = PSQLClient(conn_str=PADWH_CONN)
    psql_client.insert(
        schema=SCHEMA, table=STATISTICS_TABLES["sales_report"], data=data
    )

    logger.info("Sales report has been imported")
