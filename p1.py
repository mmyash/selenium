
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Close any running Edge instances
os.system("taskkill /f /im msedge.exe >nul 2>&1")
time.sleep(2)  # Wait for processes to terminate

# Set Edge user data directory and profile
user_data_dir = r"C:\Users\MagnusMinds\AppData\Local\Microsoft\Edge\User Data"  # Edge user data directory
profile_directory = "Default"

options = Options()
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory}")

max_retries = 3
for attempt in range(max_retries):
    try:
        print(f"Attempt {attempt + 1}: Launching Edge with custom profile...")
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

        print("Opening YouTube...")
        driver.get("https://www.youtube.com")
        
        # Wait for the search bar to be visible and interactable
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_query"))
        )
        
        print("Searching for 'selenium playlist'...")
        search_box.send_keys("selenium playlist")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results and click the first video
        first_video = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ytd-video-renderer #video-title"))
        )
        first_video.click()

        # Wait for the video player to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "video"))
        )

        # Open settings menu and set playback speed to 2x
        print("Setting playback speed to 2x...")
        settings_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".ytp-settings-button"))
        )
        settings_button.click()

        # Select Playback speed option
        playback_speed_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ytp-menuitem') and .//div[text()='Playback speed']]"))
        )
        playback_speed_option.click()

        # Select 2x speed
        speed_2x = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ytp-menuitem') and .//div[text()='2']]"))
        )
        speed_2x.click()

        print("Playing video at 2x speed...")
        time.sleep(10)  # Keep the video playing for 10 seconds
        break  # Exit loop if successful

    except Exception as e:
        print(f"❌ Error on attempt {attempt + 1}: {e}")
        if attempt < max_retries - 1:
            print("Retrying...")
            time.sleep(2)
        else:
            print("✔ Make sure all Edge windows are fully closed and profile is not locked.")

    finally:
        if 'driver' in locals():
            print("Closing browser...")
            driver.quit()
