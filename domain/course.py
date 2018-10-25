import json


class Course:

    def __init__(self, title, sections):
        self.title = title
        self.sections = sections

    def getTitle(self):
        return self.title

    def getSections(self):
        return self.sections

    def __repr__(self):
        return json.dumps(self, default=lambda x: x.__dict__)
