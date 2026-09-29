from wikibot import scrape

def test_scrape():
    result = scrape("Python (programming language)", sentences=2)
    assert "Python is an interpreted" in result

    result_disambiguation = scrape("Mercury", sentences=2)
    assert "Disambiguation error" in result_disambiguation

    result_page_error = scrape("ThisPageDoesNotExist12345", sentences=2)
    assert result_page_error == "Page not found."