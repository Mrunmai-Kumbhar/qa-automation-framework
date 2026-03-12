from selenium.webdriver.common.by import By


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    add_backpack_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_item = (By.CLASS_NAME, "inventory_item_name")

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_backpack_button).click()

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_item_name(self):
        return self.driver.find_element(*self.cart_item).text