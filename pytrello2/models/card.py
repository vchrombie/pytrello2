from .model import Model


class Card(Model):
    """
    Represents a Trello Card.
    """

    def __init__(self, data):
        """
        Initializes a new Card object.
        """
        self.id = data.get("id")
        self.__dict__.update(data)

    def __str__(self):
        """
        Returns a string representation of a Card object.
        """
        return f"Card(id={self.id}, idList={self.idList})"
