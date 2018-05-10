from dependency_injector import providers

from src.app.main_app import MainApp
from src.scrapers.airbnb_scraper import AirbnbScraper
from src.scrapers.property_scraper_factory import PropertyScraperFactory
from src.url_utils.url_fetcher import UrlFetcher

__all__ = ['DIContainer']


class DIContainer(object):
    url_fetcher = providers.Factory(UrlFetcher)

    property_scraper_factory = providers.Factory(
        PropertyScraperFactory,
    )
    airbnb_scraper = providers.Factory(
        AirbnbScraper,
        url_fetcher,
    )

    main_app = providers.Singleton(
        MainApp,
        property_scraper_factory,
    )
