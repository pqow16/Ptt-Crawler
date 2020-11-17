# Ptt爬蟲
簡介：
這是我的第一個爬蟲程式，它可以把PTT裡被噓到有X的文章(噓數、標題、網址)擷取下來存成csv檔。

需求：
python
Selenium
google chrome

使用說明：
將ptt_crawler.py與chromedriver.exe放在同一個資料夾，並執行ptt_crawler.py。
在ptt_crawler.py裡的 __name__=="__main__" 裡可以設定要爬的PTT版、爬的頁數、存檔名稱與間隔時間。
