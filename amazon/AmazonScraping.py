from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd


driver = webdriver.Chrome()
#pages = [str(i) for i in range(1,5)]

driver.get("https://www.amazon.com/-/es/")

text_input = driver.find_element_by_id("twotabsearchtextbox")
text_input.send_keys("Shimano")

search_button = driver.find_element_by_class_name("nav-input")
search_button.click()

page = BeautifulSoup(driver.page_source,"html.parser")
