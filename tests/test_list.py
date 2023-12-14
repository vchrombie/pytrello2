import json
import os
import pytest

from unittest.mock import Mock
from pytrello2.models.list import ListClass
from pytrello2.list import ListManager

# Constants for mock data file paths
LIST_MOCK_DATA = "list.json"


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


# Test for get_list method
def test_get_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.get.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.get_list("test_list_id")

    assert isinstance(list_type, ListClass)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


# Test for get_all_boards method
def test_get_cards_on_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.get.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.get_cards_on_list("test_list_id")

    assert isinstance(list_type, ListClass)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


def test_create_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.post.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.create_list("test_board_id", "test_name")

    assert isinstance(list_type, ListClass)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


def test_update_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.put.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.update_list("test_list_id", "test_board_id", "test_name")

    assert isinstance(list_type, ListClass)
    assert list_type.id == list_data["id"]


def test_delete_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.post.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.archive_list("test_list_id")

    assert isinstance(list_type, ListClass)
