import urllib.request

__all__ = ['UrlFetcher']


class UrlFetcher:
    def fetch(self, url):
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read()

        return html
