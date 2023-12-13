import json
import os

from pytrello2.models.board import Board
from pytrello2.models.card import Card

# Constants for mock data file paths
BOARD_MOCK_DATA = "board.json"
CARD_MOCK_DATA = "card.json"


# Utility function to load mock data from a file
def load_mock_data(file_name):
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "data")
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)


# Test for board model
def test_board_model():
    mock_data = load_mock_data(BOARD_MOCK_DATA)
    board = Board(mock_data)

    assert board.id == mock_data["id"]
    assert board.name == mock_data["name"]
    assert board.desc == mock_data["desc"]
    assert board.closed == mock_data["closed"]
    assert board.url == mock_data["url"]


# Test for board str method
def test_board_str():
    mock_data = load_mock_data(BOARD_MOCK_DATA)
    board = Board(mock_data)

    expected_str = (
        f"Board(id={mock_data['id']}, name={mock_data['name']},"
        f" desc={mock_data['desc']}, url={mock_data['url']})"
    )
    assert str(board) == expected_str


# Test for card model
def test_card_model():
    mock_data = load_mock_data(CARD_MOCK_DATA)
    card = Card(mock_data)

    assert card.idList == mock_data["idList"]
    assert card.name == mock_data["name"]
    assert card.desc == mock_data["desc"]


# Test for card str method
def test_card_str():
    mock_data = load_mock_data(CARD_MOCK_DATA)
    card = Card(mock_data)

    expected_str = (
        f"Card(idList={mock_data['idList']}, name={mock_data['name']},"
        f" desc={mock_data['desc']},"
    )
    assert str(card) == expected_str
