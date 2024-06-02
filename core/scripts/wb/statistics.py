from time import sleep
from typing import List, Tuple

from scripts.objects.logger import logger
from scripts.wb.client import WBClient

STATISTICS_TABLES = {
    "incomes": "wb_statistics_incomes",
    "stocks": "wb_statistics_stocks",
    "orders": "wb_statistics_orders",
    "sales": "wb_statistics_sales",
    "sales_report": "wb_statistics_sales_report",
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

    def get_sales_report(self, date_from: str, date_to: str) -> List[dict]:
        """
        Gets sales report

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
            date_to: Date to which to get data. Format: YYYY-MM-DDTHH:MM:SS
        """
        logger.info(f"Getting sales report from {date_from} to {date_to}")

        data = []
        rrdid = 0

        while True:
            _, report_part = self.get_sales_report_part(
                date_from=date_from, date_to=date_to, rrdid=rrdid
            )
            if len(report_part) == 0:
                break

            data.extend(report_part)
            rrdid = report_part[-1]["rrd_id"]
            sleep(61)

        logger.info("Sales report has been received")
        return data

    def get_sales_report_part(
        self, date_from: str, date_to: str, limit: int = 100000, rrdid: int = 0
    ) -> Tuple[int, List[dict]]:
        """
        Gets part of sales report that defined by limit

        Params:
            date_from: Date from which to get data. Format: YYYY-MM-DDTHH:MM:SS
            date_to: Date to which to get data. Format: YYYY-MM-DDTHH:MM:SS
            limit: Number of rows to get
            rrdid: Unique identifier for the report line. Required to receive the report in parts
        """
        return self.client.make_request(
            method="get",
            url=f"{self.API_V5}reportDetailByPeriod",
            params={
                "dateFrom": date_from,
                "dateTo": date_to,
                "limit": limit,
                "rrdid": rrdid,
            },
        )
