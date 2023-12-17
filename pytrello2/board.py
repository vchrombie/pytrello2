from .models.board import Board


class BoardManager:
    """
    Manages operations related to Trello boards.
    """

    def __init__(self, client):
        """
        Initializes the BoardManager with a client to handle requests to the Trello API.
        """
        self.client = client

    def get_board(self, board_id):
        """
        Returns a Board object with the given ID.
        """
        board_data = self.client.get(f"boards/{board_id}")
        return Board(board_data)

    def get_boards_by_filter(self, filter=None):
        """
        Returns a list of Board objects that match the given filter.
        """
        params = {"filter": filter} if filter else {}
        boards_data = self.client.get("members/me/boards", params=params)
        return [Board(board_data) for board_data in boards_data]

    def get_all_boards(self):
        """
        Returns a list of Board objects for all boards.
        """
        return self.get_boards_by_filter(filter="all")

    def create_board(self, name, desc):
        """
        Creates a new Board object.
        """
        data = {}
        data["name"] = name
        data["desc"] = desc
        board_data = self.client.post("boards/", data)
        return Board(board_data)

    def delete_board(self, board_id):
        """
        Deletes a Board object with the given ID.
        """
        return self.client.delete(f"boards/{board_id}")
