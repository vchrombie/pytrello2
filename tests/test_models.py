from pytrello2.models import Board, Card, List
from pytrello2.models.model import Model

from .utils import load_mock_data


# Constants for mock data file paths
BOARD_MOCK_DATA = "board.json"
CARD_MOCK_DATA = "card.json"
LIST_MOCK_DATA = "list.json"


# Test for model
def test_model():
    model = Model("test_id")

    assert model.id == "test_id"
    assert model.to_json() == '{\n    "id": "test_id"\n}'


# Test for board model
def test_board_model():
    mock_data = load_mock_data(BOARD_MOCK_DATA)
    board = Board(mock_data)

    assert board.id == mock_data["id"]
    assert board.name == mock_data["name"]


# Test for board str method
def test_board_str():
    mock_data = load_mock_data(BOARD_MOCK_DATA)
    board = Board(mock_data)

    expected_str = f"Board(id={mock_data['id']}, name={mock_data['name']})"
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


# Test for list model
def test_list_model():
    mock_data = load_mock_data(LIST_MOCK_DATA)
    list = List(mock_data)

    assert list.id == mock_data["id"]
    assert list.name == mock_data["name"]
    assert list.idBoard == mock_data["idBoard"]


# Test for list str method
def test_list_str():
    mock_data = load_mock_data(LIST_MOCK_DATA)
    list_data = List(mock_data)

    expected_str = (
        f"List(id={mock_data['id']}, name={mock_data['name']},"
        f" idBoard={mock_data['idBoard']})"
    )
    print(expected_str)
    assert str(list_data) == expected_str
