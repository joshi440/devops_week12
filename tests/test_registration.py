
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


# Base URL of the Flask registration application
URL = "http://127.0.0.1:5000/"


# Setup and close the browser for each test
@pytest.fixture
def driver():
    options = Options()

    # Run Chrome without opening a visible browser window
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())

    browser = webdriver.Chrome(
        service=service,
        options=options
    )

    try:
        yield browser
    finally:
        browser.quit()


# Test 1: Student name is empty
def test_empty_student_name(driver):
    driver.get(URL)

    driver.find_element(
        By.NAME, "roll_number"
    ).send_keys("23251A1241")

    driver.find_element(
        By.TAG_NAME, "button"
    ).click()

    name = driver.find_element(
        By.NAME, "student_name"
    )

    assert name.get_attribute("required") is not None
    assert name.get_property("validity")["valueMissing"] is True


# Test 2: Roll number is empty
def test_empty_roll_number(driver):
    driver.get(URL)

    driver.find_element(
        By.NAME, "student_name"
    ).send_keys("Joshitha")

    driver.find_element(
        By.TAG_NAME, "button"
    ).click()

    roll = driver.find_element(
        By.NAME, "roll_number"
    )

    assert roll.get_attribute("required") is not None
    assert roll.get_property("validity")["valueMissing"] is True


# Test 3: Both fields are empty
def test_both_fields_empty(driver):
    driver.get(URL)

    driver.find_element(
        By.TAG_NAME, "button"
    ).click()

    name = driver.find_element(
        By.NAME, "student_name"
    )

    roll = driver.find_element(
        By.NAME, "roll_number"
    )

    assert name.get_property("validity")["valueMissing"] is True
    assert roll.get_property("validity")["valueMissing"] is True


# Test 4: Valid student registration
def test_valid_registration(driver):
    driver.get(URL)

    driver.find_element(
        By.NAME, "student_name"
    ).send_keys("Joshitha")

    driver.find_element(
        By.NAME, "roll_number"
    ).send_keys("23251A1241")

    driver.find_element(
        By.TAG_NAME, "button"
    ).click()

    assert "Registration Successful!" in driver.page_source
    assert "Joshitha" in driver.page_source
    assert "23251A1241" in driver.page_source
