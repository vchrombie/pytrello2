from pytrello2 import TrelloClient
from pytrello2.client import HttpClient
from pytrello2.board import BoardManager
from pytrello2.card import CardManager
from pytrello2.list import ListManager


TEST_API_KEY = "test_api_key"
TEST_TOKEN = "test_token"


# Test for TrelloClient class
def test_trello_client():
    client = TrelloClient(TEST_TOKEN, TEST_API_KEY)

    assert isinstance(client.http_client, HttpClient)
    assert isinstance(client.board, BoardManager)
    assert isinstance(client.card, CardManager)
    assert isinstance(client.list, ListManager)

    assert client.http_client.api_key == TEST_API_KEY
    assert client.http_client.token == TEST_TOKEN
