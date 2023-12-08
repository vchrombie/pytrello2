from pytrello2 import TrelloClient
from pytrello2.client import HttpClient
from pytrello2.board import BoardManager

TEST_API_KEY = "test_api_key"
TEST_TOKEN = "test_token"


# Test for TrelloClient class
def test_trello_client():
    client = TrelloClient(TEST_TOKEN, TEST_API_KEY)

    assert isinstance(client.http_client, HttpClient)
    assert isinstance(client.board, BoardManager)

    assert client.http_client.api_key == TEST_API_KEY
    assert client.http_client.token == TEST_TOKEN
