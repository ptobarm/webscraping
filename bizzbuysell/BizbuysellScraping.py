from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
pages = [str(i) for i in range(1,23)]

#Alabama
#driver.get("https://www.bizbuysell.com/alabama-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#Alaska
#driver.get("https://www.bizbuysell.com/alaska-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#Arizona
#driver.get("https://www.bizbuysell.com/arizona-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#Arkansas
#driver.get("https://www.bizbuysell.com/arkansas-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#California
#driver.get("https://www.bizbuysell.com/california-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#driver.get("https://www.bizbuysell.com/california-businesses-for-sale/28/?q=aXI9MSZsc3JfcmxicG49MzAmc3BpZD0xJnc9cQ%3d%3d")
#Colorado
driver.get("https://www.bizbuysell.com/colorado-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#Connecticut
#driver.get("https://www.bizbuysell.com/connecticut-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
#Vermont
#driver.get("https://www.bizbuysell.com/vermont-businesses-for-sale/?q=aXI9MSZzcGlkPTEmdz1x")
dataframe = pd.DataFrame(columns=["US-State","Title", "URL"])


for page in pages:
    try:
        wait = WebDriverWait(driver, 30)

        #resultRowContainer_beforeAd1
        containers = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "listingResult")))
        #containers = driver.find_elements_by_class_name('listingResult')
        for container in containers:
            url = container.get_attribute("href")
            title = container.get_attribute("title")
            dataframe = dataframe.append({'US-State': 'Colorado','Title': title, 'URL': url}, ignore_index=True)

        nextPageButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "bbsPager_next")))
        ref = nextPageButton.get_attribute("href")
        if ref != 'javascript:void(0);':
            nextPageButton.click()
    finally:
        dataframe.to_csv("bizbuysell.csv",mode='a', index=False,header=False)
        #driver.quit()

driver.close()
