from domain.lecture import Lecture


class LecturesFactory:

    @staticmethod
    def create(lecture_headers):
        lectures = list(map(lambda x: Lecture(x), lecture_headers))
        return lectures
