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
pages = [str(i) for i in range(1,5)]
dataframe = pd.DataFrame(columns=["Title", "Description", "Rate", "Pricing"])

for page in pages:
    browser.get("https://www.fiverr.com/categories/music-audio/voice-overs?source=hplo_search_tag&pos=1&name=voice-overs&page=" + page)
    #https://www.fiverr.com/categories/music-audio/voice-overs?source=hplo_search_tag&pos=1&name=voice-overs&page=2
    #https://www.fiverr.com/categories/music-audio/voice-overs?source=hplo_search_tag&pos=1&name=voice-overs&page=3
    #browser.get("https://www.fiverr.com/?show_join=true&utm_source=105990&utm_medium=cx_affiliate&utm_campaign=&cxd_token=105990_4417711&show_join=true")

    print('Page: ' + page)

    # Pause the loop
    sleep(randint(8,15))

    page = BeautifulSoup(browser.page_source,"html5lib")

    #print(page)

    #browser.get_cookies()

    #page.find('input')['value'] = 'Voice Over'
    #text_input = page.findAll('input')

    #text_input = page.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/form/input")
    #text_input = page.find_element_by_class_name("js-search-input")
    #text_input.send_keys("Voice Over")

    #search_button = page.find_element_by_class_name("btn-submit")
    #search_button = page.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/form/button")
    #search_button.click()

    #/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/form/input
    #/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/form/input
    #
    #/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[1]/form/button
    #/html/body/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/form/button


    #Title, image & videos, description, pricing, categories.


    #print(page)


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
    #tags = page.select('.seller-name')
    #for tag in tags:
    #    print(tag.a.getText())

    #summ = page.select('.pagination-arrows')
    #summ.a.click()

print("********************")






#pagination-arrows
#nav = browser.find_element_by_id("mainnav")
