from appium.webdriver.webdriver import WebDriver
import inspect

print("WebDriver module:", WebDriver.__module__)
print("WebDriver init signature:\n", inspect.signature(WebDriver.__init__))
