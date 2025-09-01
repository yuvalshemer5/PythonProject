import re

class CartPage():
    CART_LINK = 'a[data-qa-action="shop-navigation-link-Shopping_bag"]'

    def __init__(self,page):
        print("into init")
        self.page = page


    def get_item_count(self) -> int:
        text = self.page.locator(self.CART_LINK).text_content().strip()
        match = re.search(r"\[(\d+)\]", text)
        return int(match.group(1)) if match else 0
