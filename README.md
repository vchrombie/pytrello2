# pytrello2

<img src="./assets/pytrello2.png" width="160" height="160" align="right">

[![CI Python](https://github.com/5-jigglypuff/pytrello2/actions/workflows/ci-python.yml/badge.svg?branch=master)](https://github.com/5-jigglypuff/pytrello2/actions/workflows/ci-python.yml) 
[![Coverage Status](https://coveralls.io/repos/github/5-jigglypuff/pytrello2/badge.svg?branch=master)](https://coveralls.io/github/5-jigglypuff/pytrello2?branch=master) 
[![PyPI version](https://badge.fury.io/py/pytrello2.svg)](https://badge.fury.io/py/pytrello2)

> Python wrapper for the Trello API

`pytrello2` is a Python wrapper and ORM that provides an easy way to interact with the Trello API. It handles authentication, mapping Python objects to Trello JSON, and provides a clean interface for all API endpoints.

## Installation

```python
pip install pytrello2
```

## Getting started

1. Clone your new repository to your local machine.
    ```bash
    git clone https://github.com/5-jigglypuff/pytrello2
    ```
2. Install the required dependencies using Poetry.
    ```bash
    poetry install
    ```
3. Activate the virtual environment using Poetry.
    ```bash
    poetry shell
    ```
4. Run static analysis using flake8.
    ```bash
    flake8
    ```
5. Run code formatting using black.
    ```bash
    black .
    ```
6. Run tests using pytest.
    ```bash
    pytest
    ```

## Authentication

A Trello API key and token is needed to use pytrello2.  To set up authentication, follow these steps:

1. Obtain your Trello API key by logging into Trello, and then visiting <https://trello.com/1/appKey/generate>.
2. Generate a token using the key, and grant the necessary permissions.

## Examples

```python
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
```
    
## Contributing

Contributions are welcome! Check out the [Contribution Guidelines](./CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
