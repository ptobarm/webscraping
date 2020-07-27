from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
driver =  webdriver.Chrome(chrome_options=chrome_options)
'''

driver = webdriver.Chrome()


#Se defina dataframe con su cabecera
dataframe = pd.DataFrame(columns=["Usuario", "Apertura", "Ciere", "Total_Abonos","Total_Gastos","Saldo_Cierre","Id"])


url = 'https://clinicadentalfa.dentalink.cl/sessions/login'
driver.get(url)

#Ingreso credenciales
text_input = driver.find_element_by_name('rut')
text_input.send_keys("pablotobar")

text_input = driver.find_element_by_name('password')
text_input.send_keys("pablotobar")

login_button = driver.find_element_by_name("ingresar")
login_button.click()
time.sleep(2)

#Se selecciona la opcón "Cajas" del Menú
caja = driver.find_element_by_xpath('/html/body/div[15]/div/div/table/tbody/tr/td[1]/ul/li[3]/a')
caja.click()
time.sleep(2)

#Se selecciona la opción "Cajas Cerradas"
cajaCerrada = driver.find_element_by_xpath('//*[@id="main-view"]/div[1]/div/div/ul/li[2]/a')
cajaCerrada.click()
time.sleep(2)

#Se baja hasta el final de la página para obtener todas las cajas
SCROLL_PAUSE_TIME = 0.5
last_height = driver.execute_script("return document.body.scrollHeight")

try:

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


    wait = WebDriverWait(driver, 30)
    #tbody = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="cajas-cerradas-tabla"]/tbody/tr')))
    #tbody = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="cajas-cerradas-tabla"]/tbody')))
    #table = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="cajas-cerradas-tabla"]')))
    #html = table[0].get_attribute('innerHTML')

    #***************************
    '''
    session = requests.Session()
    jar = requests.cookies.RequestsCookiesJar()
    jar.set('PHPSESSID','tjerunqk7v17imaq6sm3463of3')
    session.cookies = jar

    r = 'https://clinicadentalfa.dentalink.cl/cajas/cerradas/20/0/0'
    j = json.loads(r.text)
    '''
    #cookies = {'PHPSESSID':'tjerunqk7v17imaq6sm3463of3'}
    #response = requests.get(url, cookies=cookies)



    #***************************





    #obtengo la tabla y la convierto en un elemento panda para manipularla
    #data1 = pd.read_html(str(html))
    soup = BeautifulSoup(driver.page_source,'html.parser')
    table = soup.find("table", {"id": "cajas-cerradas-tabla"})
    data1 = pd.read_html(str(table))
    #print(data1[0])


    usuario = ''
    apertura = ''
    cierre = ''
    total_abonos = ''
    total_gastos = ''
    saldo_cierre = ''




    ##Se recorre la tabla para obtener la información
    #for tr in tbody:
        ##print(tr.get_attribute('innerHTML'))
        #tds = tr.find_elements_by_tag_name('td')
        ##print('usuario: ' + tds[0].get_attribute('innerHTML'))
        ##print('apertura: ' + tds[1].get_attribute('innerHTML'))
        #print('detalle: ' + tds[3].get_attribute('innerHTML'))
        ##print('**************')
        #usuario = tds[0].get_attribute('innerHTML').strip()
        #apertura = tds[1].get_attribute('innerHTML').strip()
        #cierre = tds[2].get_attribute('innerHTML').strip()
        #total_abonos = tds[4].get_attribute('innerHTML').strip()
        #total_gastos = tds[5].get_attribute('innerHTML').strip()
        #saldo_cierre = tds[6].get_attribute('innerHTML').strip()

        #detalle = tds[3]
        #detalle.click()
        #time.sleep(2)


        #divId = driver.find_element_by_xpath('/html/body/div[25]/div[1]/div/div/div[1]')
        #id = divId.get_attribute('innerHTML').strip()
        #print('id: ' + divId.get_attribute('innerHTML'))


        #close_button = driver.find_element_by_xpath('/html/body/div[25]/div[3]/button')
        #close_button.click()
        #time.sleep(2)

        #dataframe = dataframe.append({'Usuario':usuario,'Apertura':apertura,'Ciere':cierre,'Total_Abonos':total_abonos,'Total_Gastos':total_gastos,'Saldo_Cierre':saldo_cierre,'Id':id},ignore_index=True)

finally:
    print('******** Finally ********')
    #dataframe.to_csv("cajas.csv",sep=',', index=False)
    #data1[0].to_csv("cajas.csv",sep=',', index=False)



#soup = BeautifulSoup(driver.page_source,"html.parser")
#print(soup)

#driver.close()
