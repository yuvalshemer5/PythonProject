class HomePage():

    def __init__(self, page):
        print ("into init")
        self.page = page

    def get_into_men_jackets_section(self):
        menu_button = self.page.locator("[data-qa-id='layout-header-toggle-menu']")
        menu_button.click()
        men_button = self.page.locator("[data-categoryid='1885841']")
        men_button.click()
        li_cat = self.page.locator('li[data-categoryid="2537410"]')
        li_cat.click()
        print("Successfully Got Into Jackets Category")

    def get_into_men_blazers_section(self):
        menu_button = self.page.locator("[data-qa-id='layout-header-toggle-menu']")
        menu_button.click()
        men_button = self.page.locator("[data-categoryid='1885841']")
        men_button.click()
        li_cat = self.page.locator('li[data-categoryid="2436309"]')
        li_cat.click()
        print("Successfully Got Into Blazers Category")

    def get_into_search_page(self):
        search_field = self.page.locator('[data-qa-id="header-search-text-link"]')
        search_field.click()
        print("Successfully Got Into Search Page")