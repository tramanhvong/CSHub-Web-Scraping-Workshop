import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import *
from typing import *



driver = webdriver.Chrome(service=service, options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )






def example1():
    driver.get("")
    countries = driver.find_elements(,"")
    if():
        print("Succesfully found countries!")

    else:
        print("Elements not found.")

    return countries
    

scrapedCountries: List["HTML_TAGS"] = example1()

print(scrapedCountries)


input("Press Enter to exit...")