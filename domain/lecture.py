import json


class Lecture:

    def __init__(self, lecture_header):
        self.id = lecture_header.id
        self.title = lecture_header.title
        #self.id = id
        #self.title = title

    #def get_title(self):
    #    return self.title

    def __repr__(self):
        return json.dumps(self, default=lambda x: x.__dict__)
