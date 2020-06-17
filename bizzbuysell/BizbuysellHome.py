from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get("https://www.bizbuysell.com/")
#page = BeautifulSoup(driver.page_source,"html.parser")
select = Select(driver.find_element_by_id('ddlStates'))
options = select.options

for option in options:
    print(option.text)


driver.close()
