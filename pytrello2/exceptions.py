class TrelloAPIException(Exception):
    """
    Base exception class for Trello API errors.
    """

    def __init__(self, message=None, status_code=None):
        super().__init__(message)
        self.status_code = status_code
