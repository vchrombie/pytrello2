from .models import List, Card


class ListManager:
    """
    Manages operations related to Trello Lists.
    """

    def __init__(self, client):
        """
        Initializes the ListManager with a client to handle requests to the
        Trello API.
        """
        self.client = client

    def get_list(self, list_id):
        """
        Retrieves a specific list by its ID.

        Parameters:
            - list_id (str): The unique identifier of the list.
        """
        list = self.client.get(f"lists/{list_id}/")
        return List(list)

    def create_list(self, name, board_id, **kwargs):
        """
        Creates a new list on a specified board.

        Parameters:
            - name (str): The name of the new list.
            - board_id (str): The unique identifier of the board where the list
              will be created.
        """
        data = {"name": name, "idBoard": board_id}
        data.update(kwargs)
        list = self.client.post("lists/", data)
        return List(list)

    def update_list(self, list_id, **kwargs):
        """
        Updates a list with the given ID.

        Parameters:
            - list_id (str): The unique identifier of the list.
            - kwargs: Additional options for the list.
        """
        data = {}
        data.update(kwargs)
        list_data = self.client.put(f"lists/{list_id}/", data)
        return List(list_data)

    def archive_list(self, list_id):
        """
        Archives a list with the given ID.

        Parameters:
            - list_id (str): The unique identifier of the list to archive.
        """
        return self.client.post(f"lists/{list_id}/closed/", {"value": True})

    def get_cards_on_list(self, list_id):
        """
        Retrieves all cards on a specific list.

        Parameters:
            - list_id (str): The unique identifier of the list.
        """
        cards = self.client.get(f"lists/{list_id}/cards/")
        return [Card(card) for card in cards]
