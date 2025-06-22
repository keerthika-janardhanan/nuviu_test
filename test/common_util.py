import time
from selenium.webdriver.support import expected_conditions as EC

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage

def scroll_until_visible(driver, max_swipes=5):
    slides = driver.find_elements(AppiumBy.IOS_CLASS_CHAIN, '//XCUIElementTypeOther[@name="MYVUSE"]/XCUIElementTypeOther[10]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeLink')
    slide_count = len(slides)
    print(f"Slide count: {slide_count}")

    # Swipe left for each slide
    for i in range(slide_count - 1):
        driver.execute_script("mobile: swipe", {"direction": "left"})
        time.sleep(1)