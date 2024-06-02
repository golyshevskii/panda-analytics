from typing import Tuple

from scripts.wb.client import WBClient

STATISTICS_TABLES = {
    "incomes": "wb_statistics_incomes",
    "stocks": "wb_statistics_stocks",
    "orders": "wb_statistics_orders",
    "sales": "wb_statistics_sales",
}


class Statistics:
    """Class for working with WB API statistics"""

    API_V1 = "https://statistics-api.wildberries.ru/api/v1/supplier/"
    API_V5 = "https://statistics-api.wildberries.ru/api/v5/supplier/"

    def __init__(self, client: WBClient):
        self.client = client

    def get_incomes(self, date_from: str, **kwargs) -> Tuple[int, dict]:
        """
        Gets statistics about incomes

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
        """
        return self.client.make_request(
            method="get", url=f"{self.API_V1}incomes", params={"dateFrom": date_from}
        )

    def get_stocks(self, date_from: str, **kwargs) -> Tuple[int, dict]:
        """
        Gets statistics about stocks

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
        """
        return self.client.make_request(
            method="get", url=f"{self.API_V1}stocks", params={"dateFrom": date_from}
        )

    def get_orders(self, date_from: str, flag: int = 0) -> Tuple[int, dict]:
        """
        Gets statistics about orders

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
            flag: 0 - all orders from date_from, 1 - only orders = date_from
        """
        return self.client.make_request(
            method="get",
            url=f"{self.API_V1}orders",
            params={"dateFrom": date_from, "flag": flag},
        )

    def get_sales(self, date_from: str, flag: int = 0) -> Tuple[int, dict]:
        """
        Gets statistics about sales

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
            flag: 0 - all orders from date_from, 1 - only orders = date_from
        """
        return self.client.make_request(
            method="get",
            url=f"{self.API_V1}sales",
            params={"dateFrom": date_from, "flag": flag},
        )
