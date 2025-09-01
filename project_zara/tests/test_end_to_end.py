from project_zara.pages.cart_page import CartPage
from project_zara.pages.home_page import HomePage
from project_zara.pages.product_page import ProductPage
from project_zara.pages.search_page import SearchPage
class TestZaraOnlineStore():


    def test_searching_product_and_adding_to_cart(self, setup_zara): #testing E2E process of searching a product and adding it to the cart
        page = setup_zara
        home_page = HomePage(page)
        search_page = SearchPage(page)
        cart_page = CartPage(page)
        product_page = ProductPage(page)
        home_page.get_into_search_page()
        search_page.search_product_vinyl_print()
        product_page.add_product_to_cart()
        page.wait_for_timeout(1000) #waiting for product to be added to the cart
        count = cart_page.get_item_count()
        assert count == 1, f"Expected 1 item in cart, but found {count}"

    def test_if_product_has_colors_options__true(self, setup_zara): #testing a product with colors if it has colors
        page = setup_zara
        home_page = HomePage(page)
        search_page = SearchPage(page)
        product_page = ProductPage(page)
        home_page.get_into_search_page()
        search_page.search_product_has_colors()
        page.wait_for_timeout(2000) #wait for page to load
        has_colors = product_page.check_if_product_has_colors()
        assert has_colors, "I expected the product to have color options but none were found."

    def test_if_product_has_colors_options__false(self, setup_zara): #testing a product without colors if it has colors
        page = setup_zara
        home_page = HomePage(page)
        search_page = SearchPage(page)
        product_page = ProductPage(page)
        home_page.get_into_search_page()
        search_page.search_product_without_colors()
        page.wait_for_timeout(2000) #wait for page to load
        has_colors = product_page.check_if_product_has_colors()
        assert has_colors, "I expected the product to have color options but none were found."

    def test_get_into_mens_jackets(self, setup_zara): #testing getting into jackets category and checking if the URL is right
        page = setup_zara
        home_page = HomePage(page)
        home_page.get_into_men_jackets_section()
        assert page.url == "https://www.zara.com/il/en/man-jackets-l640.html?v1=2536906", "Test URL is not expected"

    def test_get_into_mens_blazers(self, setup_zara): #testing getting into blazers category and checking if the URL is right
        page = setup_zara
        home_page = HomePage(page)
        home_page.get_into_men_blazers_section()
        assert page.url == "https://www.zara.com/il/en/man-blazers-l608.html?v1=2436311", "Test URL is not expected"


    def test_price_lower_500__passes(self,setup_zara): #compare product's price to 500 - lower, needs to pass
        page = setup_zara
        home_page = HomePage(page)
        product_page = ProductPage(page)
        search_page = SearchPage(page)
        home_page.get_into_search_page()
        search_page.search_product_vinyl_print()
        price = product_page.get_product_price()
        assert price < 500, f"product's price is {price} which is greater than 500"

    def test_price_lower_500__fails(self,setup_zara): #compare product's price to 500 - higher, needs to fail
        page = setup_zara
        home_page = HomePage(page)
        search_page = SearchPage(page)
        product_page = ProductPage(page)
        home_page.get_into_search_page()
        search_page.search_product_suede_leather_jacket()
        price = product_page.get_product_price()
        assert price < 500, f"first product on the jackets category price is {price} which is greater than 500"