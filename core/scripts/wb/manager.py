from config import PADWH_CONN, WB_API_TOKENS
from scripts.objects.logger import logger
from scripts.tools.psql.client import PSQLClient
from scripts.wb.api import get_statistics_incomes
from scripts.wb.client import WBClient
from scripts.wb.utils import SCHEMA, STATISTICS_INCOMES_TABLE


def import_incomes_statistics(customer_id: str, date_from: str):
    """
    Imports incomes statistics of a customer to the database

    Params:
        customer_id: ID of the customer
        date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
    """
    logger.info(
        f"Importing incomes statistics for customer {customer_id} " f"from {date_from}"
    )

    client = WBClient(api_token=WB_API_TOKENS[customer_id])
    _, incomes = get_statistics_incomes(date_from=date_from, client=client)

    psql_client = PSQLClient(conn_str=PADWH_CONN)
    psql_client.insert(schema=SCHEMA, table=STATISTICS_INCOMES_TABLE, data=incomes)

    logger.info("Incomes statistics have been imported")
