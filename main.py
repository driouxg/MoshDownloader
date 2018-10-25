from service.factory.lecture_metadata_parser import LectureMetadataParser
from service.factory.download_link_metadata_parser import DownloadLinkMetadataParser
from service.factory.lectures_factory import LecturesFactory
from service.factory.sections_factory import SectionsFactory
from service.html_tag_parser import HtmlTagParser
from service.downloader import Downloader
from service.title_grouper import TitleGrouper

base_url = "https://codewithmosh.com"
course_url = base_url + "/courses/357787/lectures/5634517"
sign_in_url = base_url + "/sign_in"

downloader = Downloader()
html = downloader.scrape_html(course_url)
html_parser = HtmlTagParser(html)
lecture_metadata_parser = LectureMetadataParser()
download_link_metadata_parser = DownloadLinkMetadataParser()

lecture_metadata = html_parser.find_lecture_metadata()
download_link_metadata = html_parser.find_download_metadata()
section_metadata = html_parser.find_section_metadata()

print(download_link_metadata)

lecture_data = lecture_metadata_parser.parse_lecture_headers(lecture_metadata)
lectures = LecturesFactory.create(lecture_data)
download_links = download_link_metadata_parser.parse_download_link(download_link_metadata)
grouped_lectures = TitleGrouper.create_groups(lectures)
sections = SectionsFactory.create(section_metadata, grouped_lectures)

print(grouped_lectures)
print(lectures)
print(sections)
