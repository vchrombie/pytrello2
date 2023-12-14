import pytest

from unittest.mock import Mock

from pytrello2.models.board import Board
from pytrello2.board import BoardManager

from .utils import load_mock_data


# Constants for mock data file paths
BOARD_MOCK_DATA = "board.json"
BOARDS_MOCK_DATA = "boards.json"


# Fixture for the mock HTTP client
@pytest.fixture
def mock_http_client():
    return Mock()


# Test for get_board method
def test_get_board(mock_http_client):
    board_data = load_mock_data(BOARD_MOCK_DATA)
    mock_http_client.get.return_value = board_data

    board_manager = BoardManager(mock_http_client)
    board = board_manager.get_board("test_board_id")

    assert isinstance(board, Board)
    assert board.id == board_data["id"]
    assert board.name == board_data["name"]
    mock_http_client.get.assert_called_once_with("boards/test_board_id")


# Test for get_all_boards method
def test_get_all_boards(mock_http_client):
    boards_data = load_mock_data(BOARDS_MOCK_DATA)
    mock_http_client.get.return_value = boards_data

    board_manager = BoardManager(mock_http_client)
    boards = board_manager.get_all_boards()

    assert len(boards) == len(boards_data)

    for board, mock_data in zip(boards, boards_data):
        assert isinstance(board, Board)
        assert board.id == mock_data["id"]
        assert board.name == mock_data["name"]
    mock_http_client.get.assert_called_once_with(
        "members/me/boards", params={"filter": "all"}
    )


# Test for create_board method
def test_create_board(mock_http_client):
    board_data = load_mock_data(BOARD_MOCK_DATA)
    mock_http_client.post.return_value = board_data

    board_manager = BoardManager(mock_http_client)
    board = board_manager.create_board("test_board", "test_todo")

    assert isinstance(board, Board)
    assert board.id == board_data["id"]
