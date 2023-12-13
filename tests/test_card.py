import json
import os
import pytest

from unittest.mock import Mock
from pytrello2.models.card import Card
from pytrello2.card import CardManager

# Constants for mock data file paths
CARD_MOCK_DATA = "card.json"


# Utility function to load mock data from a file
def load_mock_data(file_name):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(current_dir, "data")
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)


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
    mock_http_client.get.assert_called_once_with("cards/test_card_id")


def test_create_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.post.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.create_card("test_id_list", "test_desc")

    assert isinstance(card, Card)
    assert card.id == card_data["id"]


def test_delete_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.delete.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.delete_card("test_card_id")

    assert isinstance(card, Card)


def test_update_card(mock_http_client):
    card_data = load_mock_data(CARD_MOCK_DATA)
    mock_http_client.put.return_value = card_data

    card_manager = CardManager(mock_http_client)
    card = card_manager.update_card("test_card_id", "idList", "desc")

    assert isinstance(card, Card)
    assert card.id == card_data["id"]
