from appium.options.ios import XCUITestOptions

def get_ios_capabilities(cloud_options=None):
    options = XCUITestOptions()

    options.set_capability("platformName", "iOS")
    options.set_capability("platformVersion", "18.5")
    options.set_capability("deviceName", "iPhone")
    options.set_capability("automationName", "XCUITest")
    options.set_capability("udid", "00008020-000B79E90223002E")
    options.set_capability("bundleId", "com.nuviu")
    options.set_capability("xcodeOrgId", "4VCBUA2A64")
    options.set_capability("xcodeSigningId", "Apple Developer")
    options.set_capability("updatedWDABundleId", "com.vuse.testApp")
    options.set_capability("noReset", False)

    if cloud_options:
        options.set_capability("cloud:options", cloud_options)

    return options