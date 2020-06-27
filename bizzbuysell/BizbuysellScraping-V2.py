import requests
import pandas as pd
from bs4 import BeautifulSoup
from math import ceil

print('**** INICIO ****')


a = [['Alabama','https://www.bizbuysell.com/alabama-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['Alaska','https://www.bizbuysell.com/alaska-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['Arizona','https://www.bizbuysell.com/arizona-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['Arkansas','https://www.bizbuysell.com/arkansas-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['California','https://www.bizbuysell.com/california-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['Colorado','https://www.bizbuysell.com/colorado-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'],
     ['Connecticut','https://www.bizbuysell.com/connecticut-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x']]


#a = [['California','https://www.bizbuysell.com/california-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x']]
#url = 'https://www.bizbuysell.com/alabama-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x'

dataframe = pd.DataFrame(columns=["US-State","Title", "URL"])

def getSoup(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers = headers)
    return BeautifulSoup(page.content,'html.parser')


def getCompanies(p_soup, p_datafr,p_state):
    companies = p_soup.findAll('a',class_=['listingResult','result','featured','indexed'])
    for companie in companies:
        urlCompanie = 'https://www.bizbuysell.com/' + companie.get('href')
        title = companie.get('title')
        #print('url: ' + url + ' Title: ' + title)
        p_datafr = p_datafr.append({'US-State': p_state,'Title': title, 'URL': urlCompanie}, ignore_index=True)
    return p_datafr

#Get the next URL
def findNextUrl(p_soup):
    next = p_soup.find('a',class_='bbsPager_next')
    nextUrl = next.get('href')
    print(nextUrl)
    return nextUrl


for link in a:
    #print(link)
    #print(link[0])
    #print(link[1])
    state = link[0]
    url = link[1]

    soup = getSoup(url)


    #Geto total Results (only once)
    divResult = soup.find('div',id='resultDiv')
    results = divResult.div.span.getText()
    valor = results.split()
    #val = ceil(int(valor[0])/50)
    #print(len(valor[0].split('+')))
    if len(valor[0].split('+')) > 1:
        val = ceil(int(valor[0].split('+')[0])/50)
    else:
        val = ceil(int(valor[0])/50)
    print('val: ' + str(val))

    urlNext = findNextUrl(soup)

    for i in range(val):
        if i == 0:
            dataframe = getCompanies(soup,dataframe,state)
            dataframe.append(dataframe)
        else:
            soup = getSoup(urlNext)
            urlNext = findNextUrl(soup)
            dataframe = getCompanies(soup,dataframe,state)
            dataframe.append(dataframe)

dataframe.to_csv("bizzbuysell/bizbuysell.csv",mode='a', index=False,header=False)

print('**** FIN ****')
