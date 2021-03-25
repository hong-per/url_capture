#!/bin/bash

from Screenshot import Screenshot_Clipping
from selenium import webdriver 
from time import sleep 
from datetime import datetime
from selenium.common.exceptions import TimeoutException
import os

options = webdriver.FirefoxOptions()
options.add_argument('--no-sandbox')
options.headless = True 
browser = webdriver.Firefox(executable_path="/home/geckodriver", options=options)
ob=Screenshot_Clipping.Screenshot()


now = datetime.now()
year = now.year
month = now.month
day = now.day

year_path = f"/var/www/html/capture/{year}"
month_path = f"/var/www/html/capture/{year}/{month}"
day_path = f"/var/www/html/capture/{year}/{month}/{day}"

url_list = []


def today_folder():

    if not os.path.isdir(year_path):
        os.mkdir(year_path)
    if not os.path.isdir(month_path):
        os.mkdir(month_path)
    if not os.path.isdir(day_path):
        os.mkdir(day_path)

        
def capture(url_list):

    for url in url_list:
        
        browser.implicitly_wait(10)
        browser.get(url) 
        browser.maximize_window()
        screenshot_name = url[8:].replace("/", ".")

        ob.full_Screenshot(browser, save_path=f"{day_path}", image_name=f"{screenshot_name}.png")

        # or
        # S = lambda X: browser.execute_script("return document.body.parentNode.scroll"+X) 
        # browser.set_window_size(S("Width"), S("Height")) 
        # browser.find_element_by_tag_name("body")
        # browser.save_screenshot(f"{day_path}/{screenshot_name}.png")


if __name__ == "__main__":
    today_folder()
    capture(url_list)


browser.quit()
