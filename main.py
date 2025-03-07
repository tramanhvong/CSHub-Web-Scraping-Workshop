import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
from typing import *
from bs4 import BeautifulSoup
import csv


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )



def example1bs4():

    soup = BeautifulSoup(requests.get("https://www.scrapethissite.com/pages/simple/").content, "html.parser")
    countries = soup.findAll("div", class_="country")
    if(countries):
        print("Succesfully found countries")


  


    sorted_countries_by_area = sorted(countries, key=lambda country: float(country.find(class_="country-area").get_text(strip = True)))


    for country in sorted_countries_by_area:
        name = country.find(class_="country-name")
        area = country.find(class_="country-area")
        print(f"{name}: {area}")




def example1selenium():
    driver.get("")
    countries = driver.find_elements(...,"")
    if(...):
        print("Succesfully found countries!")

    else:
        print("Elements not found.")


    sorted_countries_by_area = sorted(countries, key=lambda country: float(country.find_element(By.CLASS_NAME, ...).text.replace(',', '')))

    for country in sorted_countries_by_area:
        name = ...
        area = ...
        print(f"{name}: {area}")


def example2selenium():

    driver.get("")
    myTable = driver.find_element(..., "")

    # Extract rows
    rows = myTable.find_elements(..., "")
    headers = myTable.find_elements(..., "")

    # Extract header row
    header_row = []


    if headers:
        for header in headers:
            header_row.append(header.text.strip())

    # Extract table data
    table_data = []


    for row in rows:
        cells = row.find_elements(..., "")  # Use "th" for headers
        row_data = []
        for cell in cells:
            row_data.append(...)
        
        if row_data:  # Remove empty rows
            table_data.append(row_data)

    # Print headers
    print(header_row)

    # Print table data
    for row in table_data:
        for cell in row:
            print(row)

    # Save data to CSV
    with open("scraped_table.csv", "w", newline="", encoding="utf-8") as file:
        
        writer = csv.writer(file)

        # Write headers if present
        if header_row:
            writer.writerow(header_row)

        # Write data
        for row in table_data:
            writer.writerow(row)

    print("CSV file saved!")


def example2bs4():
    url = "https://www.nba.com/players"
    response = requests.get(url)
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the table
    my_table = soup.find('table', class_='players-list') # tag, class_ = className

    print(type(my_table))

    # Extract headers (if any)
    headers = my_table.find_all('th')

    header_row = []

    if(headers):
        for header in headers:
            header_row.append(header)

    # Extract table rows
    rows = my_table.find_all("tr")
    
    # Process the table data
    table_data = []
    for row in rows:
        cells = row.find_all("cell")
        cells_text = []

        for cell in cells:
            cells_text.append(cell)


        table_data.append(cells_text)

    row_data = []
    
    for cell in cells:
        row_data.append(cell)
    
    if row_data:  # Ensure the row is not empty
        table_data.append(row_data)

    for row in table_data:
        if row == []:
            table_data.remove(row)

    # Print header and data
    print(header_row)
    for i in table_data:
        print(i)
    
    # Save to CSV
    with open("./nba_players.csv", "r", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write headers if present
        if header_row:
            writer.writerow(header_row)

        # Write data
        writer.writerows(table_data)

    print("CSV file saved!")


    

def playerLookup():
    playertofind = input("Enter the name of a NBA player currently playing:")
    driver.get("https://www.nba.com/players")



    #To avoid some unnecesary element from popping up
    driver.refresh()
    driver.refresh()
    driver.refresh()
    driver.refresh()    

'''
   Hints to get you started:

   Not only can selenium dynamically scrape/crawl websites but it can also interact with the browser.

   Use .click() on an element to click it.
   for example, if you lets say scrape a button called searchButton: searchButton.click()

   You can also send keystrokes into a form/input field, so for example if we found an element named textBox: textBox.sendkeys("Your String") would send the string into the textbox.
   
   
   
   '''
example2bs4()

driver.get("https://www.google.com")


input("Press Enter to exit...")
