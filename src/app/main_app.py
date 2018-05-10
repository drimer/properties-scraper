from src.scrapers.property_scraper_factory import PropertyScraperFactory


class MainApp:
    def __init__(self, scraper_factory: PropertyScraperFactory):
        self.scraper_factory = scraper_factory

    def run(self):
        urls = (
            'https://www.airbnb.co.uk/rooms/14531512?s=51',
            'https://www.airbnb.co.uk/rooms/19278160?s=51',
            'https://www.airbnb.co.uk/rooms/19292873?s=51',
        )
        properties = [self.scraper_factory.get(url).scrape() for url in urls]

        for count, property_ in enumerate(properties):
            print('{} - Property scraped:\n{}'.format(
                count + 1, str(property_))
            )
