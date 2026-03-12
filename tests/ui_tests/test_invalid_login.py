from pages.login_page import LoginPage


def test_invalid_login(driver):

    driver.get("https://www.saucedemo.com")

    login_page = LoginPage(driver)

    login_page.enter_username("wrong_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    error_text = login_page.get_error_message()

    assert "Epic sadface" in error_text