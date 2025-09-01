import re

class ProductPage():
    def __init__(self,page):
        print("into init")
        self.page = page

    def add_product_to_cart(self):
        add_to_cart_button = self.page.locator('button[data-qa-action="add-to-cart"]')
        add_to_cart_button.click()
        size_button = self.page.locator('div[data-qa-qualifier="size-selector-sizes-size-label"]', has_text="M")
        size_button.click()
        shopping_bag_button = self.page.get_by_role("button", name="See shopping basket")
        shopping_bag_button.click()
        print("product was added successfully")

    def check_if_product_has_colors(self):
        locator = self.page.locator(".product-detail-color-selector__color-selector-container")
        return locator.is_visible()

    def get_product_price(self):
        first_price_text = self.page.locator("span.money-amount__main").first.text_content()
        print("Raw price text:", first_price_text)
        match = re.search(r"(\d[\d,\.]*)", first_price_text)
        assert match, "No price found in the first element"
        normalized = match.group(1).replace(",", "")
        price_value = int(float(normalized))
        print("Actual price:", price_value)
        return price_value