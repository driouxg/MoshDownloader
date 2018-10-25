import re


class DownloadLinkMetadataParser:

    def __init__(self):
        self.pattern = ''

    def parse_download_link(self, download_metadatum):
        return

    def search(self, metadatum):
        return re.search(self.pattern, str(metadatum))
