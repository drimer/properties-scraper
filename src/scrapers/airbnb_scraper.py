from bs4 import BeautifulSoup

from src.property import Property
from src.scrapers.property_scraper import PropertyScraper

__all__ = ['AirbnbScraper']


class AirbnbScraper(PropertyScraper):
    def scrape_name(self, parser):
        summary = parser.find(id='summary')
        if not summary:
            return None

        h1 = summary.find('h1')
        if not h1:
            return None

        return h1.get_text()

    def scrape_type(self, parser):
        parent_span = parser.find('span', {'class': '_1k9f13qb'})
        if not parent_span:
            return None

        span = parent_span.find('span')
        if not span:
            return None

        return span.get_text()

    def scrape_number_bedrooms(self, parser):
        beds_text = [
            div.get_text() for div in
            parser.find_all('span', {'class': '_8xnct4e'})
            if div and 'bed' in div.get_text()
        ]

        if len(beds_text) == 0:
            return None

        return int(beds_text[0][0])

    def scrape_number_bathrooms(self, parser):
        bathrooms_text = [
            div.get_text() for div in
            parser.find_all('span', {'class': '_8xnct4e'})
            if div and 'bath' in div.get_text()
        ]

        if len(bathrooms_text) == 0:
            return None

        return int(bathrooms_text[0][0])

    def scrape_amenities(self, parser):
        section_title_divs = parser.find_all('div', {'class': '_281ya1u'})
        amenities_title_div = [
            div for div in section_title_divs
            if div and div.get_text() == 'Amenities'
        ]

        if len(amenities_title_div) == 0:
            return None

        amenities_whole_section = amenities_title_div[0].parent.parent.parent
        amenities_divs = amenities_whole_section.find_all('div', {'class': '_eqfc55u'})

        return [div.get_text() for div in amenities_divs] or None

    def scrape(self) -> Property:
        html = self.url_fetcher.fetch(self.url)
        parser = BeautifulSoup(html, 'html.parser')

        name = self.scrape_name(parser)
        type_ = self.scrape_type(parser)
        number_bedrooms = self.scrape_number_bedrooms(parser)
        number_bathrooms = self.scrape_number_bathrooms(parser)
        amenities = self.scrape_amenities(parser)

        property_ = Property(
            name=name,
            type_=type_,
            number_bedrooms=number_bedrooms,
            number_bathrooms=number_bathrooms,
            amenities=amenities,
        )

        if property_.all_is_unknown():
            return None
        else:
            return property_
