import requests
import urllib
import re
import pandas as pd
from bs4 import BeautifulSoup


data = pd.read_csv("bizzbuysell/bizbuysell.csv")
dataframe = pd.DataFrame(columns=["US-State","URL","Title","Location","AskPrice","CashFlow","GrossRevenue","EBITDA","FF&E","Inventory","Rent","RealEstate","Established","Inventory-2","RealEstate-2","BuildingSF","LeaseExpiration","Employees","FurnitureFixturesAndEquipment","Facilities","GrowthAndExpansion","Financing","SupportAndTraining","ReasonForSelling"])


print("**** Inicio ****")
for index,fila in data.iterrows():
    #url = 'https://www.bizbuysell.com/Business-Opportunity/Profitable-Exterior-Property-Maintenance-Business/1758753/?d=JTJmYWxhYmFtYS1idXNpbmVzc2VzLWZvci1zYWxlJTJmJTNmcSUzZGFYSTlNU1p6Y0dsa1BURW1kejF4'
    url = fila['URL']
    print(url)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    page = requests.get(url, headers = headers)

    soup = BeautifulSoup(page.content,'html.parser')

    if soup.find('h1',class_='bfsTitle') is not None:
        title = soup.find('h1',class_='bfsTitle').getText()
    else:
        title = ''
    #print("title: " + title)

    #image = soup.find('div',class_='image')
    #image_attributes = image.attrs['style']
    if soup.find('h2',class_='gray') is not None:
        location = soup.find('h2',class_='gray').getText()
    else:
        location = ''
    #print("location: " + location)

    tags = soup.findAll('div',class_ =['span6','specs'])
    #print(tags)

    if tags[0].find("p").b is not None:
        askPrice =  tags[0].find("p").b.getText()
        #print("askPrice: " + askPrice)
    else:
        askPrice = ''

    if tags[1].find("p").b is not None:
        cashFlow = tags[1].find("p").b.getText()
        #print("cashFlow: " + cashFlow)
    else:
        cashFlow = ''

    grossRevenue = ''
    ebitda = ''
    ff = ''
    inventory = ''
    rent = ''
    realEstate = ''
    established = ''


    if tags is not None:

        for tag in tags:
            ps = tag.findAll("p")

            for p in ps:
                #print(p)
                if p.span.find(text=re.compile("Gross Revenue")) is not None:
                    #grossRevenue = tag.p.find(text=re.compile("Gross Revenue")).findNext("b").getText()
                    #grossRevenue = tags[2].findAll("p")[0].b.getText()
                    grossRevenue = p.b.getText()
                    #print("grossRevenue: " + grossRevenue)

                if p.span.find(text=re.compile("EBITDA")) is not None:
                    ebitda = p.b.getText()
                    #ebitda = tags[2].findAll("p")[1].b.getText()
                    #print("ebitda: " + ebitda)

                if p.span.find(text=re.compile("FF&E")) is not None:
                    ff = p.b.getText()
                    #ff = tags[2].findAll("p")[2].b.getText()
                    #print("ff: " + ff)

                if p.span.find(text=re.compile("Inventory")) is not None:
                    inventory = p.b.getText()
                    #inventory = tags[3].findAll("p")[0].b.getText()
                    #print("inventory: " + inventory)

                if p.span.find(text=re.compile("Rent")) is not None:
                    rent = p.b.getText()
                    #rent = tags[3].findAll("p")[1].b.getText()
                    #print("inventory: " + inventory)

                if p.span.find(text=re.compile("Real Estate")) is not None:
                    realEstate = p.b.getText()
                    #realEstate = tags[3].findAll("p")[1].b.getText()
                    #print("inventory: " + inventory)

                if p.span.find(text=re.compile("Established")) is not None:
                    established = p.b.getText()
                    #established = tags[3].findAll("p")[2].b.getText()
                    #print("established: " + established)

    tags = soup.findAll("dl", {"class": "listingProfile_details"})


    detailInformation = soup.find('dl',class_='listingProfile_details')

    inventory2 = ''
    realEstate2 = ''
    buildingSF = ''
    leaseExpiration = ''
    employees = ''
    furnitureFixturesAndEquipment = ''
    facilities = ''
    growthAndExpansion = ''
    financing = ''
    supportAndTraining = ''
    reasonForSelling = ''

    businessDescription = ''

    if detailInformation is not None:
        if detailInformation.find(text=re.compile("Inventory")) is not None:
            #print(detailInformation.find(text=re.compile("Inventory")))
            #print(detailInformation.find(text=re.compile("Inventory")).findNext("dd").getText())
            inventory2 = detailInformation.find(text=re.compile("Inventory")).findNext("dd").getText()
            #print("inventory2: " + inventory2)

        if detailInformation.find(text=re.compile("Real Estate")) is not None:
            #print(detailInformation.find(text=re.compile("Real Estate")))
            #print(detailInformation.find(text=re.compile("Real Estate")).findNext("dd").getText())
            realEstate2 = detailInformation.find(text=re.compile("Real Estate")).findNext("dd").getText()
            #print("realEstate2: " + realEstate2)

        if detailInformation.find(text=re.compile("Building")) is not None:
            #print(detailInformation.find(text=re.compile("Building")))
            #print(detailInformation.find(text=re.compile("Building")).findNext("dd").getText())
            buildingSF = detailInformation.find(text=re.compile("Building")).findNext("dd").getText()
            #print("buildingSF: " + buildingSF)

        if detailInformation.find(text=re.compile("Lease Expiration")) is not None:
            #print(detailInformation.find(text=re.compile("Lease")))
            #print(detailInformation.find(text=re.compile("Lease")).findNext("dd").getText())
            leaseExpiration = detailInformation.find(text=re.compile("Lease Expiration")).findNext("dd").getText()
            #print("leaseExpiration: " + leaseExpiration)

        if detailInformation.find(text=re.compile("Employees")) is not None:
            #print(detailInformation.find(text=re.compile("Employees")))
            #print(detailInformation.find(text=re.compile("Employees")).findNext("dd").getText())
            employees = detailInformation.find(text=re.compile("Employees")).findNext("dd").getText()
            #print("employees: " + employees)

        if detailInformation.find(text=re.compile("Furniture")) is not None:
            #print(detailInformation.find(text=re.compile("Furniture")))
            #print(detailInformation.find(text=re.compile("Furniture")).findNext("dd").getText())
            furnitureFixturesAndEquipment = detailInformation.find(text=re.compile("Furniture")).findNext("dd").getText()
            #print("furnitureFixturesAndEquipment: " + furnitureFixturesAndEquipment)

        if detailInformation.find(text=re.compile("Facilities")) is not None:
            #print(detailInformation.find(text=re.compile("Facilities")))
            #print(detailInformation.find(text=re.compile("Facilities")).findNext("dd").getText())
            facilities = detailInformation.find(text=re.compile("Facilities")).findNext("dd").getText()
            #print("facilities: " + facilities)

        if detailInformation.find(text=re.compile("Growth")) is not None:
            #print(detailInformation.find(text=re.compile("Growth")))
            #print(detailInformation.find(text=re.compile("Growth")).findNext("dd").getText())
            growthAndExpansion = detailInformation.find(text=re.compile("Growth")).findNext("dd").getText()
            #print("growthAndExpansion: " + growthAndExpansion)

        if detailInformation.find(text=re.compile("Financing")) is not None:
            #print(detailInformation.find(text=re.compile("Financing")))
            #print(detailInformation.find(text=re.compile("Financing")).findNext("dd").getText())
            financing = detailInformation.find(text=re.compile("Financing")).findNext("dd").getText()
            #print("financing: " + financing)

        if detailInformation.find(text=re.compile("Support")) is not None:
            #print(detailInformation.find(text=re.compile("Support")))
            #print(detailInformation.find(text=re.compile("Support")).findNext("dd").getText())
            supportAndTraining = detailInformation.find(text=re.compile("Support")).findNext("dd").getText()
            #print("supportAndTraining: " + supportAndTraining)

        if detailInformation.find(text=re.compile("Reason")) is not None:
            #print(detailInformation.find(text=re.compile("Reason")))
            #print(detailInformation.find(text=re.compile("Reason")).findNext("dd").getText())
            reasonForSelling = detailInformation.find(text=re.compile("Reason")).findNext("dd").getText()
            #print("reasonForSelling: " + reasonForSelling)

        dataframe = dataframe.append({'US-State':'Vermont','URL':url,'Title':title.strip(),'Location':location.strip(),'AskPrice':askPrice.strip(),'CashFlow':cashFlow.strip(),'GrossRevenue':grossRevenue.strip(),'EBITDA':ebitda.strip(),'FF&E':ff.strip(),'Inventory':inventory.strip(),'Rent':rent.strip(),'RealEstate':realEstate.strip(),'Established':established.strip(),'Inventory-2':inventory2.strip(),'RealEstate-2':realEstate2.strip(),'BuildingSF':buildingSF.strip(),'LeaseExpiration':leaseExpiration.strip(),'Employees':employees.strip(),'FurnitureFixturesAndEquipment':furnitureFixturesAndEquipment.strip(),'Facilities':facilities.strip(),'GrowthAndExpansion':growthAndExpansion.strip(),'Financing':financing.strip(), 'SupportAndTraining':supportAndTraining.strip(),'ReasonForSelling':reasonForSelling.strip()}, ignore_index=True)

dataframe.to_csv("bizzbuysell/bizzbuyselldata.csv",sep='|', index=False)
print("**** Fin ****")
