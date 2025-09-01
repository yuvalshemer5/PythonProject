class SearchPage():

    def __init__(self, page):
        print ("into init")
        self.page = page

    def search_product_vinyl_print(self):
        search_box = self.page.locator("#search-home-form-combo-input")
        search_box.click()
        search_box.fill("VINYL PRINT T-SHIRT")
        self.page.keyboard.press("Enter")
        men_search_button = self.page.get_by_role("button", name="Man").nth(1)
        men_search_button.click()
        the_product = self.page.locator('a[href*="vinyl-print-t-shirt"]').nth(0)
        the_product.click()
        print("Successfully got into the product page")

    def search_product_suede_leather_jacket(self):  #SUEDE LEATHER JACKET
        search_box = self.page.locator("#search-home-form-combo-input")
        search_box.click()
        search_box.fill("SUEDE LEATHER JACKET")
        self.page.keyboard.press("Enter")
        men_search_button = self.page.get_by_role("button", name="Man").nth(1)
        men_search_button.click()
        the_product = self.page.locator('a[href*="suede-leather-jacket"]').nth(0)
        the_product.click()
        print("Successfully got into the product page")

    def search_product_has_colors(self):
        search_box = self.page.locator("#search-home-form-combo-input")
        search_box.click()
        search_box.fill("WASHED HEAVYWEIGHT T-SHIRT")
        self.page.keyboard.press("Enter")
        men_search_button = self.page.get_by_role("button", name="Man").nth(1)
        men_search_button.click()
        the_product = self.page.locator('a[href*="washed-heavyweight-t-shirt"]').nth(0)
        the_product.click()
        print("Successfully got into the product page")

    def search_product_without_colors(self):
        search_box = self.page.locator("#search-home-form-combo-input")
        search_box.click()
        search_box.fill("SUN PRINT T-SHIRT")
        self.page.keyboard.press("Enter")
        men_search_button = self.page.get_by_role("button", name="Man").nth(1)
        men_search_button.click()
        the_product = self.page.locator('a[href*="sun-print-t-shirt"]').nth(0)
        the_product.click()
        print("Successfully got into the product page")









