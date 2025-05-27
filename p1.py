from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
    # Open Google
driver.get("https://client.wvd.microsoft.com/arm/webclient/index.html")
time.sleep(200)
# Find search bar and search for a keyword
