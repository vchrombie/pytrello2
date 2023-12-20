from .models import Card


class CardManager:
    """
    Manages operations related to Trello Cards.
    """

    def __init__(self, client):
        """
        Initializes the CardManager with a client to handle requests to the
        Trello API.
        """
        self.client = client

    def get_card(self, card_id):
        """
        Retrieves a card with the given ID.

        Parameters:
            - card_id (str): The unique identifier of the card.
        """
        card = self.client.get(f"cards/{card_id}/")
        return Card(card)

    def create_card(self, list_id, **kwargs):
        """
        Creates a new card on a specified list.

        Parameters:
            - list_id (str): The unique identifier of the list to add the card to.
            - kwargs: Additional options for the card.
        """
        data = {"idList": list_id}
        data.update(kwargs)
        card = self.client.post("cards/", data)
        return Card(card)

    def update_card(self, card_id, **kwargs):
        """
        Updates a card with the given ID.

        Parameters:
            - card_id (str): The unique identifier of the card.
            - kwargs: Additional options for the card.
        """
        data = {}
        data.update(kwargs)
        card = self.client.put(f"cards/{card_id}/", data)
        return Card(card)

    def delete_card(self, card_id):
        """
        Deletes a card with the given ID.

        Parameters:
            - card_id (str): The unique identifier of the card.
        """
        return self.client.delete(f"cards/{card_id}/")
