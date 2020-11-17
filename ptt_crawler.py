#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
#import pathlib
import os
import re
import csv


class ptt_crawl:
    def __init__(self, html, filename, page, delay):
        self.html = html
        self.filename = filename
        self.page = page
        self.delay = delay
        #self.driver = pathlib.Path(__file__).parent.absolute().joinpath("chromedriver.exe")
        self.driver = os.path.join(os.path.dirname((os.path.realpath(__file__))), "chromedriver.exe")
        print(self.driver)
    
    #開始爬蟲
    def start(self):
        self.driver = webdriver.Chrome(self.driver)
        self.driver.get(f"{self.html}")
        self.driver.add_cookie({'name':'over18', 'value':'1'})
        self.driver.get(f"{self.html}")
        assert "批踢踢" in self.driver.title

        #創一個新的.csv檔，並寫入
        with open(f'{self.filename}', 'w+', newline='') as self.practice:
            self.writer = csv.writer(self.practice, delimiter = ',', quotechar = '|', quoting=csv.QUOTE_MINIMAL)
            self.writer.writerow(['噓', '標題', '連結'])

            #找前page頁的內容
            for i in range(self.page+1):
                self.findX(self.driver, self.writer)
                self.nextpage(self.driver)
                time.sleep(self.delay)


    #把被噓到X的推文找出來並寫入CSV檔
    def findX(self, driver, writer):
        row = driver.find_elements_by_xpath('//*[@id="main-container"]/div[2]/div[@class="r-ent"]')
        for i in row:
            try:
                endorse = i.find_element_by_xpath('.//div[@class = "nrec"]/span')
                if re.fullmatch('X.', endorse.text):
                    title = i.find_element_by_xpath('.//div[@class = "title"]/a')
                    writer.writerow([endorse.text, title.text, title.get_attribute('href')])
            except NoSuchElementException:
                pass
    
    #上一頁
    def nextpage(self, driver):
        button = driver.find_element_by_xpath('//*[@id="action-bar-container"]/div/div[2]/a[2]')
        button.click()
        
            
if __name__ == '__main__':
    print('Ptt crawler is running')

    ptt_gossip = ptt_crawl(
        html='https://www.ptt.cc/bbs/Gossiping/index.html', #輸入你想要的ptt某版網址
        filename='practice.csv',    #爬蟲下來csv檔的檔案名稱
        page=20,    #總共爬幾頁
        delay=1.5)    #爬蟲時換頁的間隔時間(秒)，避免變成DDOS

    #ptt_gossip.driver=("c:\Users\user\Desktop\crawler.py") #chromedriver.exe的路徑(含檔案名稱/chromedriver.exe)，預設路徑是這個python檔的路徑
    ptt_gossip.start()  #開始爬蟲

    print('done')


# In[ ]:




