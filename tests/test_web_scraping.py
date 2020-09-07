from web_scraping.scraper import *

def test_count():

    URL = "https://en.wikipedia.org/wiki/Petra"

    assert get_citations_needed_count(URL) == 5

def test_report():
    URL = "https://en.wikipedia.org/wiki/Petra"
    expected = open("test.txt", "r")

    assert get_citations_needed_report(URL) == expected.read()

