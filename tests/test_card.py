import pytest

from unittest.mock import Mock

from pytrello2.models import Card
from pytrello2.card import CardManager

from .utils import load_mock_data


# Constants for mock data file paths
CARD_MOCK_DATA = "card.json"


# Fixture for the mock HTTP client
@pytest.fixture
def mock_http_client():
    return Mock()


# Test for get_card method
def test_get_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.get.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.get_card("test_card_id")

    assert isinstance(card, Card)
    assert card.id == card_data["id"]
    assert card.name == card_data["name"]
    mock_http_client.get.assert_called_once_with("cards/test_card_id/")


# Test for create_card method
def test_create_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.post.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.create_card("test_id_list")

    assert isinstance(card, Card)
    assert card.id == card_data["id"]
    assert card.name == card_data["name"]
    assert card.idList == card_data["idList"]
    mock_http_client.post.assert_called_once_with("cards/", {"idList": "test_id_list"})


# Test for update_card method
def test_update_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.put.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.update_card("test_card_id")

    assert isinstance(card, Card)
    assert card.id == card_data["id"]
    mock_http_client.put.assert_called_once_with("cards/test_card_id/", {})


# Test for delete_card method
def test_delete_card(mock_http_client):
    mock_http_client.delete.return_value.status_code = 200

    card_manager = CardManager(mock_http_client)
    response = card_manager.delete_card("test_card_id")

    assert response.status_code == 200
    mock_http_client.delete.assert_called_once_with("cards/test_card_id/")
