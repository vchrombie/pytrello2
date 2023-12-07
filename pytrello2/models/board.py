class Board:
    """
    Represents a Trello board.
    """

    def __init__(self, data):
        """
        Initializes a new Board object.
        """
        self.id = data.get("id")
        self.name = data.get("name")
        self.desc = data.get("desc")
        self.closed = data.get("closed")
        self.url = data.get("url")

    def __str__(self):
        """
        Returns a string representation of a Board object.
        """
        return (
            f"Board(id={self.id}, name={self.name}, desc={self.desc}, url={self.url})"
        )
