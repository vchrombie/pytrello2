# pytrello2

<img
src="https://raw.githubusercontent.com/pytrello2/pytrello2/master/assets/pytrello2.png"
width="222" height="222" align="right">

[![CI
Python](https://github.com/5-jigglypuff/pytrello2/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/5-jigglypuff/pytrello2/actions/workflows/tests.yml)
[![Coverage
Status](https://coveralls.io/repos/github/5-jigglypuff/pytrello2/badge.svg?branch=master)](https://coveralls.io/github/5-jigglypuff/pytrello2?branch=master)
[![PyPI
version](https://badge.fury.io/py/pytrello2.svg)](https://badge.fury.io/py/pytrello2)

> Python wrapper for the Trello API

`pytrello2` is a Python wrapper and ORM that provides an easy way to interact
with the Trello API. Trello serves as a visual tool that enables teams to
effectively oversee various projects, workflows, or task tracking via boards
that can have files, checklists, and automation. `pytrello2` handles
authentication, mapping Python objects to Trello JSON, and provides a clean
interface for all API endpoints.

## Installation

You can install `pytrello2` using pip:

```bash
pip install pytrello2
```

You can also install `pytrello2` using Poetry:

```bash
cd pytrello2/
poetry install
poetry shell
```

## Authentication

A Trello API key and token is needed to use pytrello2. To set up authentication,
follow these steps:

1. Obtain your Trello API key by logging into Trello, and then visiting
   https://trello.com/1/appKey/generate.
2. Generate a token using the key, and grant the necessary permissions.

## Example

```py
import os
from pytrello2 import TrelloClient

# Replace 'YOUR_API_KEY' and 'YOUR_TOKEN' with your Trello API key and token.
token = os.environ["TRELLO_TOKEN"]
api_key = os.environ["TRELLO_API_KEY"]

client = TrelloClient(token, api_key)

# Get all boards of the authenticated user
boards = client.board.get_all_boards()

for board in boards:
    print(f"Board Name: {board.name}, Board ID: {board.id}")
```

## Contributing

Contributions are welcome!

Check out the [Contributing
Guidelines](https://github.com/pytrello2/pytrello2/blob/master/CONTRIBUTING.md)
for more details.

## License

This project is licensed under the MIT License - see the
[LICENSE](https://github.com/pytrello2/pytrello2/blob/master/LICENSE) file for
details.
