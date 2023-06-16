from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep
import pandas as pd
import re
csv_sucess_file = open("upwork22.csv", "w", encoding="utf-8", newline='')
success_writer = csv.writer(csv_sucess_file)
success_writer.writerow(['Name' , 'Title' , 'SellingPrice' , 'TicketPrice' , 'Size' , 'Color' ,'ProductIMGS', 'Image' ,'ProductUrl', 'Description' , 'SKU'])
prolinks=[]
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

df=pd.read_excel('linkss.xlsx')

print(f"We have: {len(df[0])} to scrape....")
sleep(1)
counteroflinks=0
for href2 in df[0]:
    proimgs=[]
    Sizz = []
    Coll=[]
    IMGS=[]
    name="none"
    productTitle='none'
    sellingprice='none'
    ticketprice='none'
    Size='none'
    Color='none'
    Img='none'
    IMGURL='none'
    Discription="none"
    SKU='none'
    driver.get(href2)
    sleep(2)
    try:
        name = driver.find_element(By.ID , "lblProductBrand").text
    except:pass
    try:
        productTitle=driver.find_element(By.ID , "lblProductName").text
    except:pass
    try:
        sellingprice = driver.find_element(By.ID , "lblSellingPrice").text
    except:pass
    try:
        ticketprice=driver.find_element(By.ID , "lblTicketPrice").text
    except:pass
    try:
        Sizes = driver.find_elements(By.ID , "ancLink")
        for s in Sizes:
            Size=s.text
            Sizz.append(Size)
            finalsize=','.join(Sizz)
    except:pass
    try:
        try:
            Colors = driver.find_element(By.ID, "divColourImages").find_element(By.TAG_NAME,'ul').find_elements(By.TAG_NAME,'li')
            for col in Colors:
                Color=col.get_attribute('data-text')
                Coll.append(Color)
                finalcolor=', '.join(Coll)
                Img = col.find_element(By.XPATH, './a/img').get_attribute('src')
                IMGS.append(Img)
                finalcolimg=', '.join(IMGS)
        except:
            Color = driver.find_element(By.ID , 'colourName').text
            Coll.append(Color)
            finalcolor = ', '.join(Coll)
            Img = driver.find_element(By.XPATH ,'//img[@id="imgProduct"]').get_attribute('src')
            IMGS.append(Img)
            finalcolimg = ', '.join(IMGS)
    except:pass
    try:
        ProductIMGss=driver.find_element(By.XPATH ,'//ul[@id="piThumbList"]').find_elements(By.TAG_NAME,'li')
        for img in ProductIMGss:
            IMGURL=img.find_element(By.TAG_NAME,'a').get_attribute('href')
            proimgs.append(IMGURL)
            finalimgs=', '.join(proimgs)
    except:pass
    try:
        Discription = driver.find_element(By.XPATH , '//span[@itemprop ="description"]').get_attribute('innerHTML')
    except:pass
    try:
        SKU1 = driver.find_element(By.XPATH , '//p[@id="lblProductCode"]').text
        SKU=int(re.findall(r'\d+',SKU1)[0])
    except:pass
    success_writer.writerow(
        [name, productTitle, sellingprice,ticketprice,finalsize,finalcolor,finalimgs,finalcolimg , href2 , Discription , SKU])
    counteroflinks+=1
    print(f"We are Now in link: {counteroflinks}")
    # if counteroflinks == 10:
    #     break
csv_sucess_file.close()
main_data_frame = pd.read_csv("upwork22.csv")
writer = pd.ExcelWriter(r'upwork55_bikes.xlsx', engine='xlsxwriter')
main_data_frame.to_excel(writer, index=False)
writer.close()