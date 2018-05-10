from src.scrapers.property_scraper import PropertyScraper

__all__ = ['PropertyScraperFactory']


class PropertyScraperFactory:
    def get(self, url: str) -> PropertyScraper:
        from src.dependency_injection.container import DIContainer

        # Depending on the domain of the url, we'd return a different
        # PropertyScraper
        scraper = DIContainer.airbnb_scraper()
        scraper.url = url
        return scraper
