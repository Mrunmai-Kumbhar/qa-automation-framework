import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce")
])
def test_login(driver, username, password):

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert "inventory" in driver.current_url