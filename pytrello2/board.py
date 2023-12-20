from .models import Board, List


class BoardManager:
    """
    Manages operations related to Trello Boards.
    """

    def __init__(self, client):
        """
        Initializes the BoardManager with a client to handle requests to the
        Trello API.
        """
        self.client = client

    def get_board(self, board_id):
        """
        Retrieves a board with the given ID.

        Parameters:
            - board_id (str): The unique identifier of the board.
        """
        board = self.client.get(f"boards/{board_id}/")
        return Board(board)

    def create_board(self, name, **kwargs):
        """
        Creates a new board.

        Parameters:
            - name (str): The name of the board.
            - kwargs: Additional options for the board.
        """
        data = {"name": name}
        data.update(kwargs)
        board = self.client.post("boards/", data)
        return Board(board)

    def delete_board(self, board_id):
        """
        Deletes a Board object with the given ID.
        """
        return self.client.delete(f"boards/{board_id}/")

    def get_boards_by_filter(self, filter=None):
        """
        Returns a list of boards matching the given filter.

        Parameters:
            - filter (str): The filter to use to match boards.
        """
        params = {"filter": filter} if filter else {}
        boards = self.client.get("members/me/boards/", params=params)
        return [Board(board) for board in boards]

    def get_all_boards(self):
        """
        Returns a list of all boards.
        """
        return self.get_boards_by_filter(filter="all")

    def get_lists_on_board(self, board_id):
        """
        Returns a list of lists on the given board.

        Parameters:
            - board_id (str): The unique identifier of the board.
        """
        lists = self.client.get(f"boards/{board_id}/lists/")
        return [List(list) for list in lists]
