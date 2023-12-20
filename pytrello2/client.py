import requests
from .exceptions import TrelloAPIException


class HttpClient:
    """
    Handles HTTP requests to the Trello API.
    """

    BASE_URL = "https://api.trello.com/1/"

    def __init__(self, token, api_key):
        """
        Initializes the HttpClient with Trello API credentials.
        """
        self.api_key = api_key
        self.token = token

    def _request(self, method, endpoint, data=None, params=None):
        """
        Sends an HTTP request to the Trello API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {"Content-Type": "application/json"}
        if params is None:
            params = {}
        params.update({"key": self.api_key, "token": self.token})

        try:
            response = requests.request(
                method, url, headers=headers, json=data, params=params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise TrelloAPIException(f"HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            raise TrelloAPIException(f"Error during request: {err}")

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the Trello API.
        """
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, data=None):
        """
        Sends a POST request to the Trello API.
        """
        return self._request("POST", endpoint, data=data)

    def put(self, endpoint, data=None):
        """
        Sends a PUT request to the Trello API.
        """
        return self._request("PUT", endpoint, data=data)

    def delete(self, endpoint, data=None):
        """
        Sends a DELETE request to the Trello API.
        """
        return self._request("DELETE", endpoint, data=data)
