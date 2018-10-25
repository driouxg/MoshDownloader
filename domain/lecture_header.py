import json


class LectureHeader:

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_tuple(self):
        return self.id, self.title

    def __repr__(self):
        return json.dumps(self, default=lambda x: x.__dict__)
