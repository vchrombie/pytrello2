from .models.list import ListClass 


class ListManager:
    """
    Manages operations related to Trello Lists.
    """

    def __init__(self, client):
        """
        Initializes the ListManager with a client to handle requests to the Trello API.
        """
        self.client = client

    def get_list(self, list_id):
        """
        Returns a ListClass object with the given ID.
        """
        list_data = self.client.get(f"lists/{list_id}")
        return ListClass(list_data)

    def get_cards_on_list(self, list_id):
        """
        Returns a ListClass object with the given ID.
        """
        list_data = self.client.get(f"lists/{list_id}/cards/")
        return ListClass(list_data)

    def create_list(self, idBoard, name):
        """
        Returns a ListClass object with the given ID.
        """
        data = {}
        data["idBoard"] = idBoard
        data["name"] = name
        list_data = self.client.post("lists/", data)
        return ListClass(list_data)

    def update_list(self, list_id, idBoard, name):
        """
        Returns a ListClass object with the given ID.
        """
        data = {}
        data["idBoard"] = idBoard
        data["name"] = name
        list_data = self.client.put(f"lists/{list_id}", data)
        return ListClass(list_data)

    def archive_list(self, list_id):
        """
        Returns a ListClass object with the given ID.
        """
        list_data = self.client.post(f"lists/{list_id}/closed")
        return ListClass(list_data)
