import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

filename = input("ชื่อไฟล์ : ")
#filename = "test"
#Insert file name
start_page = int(input("ใส่เลขหน้าเริ่มต้น: "))
#start_page = 2

#Insert result name
end_page = int(input("ใส่เลขหน้าสุดท้าย: "))
#end_page = 2



page = []

#Get bot selenium make sure you can access google chrome
driver = webdriver.Chrome(ChromeDriverManager().install())


title_lis = []
url_lis = []
address_lis = []
dev_lis = []
year_lis = []

bed_lis = []
bath_lis = []
price_sqm_lis = []


price_lis = []
public_price_lis = []
area_lis = []
total_condo_lis = []
total_floor_lis =[]
total_unit_lis = []
park_area_lis = []
lat_lis = []
long_lis = []
fac_lis = []
google_map_lis = []
rec_lis = []
prov_lis = []
amphor_lis = []
about_lis = []
detail_lis = []
#tel_lis = []
#web_lis = []
count = 0





for i in range(start_page,end_page+1):
    
    url = "https://propertyscout.co.th/%E0%B8%81%E0%B8%A3%E0%B8%B8%E0%B8%87%E0%B9%80%E0%B8%97%E0%B8%9E/%E0%B8%82%E0%B8%B2%E0%B8%A2/%E0%B8%84%E0%B8%AD%E0%B8%99%E0%B9%82%E0%B8%94+%E0%B8%AD%E0%B8%9E%E0%B8%B2%E0%B8%A3%E0%B9%8C%E0%B8%97%E0%B9%80%E0%B8%A1%E0%B9%89%E0%B8%99%E0%B8%97%E0%B9%8C+%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%81%E0%B8%9D%E0%B8%94+%E0%B8%9A%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B9%80%E0%B8%94%E0%B8%B5%E0%B9%88%E0%B8%A2%E0%B8%A7+%E0%B8%97%E0%B8%B2%E0%B8%A7%E0%B8%99%E0%B9%8C%E0%B9%80%E0%B8%AE%E0%B9%89%E0%B8%B2%E0%B8%AA%E0%B9%8C/%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2-{}/".format(i)
    
    driver.get(url)
    time.sleep(3)
    print(driver.page_source)

    soup = BeautifulSoup(driver.page_source,'html.parser')
 
    lis = [ d['href'] for d in soup.find_all('a',{'class':'w-full'})]
    print(lis)

    for link in lis: 
        driver.get(link)
        
        # for i in range(1):
        #     driver.execute_script('window.scrollBy(0, 5000)')
        #     time.sleep(2)
        
        soupx = BeautifulSoup(driver.page_source,'html.parser')

        detail = [ item.text for item in driver.find_element(By.CSS_SELECTOR,'ul').find_elements(By.CSS_SELECTOR,'li')]
        
        detail_data = "\n".join(detail)
        print(detail_data)
        detail_lis.append(detail_data)

        #bedroom
        bedroom = detail[0]
        print("bed : ",bedroom)
        bed_lis.append(bedroom)

        #bathroom 
        bath = detail[1]
        print("bathroom : ",bath)
        bath_lis.append(bath)

        #sqm 
        area = detail[2]
        print("area : ",area)
        area_lis.append(area)

        # floor = detail[3]
        # print("floor : ",floor)
        # total_floor_lis.append(floor)

        # price_per_sqm = detail[4]
        # print("Price per sqm : ",price_per_sqm)
        # price_sqm_lis.append(price_sqm_lis)


        #ชื่อโครงการ
        title = driver.find_element(By.CSS_SELECTOR,"h1.leading-snug")
        print(title.text)
        title_lis.append(title.text.strip())

        url_lis.append(link)
        print(link)

        address = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/p[1]')
        print(address.text)
        address_lis.append(address.text.strip())
    
        price = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/p[2]')
        print(price.text)
        price_lis.append(price.text)    





        lat_long = [ g.text for g in driver.find_elements(By.CSS_SELECTOR,'div.mt-2')]
        print("------")
        print(lat_long)

        try:
            lat_long_data = lat_long[0].split(",")
            lat = lat_long_data[0]

            print("Lat : ",lat)

            long = lat_long_data[1]
            print("Long : ",long)

            lat_lis.append(lat)
            long_lis.append(long)
        except: 
             print("lat : None")
             print("long : None")

             lat_lis.append(" ")
             long_lis.append(" ")



        about = driver.find_element(By.CSS_SELECTOR,'.property-listing-about').text 
        print(about)
        about_lis.append(about)

    print(lis)

time.sleep(2)


df = pd.DataFrame()

df['ชื่อโครงการ'] = title_lis 
df['ลิงค์'] = url_lis 
df['จำนวนห้องนอน'] = bed_lis 
df['จำนวนห้องน้ำ'] = bath_lis 
df['พื้นที่'] = area_lis 
df['รายละเอียด'] = detail_lis
df['ที่อยู่เต็ม'] = address_lis 
df['ราคาเปิดตัว'] = price_lis 
df['Latitude'] = lat_lis 
df['Longtitude'] = long_lis
df['เกี่ยวกับ'] = about_lis
#df['Web'] = web_lis
#df['โทร'] = tel_lis


df.to_excel(filename+".xlsx")

print("All Done")