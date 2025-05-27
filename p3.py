import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
# Specify the path of ChromeDriver
chrome_driver_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'  # Correct chromedriver.exe path
 
# Set Chrome Options for User Profile
chrome_options = Options()
#chrome_options.add_argument("user-data-dir=C:/Users/MagnusMinds/AppData/Local/Google/Chrome/User Data/Profile 8")
#chrome_options.add_argument("--profile-directory=Profile 8")  # Profile name
 
# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.google.com")
time.sleep(15)  # Let the user see something
 
driver.quit()