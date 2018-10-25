from domain.section import Section
import re


class SectionsFactory:
    pattern = 'n>\s+(?P<Title>[\w ]+)'

    @staticmethod
    def create(section_metadata, grouped_lectures):
        sections = []

        grouped_lecture_index = 0
        id = 1
        for metadatum in section_metadata:
            match = re.search(SectionsFactory.pattern, str(metadatum))

            if match:
                #print(match.groups())
                title = match.group('Title')
                sections.append(Section(int(id), title, grouped_lectures[grouped_lecture_index]))
                grouped_lecture_index += 1
                id += 1

        return sections
