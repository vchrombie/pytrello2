import pytest
import requests

from unittest.mock import patch, Mock
from pytrello2.client import HttpClient
from pytrello2.exceptions import TrelloAPIException


# Fixture for the mock HTTP client
@pytest.fixture
def http_client():
    return HttpClient(token="test_token", api_key="test_api_key")


# Test for get method
def test_get(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = http_client.get("some_endpoint")
        mock_request.assert_called_once_with(
            "GET",
            "https://api.trello.com/1/some_endpoint",
            headers={"Content-Type": "application/json"},
            json=None,
            params={"key": "test_api_key", "token": "test_token"},
        )
        assert response == {"success": True}


# Test for post method
def test_post(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = http_client.post("some_endpoint", data={"some": "data"})
        mock_request.assert_called_once_with(
            "POST",
            "https://api.trello.com/1/some_endpoint",
            headers={"Content-Type": "application/json"},
            json={"some": "data"},
            params={"key": "test_api_key", "token": "test_token"},
        )
        assert response == {"success": True}


# Test for put method
def test_put(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = http_client.put("some_endpoint", data={"some": "data"})
        mock_request.assert_called_once_with(
            "PUT",
            "https://api.trello.com/1/some_endpoint",
            headers={"Content-Type": "application/json"},
            json={"some": "data"},
            params={"key": "test_api_key", "token": "test_token"},
        )
        assert response == {"success": True}


# Test for delete method
def test_delete(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_response.raise_for_status = Mock()
        mock_request.return_value = mock_response

        response = http_client.delete("some_endpoint", data={"some": "data"})
        mock_request.assert_called_once_with(
            "DELETE",
            "https://api.trello.com/1/some_endpoint",
            headers={"Content-Type": "application/json"},
            json={"some": "data"},
            params={"key": "test_api_key", "token": "test_token"},
        )
        assert response == {"success": True}


# Test for http error
def test_http_error(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_request.side_effect = requests.exceptions.HTTPError("HTTP Error")

        with pytest.raises(TrelloAPIException) as excinfo:
            http_client.get("some_endpoint")
        assert "HTTP error occurred: HTTP Error" in str(excinfo.value)


# Test for request exception
def test_request_error(http_client):
    with patch("pytrello2.client.requests.request") as mock_request:
        mock_request.side_effect = requests.exceptions.RequestException("Request Error")

        with pytest.raises(TrelloAPIException) as excinfo:
            http_client.get("some_endpoint")
        assert "Error during request: Request Error" in str(excinfo.value)
