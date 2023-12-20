import json


class Model:
    def __init__(self, id):
        """
        Initializes a new Model object.
        """
        self.id = id

    def to_json(self):
        """
        Returns a JSON string representation of the Model object.
        """
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
