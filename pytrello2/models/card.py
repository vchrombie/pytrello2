class Card:
    """
    Represents a Trello board.
    """

    def __init__(self, data):
        """
        Initializes a new Card object.
        """
        self.id = data.get("id")
        self.idList = data.get("idList")
        self.idBoard = data.get("board_id")
        self.name = data.get("name")
        self.desc = data.get("desc")
        self.due = data.get("due")
        self.start = data.get("start")
        self.url = data.get("url")

    def __str__(self):
        """
        Returns a string representation of a Card object.
        """
        return f"Card(idList={self.idList}, name={self.name}, desc={self.desc},"
