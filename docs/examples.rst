Examples
========

.. code-block::

    from pytrello2 import TrelloClient

    # Replace 'YOUR_API_KEY' and 'YOUR_TOKEN' with your Trello API key and token.
    client = TrelloClient(api_key='YOUR_API_KEY', token='YOUR_TOKEN')

    # Get boards
    boards = client.get_boards()
    for board in boards:
        print(f"Board Name: {board.name}, Board ID: {board.id}")

    # Create a new board
    new_board = client.create_board(name='New Board', description='Here are some details about the new board')
    print(f"New board named {new_board.name} with board ID {new_board.id} has been created.")