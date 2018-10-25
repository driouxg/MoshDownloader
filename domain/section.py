import json


class Section:

    def __init__(self, id, title, lectures):
        self.__validate_id(id)
        self.title = title
        self.lectures = lectures

    # TODO: change this, it is doing validation and setting the value
    def __validate_id(self, id):
        if type(id) == int:
            self.id = id
        else:
            raise ValueError("Section ID must be of type 'int'")

    def get_title(self):
        return self.title

    def get_lectures(self):
        return self.lectures

    def __repr__(self):
        return json.dumps(self, default=lambda x: x.__dict__)
