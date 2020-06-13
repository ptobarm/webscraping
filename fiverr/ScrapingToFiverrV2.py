from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import pandas as pd

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('headless')
#browser =  webdriver.Chrome(chrome_options=chrome_options)
#warnings.filterwarnings('ignore')

browser = webdriver.Chrome()
browser.get("https://www.fiverr.com")

text_input = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/form/input")
text_input.send_keys("Voice Over")

sleep(randint(2,5))

search_button = browser.find_element_by_xpath("//*[@id='perseus-app']/div/div[1]/div/div[2]/div[1]/div[1]/form/button")
search_button.submit()

dataframe = pd.DataFrame(columns=["Title", "Description", "Rate", "Pricing"])

page = BeautifulSoup(browser.page_source,"html.parser")



tags = page.select('.gig-card-layout')
print('Tamaño Arreglo: ', len(tags))
for tag in tags:
    #Title
    #print("Title: " + tag.find('span',class_='seller-name').a.getText())
    title = tag.find('span',class_='seller-name').a.getText()
    #description
    #print("Description: " + tag.div.div.h3.a.getText())
    description = tag.div.div.h3.a.getText()
    #Rate
    if tag.find('span', class_ = 'gig-rating') is not None:
    #print("Rate: " + tag.find('span',class_='gig-rating text-body-2').getText())
        rate = tag.find('span',class_='gig-rating text-body-2').getText()
    else:
        #print("Rate: ")
        rate = ''
    #pricing
    #print("Pricing: " + tag.div.div.footer.a.getText())
    pricing = tag.div.div.footer.a.getText()

    dataframe = dataframe.append({'Title': title, 'Description': description, 'Rate': rate, 'Pricing': pricing}, ignore_index=True)


dataframe.to_csv("fiverr.csv", index=False)

#summ = browser.select('.pagination-arrows')
#summ.a.click()

print("********************")


#pagination-arrows
#nav = browser.find_element_by_id("mainnav")
