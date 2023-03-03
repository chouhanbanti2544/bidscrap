#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
ser = Service(ChromeDriverManager().install())
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from time import sleep
import json


# In[2]:


driver = webdriver.Chrome(service=ser)

driver.maximize_window()



url = 'https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787'

driver.get(url)
driver.implicitly_wait(5)
sleep(2)

bid_req = driver.find_element(By.XPATH,"//tbody/tr/td[4]")
bid_req.click()
sleep(3)

BID_Details = []   

for i in range(1,11):
    Estv= []
    Est = driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[3]/td[2]')
    for j in Est:
        Estv.append(j.text)  
    sleep(2)

    
    DES = []
    descheck = driver.find_elements(By.XPATH,'//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[2]/td[1]')
    for l in descheck:
        if l.text =='Description:':
            pro_det = driver.find_elements(By.XPATH,'//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[2]/td[2]')
            for pro in pro_det:
                DES.append(pro.text)
                
        else:
            pro_det1 = driver.find_elements(By.XPATH,'/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[4]/div[1]/div[4]/div[2]/div[1]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[2]')
            for k in pro_det1:
                DES.append(k.text)
                
        
        

    
    Close = []
    Closing_Date = driver.find_elements(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[4]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]')
    for m in Closing_Date:
        Close.append(m.text)
        
        
    for no in range(len(Estv)):
        values = {
            'Est.value':Estv[no],
            'Description':DES[no],
            'Closing_Dates':Close[no]
        }
        BID_Details.append(values)
    with open('scrapingBID.json','w') as f:
        json.dump(BID_Details,f)


        
    #Next page
    driver.find_element(By.XPATH,'//button[@id="id_prevnext_next"]/b').click()
    
    sleep(2)
    

 


# In[ ]:




