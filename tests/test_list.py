import pytest

from unittest.mock import Mock

from pytrello2.models.list import List
from pytrello2.list import ListManager

from .utils import load_mock_data


# Constants for mock data file paths
LIST_MOCK_DATA = "list.json"


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

    assert isinstance(list_type, List)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


# Test for get_cards_on_list method
def test_get_cards_on_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.get.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.get_cards_on_list("test_list_id")

    assert isinstance(list_type, List)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


# Test for create_list method
def test_create_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.post.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.create_list("test_board_id", "test_name")

    assert isinstance(list_type, List)
    assert list_type.id == list_data["id"]
    assert list_type.name == list_data["name"]


# Test for update_list method
def test_update_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.put.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.update_list("test_list_id", "test_board_id", "test_name")

    assert isinstance(list_type, List)
    assert list_type.id == list_data["id"]


# Test for archive_list method
def test_archive_list(mock_http_client):
    list_data = load_mock_data(LIST_MOCK_DATA)
    mock_http_client.post.return_value = list_data

    list_manager = ListManager(mock_http_client)
    list_type = list_manager.archive_list("test_list_id")

    assert isinstance(list_type, List)
