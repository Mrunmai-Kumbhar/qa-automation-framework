from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_to_cart(driver):

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page = InventoryPage(driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.open_cart()

    item_name = inventory_page.get_cart_item_name()

    assert item_name == "Sauce Labs Backpack"