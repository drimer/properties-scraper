from unittest import mock

import pytest

from src.scrapers.airbnb_scraper import AirbnbScraper


@pytest.fixture
def property_1_fetcher():
    fetcher = mock.Mock()
    with open('test/assets/property_14531512.html', 'r') as f:
        fetcher.fetch.return_value = f.read()

    return fetcher


@pytest.fixture
def property_2_fetcher():
    fetcher = mock.Mock()
    with open('test/assets/property_19278160.html', 'r') as f:
        fetcher.fetch.return_value = f.read()

    return fetcher


@pytest.fixture
def property_3_fetcher():
    fetcher = mock.Mock()
    with open('test/assets/property_missing_data.html', 'r') as f:
        fetcher.fetch.return_value = f.read()

    return fetcher


def test_that_retrieves_correct_data_from_html(
        property_1_fetcher,
):
    scraper = AirbnbScraper(property_1_fetcher)
    property_ = scraper.scrape()

    assert property_.name == 'Garden Rooms: Featured in Grand Designs Sept 2017'
    assert property_.type == 'Entire guesthouse'
    assert property_.number_bedrooms == 1
    assert property_.number_bathrooms == 1
    assert sorted(property_.amenities) == sorted([
        'Kitchen',
        'Hair dryer',
        'Wireless Internet',
        'TV',
        'Cable TV',
        'Laptop friendly workspace',
    ])


def test_that_retrieves_correct_data_from_html_2(
        property_2_fetcher,
):
    scraper = AirbnbScraper(property_2_fetcher)
    property_ = scraper.scrape()

    assert property_.name == 'York Place: Luxurious  apartment For Two adults.'
    assert property_.type == 'Entire flat'
    assert property_.number_bedrooms == 1
    assert property_.number_bathrooms == 1
    assert sorted(property_.amenities) == sorted([
        'Kitchen',
        'TV',
        'Wireless Internet',
        'Laptop friendly workspace',
        'Hair dryer',
        'Iron',
    ])


def test_that_retrieves_empty_property_when_page_misses_fields(
        property_3_fetcher,
):
    scraper = AirbnbScraper(property_3_fetcher)
    property_ = scraper.scrape()

    assert property_ is None
