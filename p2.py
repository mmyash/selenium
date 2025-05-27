# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time

# options = webdriver.ChromeOptions()
# options.add_argument(r"--user-data-dir=C:\Users\MagnusMinds\AppData\Local\Google\Chrome\User Data\Profile 8") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
# options.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.in")
# time.sleep(50)

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time


# options = webdriver.ChromeOptions()
# print(1)
# options.add_argument("C:\\Users\MagnusMinds\AppData\Local\Google\Chrome\User Data") #leave out the profile
# print(2)
# options.add_argument("profile-directory=Profile 8") #enter profile here
# print(3)
# driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chrome.exe", chrome_options=options)
# print(4)
# driver.get("https:www.google.com")
# time.sleep(20)

import time

from selenium import webdriver
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chrome.exe')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

time.sleep(5) # Let the user actually see something!