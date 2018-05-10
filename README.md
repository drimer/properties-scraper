Description of the problem solved
=================================

TravelNest Homework Exercise: Airbnb Scraper

Please write some code that scrapes property name, property type
(e.g Apartment), number of bedrooms, bathrooms and list of the amenities for
the following 3 properties:

    https://www.airbnb.co.uk/rooms/14531512?s=51
    https://www.airbnb.co.uk/rooms/19278160?s=51
    https://www.airbnb.co.uk/rooms/19292873?s=51

Steps to set up
===============

- Install Python 3
- (optional) Make a virtual environment: `mkvirtualenv -p $(which python3) travelnest`
- `pip install -r requirements.txt`

Running the app
===============

- `python main.py`

Running the tests
=================

- `pip install -r dev_requirements.txt`
- `pytest`

Notes for who reviews my code
=============================

Given that I shouldn't spend more than a few hours, I've focused on a handful
of aspects:
- Code that is easily "unit-testable". By using dependency injection and
  loosely coupled classes.
- Code that is easily extended, so that we have various parsers for different
  services, eg: booking.com. Just inherit from `PropertyScraper` and register
  the new scraper in the `PropertyScraperFactory`, and we're done.
- Minimally decent test coverage. Although my tests are actually far from
  good, they at least give me some confidence on the most critical part, which
  is how I parse the HTML.
  
Things I would improve if I were to work on this in my daily job:
- Better documentation. I'm not a fan of in-line comments or such things, as
  that would mean that my code is not clear enough. Still, some basic
  descriptive docstrings in classes and public methods would be
  desirable.
- Higher test coverage. The tests for the parser only have two properties
  with all their data, and one with no html body at all. It would be good
  to add assets that have everything but the number of beds, or
  everything but the amenities, etc. Also, there are only tests for the
  class AirbnbParser. The rest of the classes should also be unit tested.
- End to end tests. But not going too crazy on these. Just to give me
  confidence that the whole setup with DI, etc works as expected.
- Better handling of errors during the parsing of the data. I've rushed
  through this a bit, and I believe that if I were to whiteboard some of this,
  I would probably go for a slightly different approach. For example,
  setting some of the property's fields to `None` to tell that we don't know 
  what those could be, might not be a great idea.
- I would add a mechanism to limit the times per X seconds we can retrieve the
  pages. I'm fairly sure that Airbnb and other services could detect too many
  requests from an IP address, and they'd block it. That's why I think we'd
  need this sort of mechanism, just to avoid raising red flags.
- I'd design a clean way of dealing with common errors like: network errors
  while fetching the pages, urls not being known (different than 
  "airbnb.co.uk"), etc.

Extra notes:
- At the time of writing this code, the third URL doesn't exist, and gets
  redirected to the main page of Airbnb. This may also happen with the other
  two urls when you're reviewing this code. If you want to modify the property
  urls, it should be as easy as modifying the list in  `MainApp.run()`.
