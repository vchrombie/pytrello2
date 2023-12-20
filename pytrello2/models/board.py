from .model import Model


class Board(Model):
    """
    Represents a Trello Board.
    """

    def __init__(self, data):
        """
        Initializes a new Board object.
        """
        super().__init__(data.get("id"))
        self.__dict__.update(data)

    def __str__(self):
        """
        Returns a string representation of a Board object.
        """
        return f"Board(id={self.id}, name={self.name})"
