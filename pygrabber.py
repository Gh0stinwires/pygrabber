import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

# Read URLs from a text file
file_path = 'urls.txt'  # Path to the text file containing URLs

with open(file_path, 'r') as file:
    website_urls = [line.strip() for line in file if line.strip()]

# Find the path to the chromedriver executable
chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

# Set up the Chrome options and service
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # Optional: Add additional Chrome options if needed
service = Service(chromedriver_path)

# Set up the Selenium web driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Loop through each URL and take a screenshot
for url in website_urls:
    try:
        # Prepend 'https://' if it's not already present
        if not url.startswith('https://'):
            url = 'https://' + url

        # Navigate to the URL
        driver.get(url)

        # Take a screenshot
        driver.save_screenshot(f'{url.replace("https://", "")}.png')

    except WebDriverException as e:
        if 'ERR_CONNECTION_TIMED_OUT' in str(e):
            print(f"Skipping URL: {url} due to connection timeout error")
            continue
        else:
            print(f"Error occurred while capturing screenshot for {url}: {str(e)}")

# Quit the web driver
driver.quit()
