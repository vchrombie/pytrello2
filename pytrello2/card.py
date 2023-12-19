from .models import Card


class CardManager:
    """
    Manages operations related to Trello cards.
    """

    def __init__(self, client):
        """
        Initializes the CardManager with a client to handle requests to the Trello API.
        """
        self.client = client

    def get_card(self, card_id):
        """
        Returns a Card object with the given ID.
        """
        card_data = self.client.get(f"cards/{card_id}")
        return Card(card_data)

    def create_card(self, idList, desc):
        """
        Returns a Card object with the given ID.
        """
        data = {}
        data["idList"] = idList
        data["desc"] = desc
        card_data = self.client.post("cards/", data)
        return Card(card_data)

    def delete_card(self, card_id):
        """
        Returns a Card object with the given ID.
        """
        card_data = self.client.delete(f"cards/{card_id}")
        return Card(card_data)

    def update_card(self, card_id, idList, desc):
        """
        Returns a Card object with the given ID.
        """
        data = {}
        data["idList"] = idList
        data["desc"] = desc
        card_data = self.client.put(f"cards/{card_id}", data)
        return Card(card_data)
