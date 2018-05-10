from src.property import Property

__all__ = ['PropertyScraper']


class PropertyScraper:
    def __init__(self, url_fetcher):
        self.url_fetcher = url_fetcher
        self._url = ''

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def scrape(self) -> Property:
        raise NotImplementedError
