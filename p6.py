import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_driver_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
chrome_options = Options()
chrome_options.binary_location = chrome_driver_path
chrome_options.add_argument(r"--user-data-dir=C:\Users\MagnusMinds\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("profile-directory=Profile 1")  # Use your correct profile

# Use actual ChromeDriver path, not browser binary
chrome_driver_executable_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Update this to the actual path

# Start Chrome with custom profile
print("Launching Chrome with user profile...")
service = Service(executable_path=chrome_driver_executable_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open first tab
driver.get("https://www.google.com")
time.sleep(3)

# Open second tab
driver.execute_script("window.open('https://www.bing.com', '_blank');")
time.sleep(3)

# Loop to switch tabs every 10 minutes
try:
    while True:
        print("Switching to tab 1...")
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(6)  # 10 minutes

        print("Switching to tab 2...")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(6)  # 10 minutes
except  :
    print("Stopping automation.")
    driver.quit()
