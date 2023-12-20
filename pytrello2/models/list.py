from .model import Model


class List(Model):
    """
    Represents a Trello List.
    """

    def __init__(self, data):
        """
        Initializes a new List object.
        """
        self.id = data.get("id")
        self.__dict__.update(data)

    def __str__(self):
        """
        Returns a string representation of a List object.
        """
        return f"List(id={self.id}, name={self.name}, idBoard={self.idBoard})"
