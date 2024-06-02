from typing import Dict, List, Tuple, Union

import requests
from scripts.objects.logger import logger


class WBClient:
    """Class for with Wildberries API"""

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers = self.set_auth_headers()

    def set_auth_headers(self) -> Dict[str, str]:
        return {
            "Authorization": self.api_token,
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
        }

    def make_request(
        self,
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        json: Union[dict, List] = None,
    ) -> Tuple[int, dict]:
        """
        Makes a request to WB API

        Params:
            method: Request method. Example: "get", "post", "put", "delete"
            url: Request url. Example: "supplier/incomes".
                WARNING: Without API base "https://api.wildberries.ru/api/v1"
            headers: Request headers.
                WARNING: Headers already contains authentication and content type
            params: Additional request parameters.
            json: Additional serialized data for request.

        Returns: (Response status code, Response data in JSON format)
        """
        kw_args = {
            "url": url,
            "headers": {**self.headers, **(headers or {})},
            "params": params,
            "json": json,
        }

        response: requests.Response = getattr(requests, method)(**kw_args)
        logger.info(
            f"{method.upper()} request to {url=}. "
            f"Status code: {response.status_code}. "
        )

        self._handle_error(response)
        return response.status_code, response.json()

    def _handle_error(self, response: requests.Response) -> None:
        """
        Handles error

        Params:
            response: Response data
        """
        response_status = response.status_code
        response_details = response.json()

        if response_status in (400, 401, 403, 429):
            raise Exception(
                f"Status Code: {response_status}. "
                f"Response details → {response_details}"
            )
