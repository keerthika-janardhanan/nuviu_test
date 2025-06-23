import time
import json
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from config.ios_cap import get_ios_capabilities
from pages.country_selection import CountrySelection
from pages.email_login import Login
from pages.home_page import HomePage
from test.common_util import scroll_until_visible

web_page = "https://my.vuse.com/dashboard#device"


def switch_to_webview(driver):
    """Switch to the first available WEBVIEW context."""
    contexts = driver.contexts
    print("Available contexts:", contexts)

    for context in contexts:
        if 'WEBVIEW' in context:
            driver.switch_to.context(context)
            break


def main():
    options = get_ios_capabilities(cloud_options={"someCloudKey": "someCloudValue"})
    driver = webdriver.Remote("http://localhost:4723", options=options)

    # try:
    switch_to_webview(driver)

    wait = WebDriverWait(driver, 10)

    try:
        # Attempt to find the search bar
        search_bar = driver.find_element(AppiumBy.CLASS_NAME, CountrySelection.SEARCH_BAR)

        # If found, send text
        search_bar.send_keys(web_page)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Go").click()

    except NoSuchElementException:
        # print("Search bar has existing content:", search_value)
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="toolbar_open_tabs_icon"]'))).click()
        wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="closeIcon"]'))).click()
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="tabsSettingsIcon"]'))).click()
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH,
                                                   '//XCUIElementTypeStaticText[@name="Privacy Controls"]'))).click()
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//XCUIElementTypeButton[@name="CLEAR WEBSITE DATA"]'))).click()
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//XCUIElementTypeButton[@name="CLEAR WEBSITE DATA"]'))).click()
        wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="back_button"]'))).click()
        wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//XCUIElementTypeButton[@name="menu-close-x"]'))).click()
        wait.until(EC.presence_of_element_located(
            (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="add_tab_btn_bkg"]'))).click()
        wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, CountrySelection.SEARCH_BAR))).send_keys(web_page)
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Go").click()


    # Select Canada
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, CountrySelection.COUNTRY_SELECTION))).click()

    # Enter Postal Code
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, CountrySelection.POSTAL_CODE))).send_keys("S0P 0A0")

    wait.until(EC.element_to_be_clickable(
        (AppiumBy.ACCESSIBILITY_ID, "Done"))).click()

    # Confirm location
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, CountrySelection.CONFIRMATION_BUTTON))).click()

    time.sleep(1)

    # age confirmation
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, Login.AGE_CONFIRMATION))).click()

    #login page
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, Login.LOGIN_ENTER))).click()

    #enter creds
    wait.until(EC.element_to_be_clickable(
        (AppiumBy.XPATH, Login.USER_EMAIL))).send_keys("sarath.nagarajan@cognizant.com")
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,Login.PASSWORD))).send_keys("Testvuse-1")
    wait.until(EC.element_to_be_clickable( (AppiumBy.ACCESSIBILITY_ID, "Done"))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.LOGIN))).click()

    #pin code confirmation
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.PIN1))).send_keys("3")
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.PIN1))).send_keys("7")
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.PIN1))).send_keys("9")
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.PIN1))).send_keys("7")
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Done"))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.CONFIRM_PIN))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.CONTINUE))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Login.NEXT_PAGE))).click()

    #Homepage navigation
    wait.until(EC.element_to_be_clickable((AppiumBy.NAME, HomePage.VUSEWORLD))).click()
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, HomePage.FIRST_DEVICE))).click()
    time.sleep(1)
    driver.execute_script("mobile: swipe", {"direction": "up"})

    slide_xpath_template = '//XCUIElementTypeButton[@name="{} of 7"]'

    for i in range(1, 8):
        # Find slide button
        slide_element = driver.find_element(AppiumBy.XPATH, slide_xpath_template.format(i))

        # Get element's center coordinates
        rect = slide_element.rect
        x = rect['x'] + rect['width'] // 2
        y = rect['y'] + rect['height'] // 2

        # Tap using coordinates
        driver.execute_script("mobile: tap", {"x": x, "y": y})
        print(f"Tapped on slide {i}")
        time.sleep(1)
    driver.execute_script("mobile: swipe", {
        "direction": "down"
    })
    element = driver.find_element(AppiumBy.XPATH, HomePage.CLOSE_DEVICE)

    # Step 2: Get the element's center coordinates
    rect = element.rect
    x = rect['x'] + rect['width'] // 2
    y = rect['y'] + rect['height'] // 2

    # Step 3: Tap using coordinates
    driver.execute_script("mobile: tap", {"x": x, "y": y})
    time.sleep(1)
    # wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,HomePage.CLOSE_DEVICE))).click()
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, HomePage.MORE_PAGE))).click()
    # wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, HomePage.ACCOUNT_DETAILS))).click()
    time.sleep(1)
    driver.execute_script("mobile: swipe", {
        "direction": "up"
    })
    time.sleep(1)
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, HomePage.DEVICE_DETAILS))).click()
    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    main()
