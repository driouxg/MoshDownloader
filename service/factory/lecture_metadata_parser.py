import re

from domain.lecture_header import LectureHeader


class LectureMetadataParser:

    def __init__(self):
        self.pattern = '(?P<LectureNumber>[0-9]+) ?- (?P<Title>[A-Za-z -]+)'

    def parse_lecture_headers(self, lectures_metadata):
        lecture_header_matches = list(map(lambda x: self.search(x), lectures_metadata))
        lecture_headers = list(map(lambda x: self.to_lecture_header(x), lecture_header_matches))
        lecture_headers = self.remove_nils(lecture_headers)
        return lecture_headers

    def search(self, metadatum):
        return re.search(self.pattern, str(metadatum))

    def to_lecture_header(self, lecture_header_match):
        if lecture_header_match:
            id = lecture_header_match.group('LectureNumber')
            title = lecture_header_match.group('Title')

            return LectureHeader(int(id), title)

    def remove_nils(self, list):
        return [x for x in list if x is not None]
