from selenium import webdriver
import re
import time
import datetime
def normal_datetime(timestamp):
    return (datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))
url = "http://127.0.0.1:8000/polls/yamap"
import time

while(1):

    driver = webdriver.Chrome('C:/Users/raev_e/Downloads/chromedriver_win32/chromedriver.exe') 
    driver.get(url) 
    time.sleep(2) 
    htmlSource = driver.page_source 
    driver.quit()
    print 1
    #print re.findall('.*?<br',htmlSource)
    try:
        mas =  htmlSource.split('<div id="list">')[1].split('<br')

        route_time =  mas[0].split(' ')[1]
        ideal_time =  mas[1].split(' ')[3]
        length =  mas[2].split(' ')[2]
        f = open("time.txt","a")
        string = str(route_time)+' '+str(length)+' '+str(normal_datetime(time.time()))+'\n'
        print string
        f.write(string)
        f.close()
        time.sleep(300)
    except:
        print "Error", time.time()
    
