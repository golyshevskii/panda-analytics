from typing import Tuple

from scripts.wb.client import WBClient

STATISTICS_API_URL = "https://statistics-api.wildberries.ru/api/v1/supplier/"


def get_statistics_incomes(date_from: str, client: WBClient) -> Tuple[int, dict]:
    """
    Gets statistics about income

    Params:
        date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
    """
    return client.make_request(
        method="get", url=f"{STATISTICS_API_URL}incomes", params={"dateFrom": date_from}
    )
