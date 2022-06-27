from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


# Write code here
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver")
browser.get(START_URL)

headers = ["name", "distance", "mass", "radius"]
stars_data = []


time.sleep(10)

def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")

    table = soup.find_all('table')[8] # Get the fourth table

    for tr_tags in table.find_all("tr"):
        td_tags = tr_tags.find_all("td")
        temp_list = []

        for index, td_tag in enumerate(td_tags):
            if index == 0:
                try:
                    temp_list.append(td_tag.find("a").string)
                except:
                    temp_list.append(td_tag.string)
            elif index in [5, 8, 9]:
                try:
                    temp_list.append(td_tag.contents[0].strip())
                except:
                    temp_list.append("")
        
        stars_data.append(temp_list)
    
    # Create CSV file
    with open("scraper.csv", "w") as f:
        writer = csv.writer(f)

        writer.writerow(headers)
        writer.writerows(stars_data)
    
scrape()