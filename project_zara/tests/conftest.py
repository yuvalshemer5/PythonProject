import pytest

from playwright.sync_api import sync_playwright

@pytest.fixture

def setup_zara():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.zara.com/il/en/", wait_until="load") #waiting for whole homepage to load to ensure reliability

        yield page
        page.close()
        browser.close()
        print ("Test End")
