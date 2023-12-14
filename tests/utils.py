import os
import json


def load_mock_data(file_name):
    """
    Load mock data from a JSON file
    :param file_name: Name of the JSON file
    :return: JSON data
    """
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(current_dir, "data")
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, "r") as file:
        return json.load(file)
