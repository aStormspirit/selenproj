from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

host = 'localhost'
capabilities = {
    "browserName": "firefox",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}

with webdriver.Remote(command_executor=f'http://{host}:4444/wd/hub', desired_capabilities=capabilities) as driver:
    # Open URL
    driver.get("https://seleniumhq.github.io")

    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
    original_window = driver.current_window_handle

    # Check we don't have other windows open already
    assert len(driver.window_handles) == 1

    # Click the link which opens in a new window
    #driver.find_element(By.LINK_TEXT, "new window").click()

    # Wait for the new window or tab
    wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    # Wait for the new tab to finish loading content
    wait.until(EC.title_is("SeleniumHQ Browser Automation"))
  