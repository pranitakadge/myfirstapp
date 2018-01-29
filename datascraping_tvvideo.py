from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd

wd = webdriver.Chrome(executable_path="C:\\Users\\User\Downloads\chromedriver_win32\chromedriver.exe")
wd.get("http://www.tvguide.com/listings/")
html_page = wd.page_source
wd.quit()
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_page,'html.parser')
# print(html_page)
listing = soup.find(id="listings")
period_tags = listing.find_all("span",class_="listings-channel-name listings-channel-name-only")
periods = [p.get_text() for p in period_tags]
# print(listing[0])
print(periods)
programs = listing.find_all("span", class_="listings-program-title")
programs_all = [pt.get_text() for pt in programs]
print(programs_all)
time = listing.find_all("span", class_="listings-program-time")
time_all = [t.get_text() for t in time]
print(time_all)


# channel = pd.DataFrame({
#         "period": periods,
#         "short_desc": programs_all,
#         "temp": time_all,
#
#     })
# print(channel)
