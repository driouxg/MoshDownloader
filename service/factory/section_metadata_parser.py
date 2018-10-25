import re


class SectionMetadataParser:

    def __init__(self):
        self.pattern = 'n>\s+(?P<Title>[\w ]+)'

    #def parse_lecture_headers(self, lectures_metadata):
    #    lecture_header_matches = list(map(lambda x: self.search(x), lectures_metadata))
    #    lecture_headers = list(map(lambda x: self.to_lecture_header(x), lecture_header_matches))
    #    lecture_headers = self.remove_nils(lecture_headers)
    #    return lecture_headers
#
    #def search(self, metadatum):
    #    return re.search(self.pattern, str(metadatum))