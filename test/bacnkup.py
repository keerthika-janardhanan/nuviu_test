import time
import json
from appium import webdriver
from appium.options.ios import XCUITestOptions  # or use UiAutomator2Options for Android
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


options = XCUITestOptions()

options.set_capability("platformName", "iOS")
options.set_capability("platformVersion", "18.5")
options.set_capability("deviceName", "iPhone")  # Can be any name, doesn't have to match UDID
options.set_capability("automationName", "XCUITest")
options.set_capability("udid", "00008020-000B79E90223002E")
options.set_capability("bundleId", "com.nuviu")
options.set_capability("xcodeOrgId", "4VCBUA2A64")
options.set_capability("xcodeSigningId", "Apple Developer")
options.set_capability("updatedWDABundleId", "com.vuse.testApp")
# options.set_capability("useNewWDA", True)
options.set_capability("noReset", False)

options.set_capability('cloud:options', cloud_options)


def load_caps_from_json(path='config/capability.json'):
    with open(path) as f:
        raw_caps = json.load(f)

    options = XCUITestOptions()
    for key, value in raw_caps.items():
        options.set_capability(key, value)

    return options
driver = webdriver.Remote("http://localhost:4723", options=options)

#clear all cookies
# Wait for webview to load
time.sleep(2)
# Check available contexts
contexts = driver.contexts
print("Available contexts:", contexts)

# Switch to webview context
for context in contexts:
    if 'WEBVIEW' in context:
        driver.switch_to.context(context)
        break

# Now interact with web content

wait = WebDriverWait(driver, 2)

element = wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'XCUIElementTypeTextField')))
element.send_keys("https://my.vuse.com/dashboard#device")
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Go").click()

canada_button = wait.until(EC.element_to_be_clickable(
    (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Canada Canada"]')
))
canada_button.click()
time.sleep(2)
postal_code = wait.until(EC.element_to_be_clickable(
    (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="POSTAL CODE"]')
))
postal_code.send_keys("S0P 0A0")
done_key = wait.until(EC.element_to_be_clickable(
    (AppiumBy.ACCESSIBILITY_ID, "Done")
))
done_key.click()
time.sleep(2)
confirm = wait.until(EC.element_to_be_clickable(
    (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name, "CONFIRM")]')
))
confirm.click()
time.sleep(2)
