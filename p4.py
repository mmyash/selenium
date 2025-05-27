import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
 
chrome_driver_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options = Options()
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options.add_argument(r"C:\Users\MagnusMinds\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument(r"profile-directory=Profile 7")  # Change this to your actual profile name
print("hii")
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
print(1)
time.sleep(5)
print(2)
driver.get("https://www.google.com")
 
time.sleep(5)
driver.quit()