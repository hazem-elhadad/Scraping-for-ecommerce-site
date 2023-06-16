from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
from time import sleep
import pandas as pd
csv_sucess_file = open("upwork22.csv", "w", encoding="utf-8", newline='')
success_writer = csv.writer(csv_sucess_file)
success_writer.writerow(['Name' , 'Title' , 'SellingPrice' , 'TicketPrice' , 'Size' , 'Color' , 'Image' ,'ProductUrl'])
prolinks=[]
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
listofcategorieslinks=['https://www.evanscycles.com/brand/cannondale' , 'https://www.evanscycles.com/brand/trek','https://www.evanscycles.com/brand/specialized'
                       ,'https://www.evanscycles.com/bikes/mountain-bikes' , 'https://www.evanscycles.com/bikes/road-bikes','https://www.evanscycles.com/bikes/hybrid-bikes' ,
                       'https://www.evanscycles.com/bikes/gravel-bikes','https://www.evanscycles.com/bikes/folding-bikes','https://www.evanscycles.com/bikes/kids-bikes' ,'https://www.evanscycles.com/skate#dcp=1&dppp=120&OrderBy=rank','https://www.evanscycles.com/skate#dcp=2&dppp=120&OrderBy=rank'
                       ,'https://www.evanscycles.com/brand/haibike','https://www.evanscycles.com/electric-bikes/all-electric-bikes/specialized','https://www.evanscycles.com/electric-bikes/all-electric-bikes/trek','https://www.evanscycles.com/electric-bikes/electric-mountain-bikes',
                       'https://www.evanscycles.com/electric-bikes/electric-folding-bikes','https://www.evanscycles.com/electric-bikes/all-electric-bikes']
for ele1 in listofcategorieslinks:
    driver.get(ele1)
    sleep(2)
    productslinks= driver.find_elements(By.XPATH ,'//div[@class="productimage s-productthumbimage col-xs-6 col-sm-12"]')
    for link in productslinks:
        href = link.find_element(By.TAG_NAME,'a').get_attribute('href')
        prolinks.append(href)
print(len(prolinks))
df=pd.DataFrame(prolinks)
df.to_excel('linkss.xlsx' , index = False)
