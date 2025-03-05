
#Various Imports for selenium and webdriver functionalities

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import time
import random







# Set Path to the chromedriver executable
driverpath = r"chromedriver.exe"



# Set Path to the log file
log_path = "chromedriver.exe"
# Set Chrome options if needed
options = Options()



import os
import stat

# Ensure the file exists
if os.path.exists(driverpath):
    # Add executable permissions
    st = os.stat(driverpath)
    os.chmod(driverpath, st.st_mode | stat.S_IEXEC)
else:
    print(f"Error: {driverpath} does not exist.")



user_agents = [
    # Add your list of user agents here
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
]

useragent = random.choice(user_agents)
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options.add_argument('--headless')
options.add_argument('--disable-gpu')  # May improve stability in headless mode
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--no-sandbox')  # Sometimes helps with stability
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f'user-agent={useragent}')
options.add_argument("--disable-gpu")
options.add_argument("--disable-software-rasterizer")
options.add_argument("--disable-webgl")

# Suppress logs from Chrome
options.add_argument("--log-level=3")  # 0 = INFO, 1 = WARNING, 2 = ERROR, 3 = FATAL

# Suppress DevTools & other logs
# Create the service with logging
service = Service(executable_path=driverpath, log_path=log_path)

web1 = "https://www.scrapethissite.com/pages/simple/"

