# Ptt爬蟲
## 簡介：
這是我的第一個爬蟲程式，製作環境為python 3.9。這個程式可以把PTT裡被噓到有X的文章(噓數、標題、網址)擷取下來存成csv檔。


## 安裝：
1. 將ptt_crawler.py, chromedriver.exe, Requirement.exe放到任何你喜歡的資料夾
2. 在python中輸入
```py 
pip install -r /(資料夾路徑)/requirements.txt
```
3. 將ptt_crawler.py與chromedriver.exe放到任何你喜歡的資料夾，再在你的IDE中執行ptt_crawler.py即可。
* 這邊提供的chromedriver是給windows系統使用的，如果是其他的作業環境，請到 [chromium](https://chromedriver.chromium.org/downloads) 下載對應的版本


## 使用說明：
預設上這個程式會去 [ptt八卦版](https://www.ptt.cc/bbs/Gossiping/index.html) 爬蟲。以每 **1.5秒** 的間隔時間換頁並抓下 **前20頁** 的內容，再將資料存成 **practice.csv** 。
如果要修改爬蟲內容，在ptt_crawler.py中找到 
```py 
if __name__=="__main__"
``` 
修改ptt_gossip這個instance的variable
```py
ptt_gossip = ptt_crawl(
        html='https://www.ptt.cc/bbs/Gossiping/index.html',
        filename='practice.csv',
        page=20,
        delay=1.5)
```
html中輸入你想要的ptt版網址，filename輸入你想要儲存的csv檔檔名，page輸入你想抓前幾頁的頁數，delay中輸入換頁的間隔時間。


* 如果你的chromedriver.exe與ptt_crawler.py不是在同一個資料夾，把以下的code改成你的chromedriver.exe的路徑
```py
ptt_gossip.driver=("c:\Users\user\Desktop\chromedriver.exe")
```