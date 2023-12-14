class ListClass:
    """
    Represents a Trello List.
    """

    def __init__(self, data):
        """
        Initializes a new List object.
        """
        self.id = data.get("id")
        self.idBoard = data.get("idBoard")
        self.name = data.get("name")
        self.url = data.get("url")

    def __str__(self):
        """
        Returns a string representation of a List object.
        """
        return (
            f"listclass(id={self.id}, idBoard={self.idBoard}," 
            f"name={self.name},id={self.id}, url={self.url})"
        )
