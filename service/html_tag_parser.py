

class HtmlTagParser:

    def __init__(self, html):
        self.html = html
        #print(html)

    def find_all(self, tag, class_name):
        return self.html.find_all(tag, attrs={"class": class_name})

    def find_lecture_metadata(self):
        return self.find_all("span", "lecture-name")

    def find_section_metadata(self):
        return self.find_all("div", "section-title")

    def find_download_metadata(self):
        return self.find_all("div", "video-options")
