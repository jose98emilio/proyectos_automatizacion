from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
    def is_username_field_present(self):
        return self.driver.find_element(By.ID, "user-name").is_displayed()

    def is_password_field_present(self):
        return self.driver.find_element(By.ID, "password").is_displayed()

    def is_login_button_present(self):
        return self.driver.find_element(By.ID, "login-button").is_displayed()

    def is_inventory_page_loaded(self):
        return "inventory" in self.driver.current_url

    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "//div[@class='error-message-container error']/h3").text 

    def get_username_field_value(self):
        return self.driver.find_element(By.ID, "user-name").get_attribute("value")