import pytest

from unittest.mock import Mock

from pytrello2.models import List, Card
from pytrello2.list import ListManager

from .utils import load_mock_data


# Constants for mock data file paths
LIST_MOCK_DATA = "list.json"
CARDS_MOCK_DATA = "cards.json"


# Fixture for the mock HTTP client
@pytest.fixture
def mock_http_client():
    return Mock()


# Test for get_list method
def test_get_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.get.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list = list_manager.get_list("test_list_id")

    assert isinstance(list, List)
    assert list.id == list_data["id"]
    assert list.name == list_data["name"]
    mock_http_client.get.assert_called_with("lists/test_list_id/")


# Test for create_list method
def test_create_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.post.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list = list_manager.create_list("test_name", "test_board_id")

    assert isinstance(list, List)
    assert list.id == list_data["id"]
    assert list.name == list_data["name"]
    assert list.closed == list_data["closed"]
    mock_http_client.post.assert_called_with(
        "lists/", {"name": "test_name", "idBoard": "test_board_id"}
    )


# Test for update_list method
def test_update_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.put.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list = list_manager.update_list("test_list_id")

    assert isinstance(list, List)
    assert list.id == list_data["id"]
    mock_http_client.put.assert_called_with("lists/test_list_id/", {})


# Test for archive_list method
def test_archive_list(mock_http_client):
    mock_http_client.post.return_value.status_code = 200

    list_manager = ListManager(mock_http_client)
    response = list_manager.archive_list("test_list_id")

    assert response.status_code == 200
    mock_http_client.post.assert_called_with(
        "lists/test_list_id/closed/", {"value": True}
    )


# Test for get_cards_on_list method
def test_get_cards_on_list(mock_http_client):
    cards_data = load_mock_data(CARDS_MOCK_DATA)
    mock_http_client.get.return_value = cards_data

    list_manager = ListManager(mock_http_client)
    cards = list_manager.get_cards_on_list("test_list_id")

    assert len(cards) == len(cards_data)

    for card, mock_data in zip(cards, cards_data):
        assert isinstance(card, Card)
        assert card.id == mock_data["id"]
        assert card.name == mock_data["name"]
    mock_http_client.get.assert_called_once_with("lists/test_list_id/cards/")
