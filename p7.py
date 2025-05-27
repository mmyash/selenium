from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

# --- Configuration for your Chrome Profile (IMPORTANT: UPDATE THESE!) ---
# 1. user_data_dir: This is the path to the 'User Data' folder.
#    Find this by going to chrome://version/ in your Chrome browser and looking at "Profile Path".
#    It's the part of the path *before* the specific profile folder (e.g., "Default", "Profile 1").
#    Example: r"C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
#    Use 'r' before the string for a raw string to handle backslashes correctly in Windows paths.
user_data_dir = r"C:\Users\MagnusMinds\AppData\Local\Google\Chrome\User Data" # <<< DOUBLE-CHECK AND REPLACE THIS with YOUR User Data path

# 2. profile_directory_name: This is the name of the specific profile folder inside 'User Data'.
#    This is the *last* part of the "Profile Path" from chrome://version/.
#    Common names are "Default", "Profile 1", "Profile 2", etc.
profile_directory_name = "Default" # <<< DOUBLE-CHECK AND REPLACE THIS with YOUR Profile Directory Name (e.g., "Default", "Profile 1")

# --- Selenium Setup ---
options = Options()

# Add the arguments to load your existing profile
# This tells Chrome to use the specified user data directory and profile.
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument(f"--profile-directory={profile_directory_name}")

# Optional: Add other arguments as needed
# options.add_argument("--headless") # Uncomment to run Chrome in headless mode (no visible UI)
options.add_argument("--start-maximized") # Start the browser window maximized

# Initialize the Chrome WebDriver
# ChromeDriverManager automatically downloads the correct ChromeDriver executable for your Chrome version.
try:
    print("Initializing Chrome WebDriver...")
    # Attempt to install and get the ChromeDriver service
    service = Service(ChromeDriverManager().install())
    
    # Create the WebDriver instance
    driver = webdriver.Chrome(service=service, options=options)
    print(f"Successfully opened Chrome with profile: '{profile_directory_name}' from '{user_data_dir}'")

    # --- Automate your task here ---
    # Example: Navigate to a website
    print("Navigating to example.com...")
    driver.get("https://www.example.com")
    print(f"Current URL: {driver.current_url}")

    # You can now interact with elements, navigate to other pages, etc.
    # For example, to find an element by its ID and print its text:
    # try:
    #     element = driver.find_element(By.ID, "some_element_id") # Example using By.ID
    #     print(f"Text of element: {element.text}")
    # except Exception as e:
    #     print(f"Could not find element: {e}")

    # Example: Keep the browser open for a few seconds to observe
    print("Keeping browser open for 10 seconds...")
    time.sleep(10)

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("\n--- CRITICAL TROUBLESHOOTING STEPS ---")
    print("1. **CLOSE ALL CHROME WINDOWS AND PROCESSES:**")
    print("   Open Task Manager (Ctrl+Shift+Esc), go to 'Processes', and end ALL 'Google Chrome' or 'chrome.exe' tasks.")
    print("   This is the most common reason for 'DevToolsActivePort file doesn't exist'.")
    print("2. **DOUBLE-CHECK PROFILE PATHS:**")
    print("   Go to `chrome://version/` in a fresh Chrome browser.")
    print("   Carefully verify `user_data_dir` and `profile_directory_name` in the script against 'Profile Path'.")
    print("   Ensure they are EXACTLY correct, including capitalization and backslashes (use 'r' prefix for paths).")
    print("3. **CONSIDER A NEW PROFILE (Diagnostic):**")
    print("   If issues persist, try creating a brand new Chrome profile (Chrome Settings -> You and Google -> Manage profiles -> Add).")
    print("   Then, find the paths for this *new* profile and use them in the script. If it works, your original profile might be corrupted.")
    print("4. **UPDATE SELENIUM & WEBDRIVER-MANAGER:**")
    print("   Run `pip install --upgrade selenium webdriver-manager` in your terminal to ensure you have the latest versions.")
    print("   This helps with driver compatibility issues.")

finally:
    # Always ensure the browser is closed, even if an error occurs
    if 'driver' in locals() and driver:
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")