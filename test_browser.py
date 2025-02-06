from selene import browser, be, have

def test_search_results(open_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('4pda').press_enter()
    browser.element('html').should(have.text('4PDA'))

def test_search_no_results(open_browser):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('dasczxasdasd1232213123123dasdczxxzczxczxasdasdasdasdasdasdasdasdasdasdasda').press_enter()
    browser.element('html').should(have.text('результаты не найдены'))

