import requests
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm
import os
import time
from colorama import  Back, Fore, Style
from colorama import init
init()
 
os.system("mode con cols=135")
user_agent = ["Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"]

API_ENDPOINT = "http://pastebin.com/api/api_post.php"
API_KEY = "bc905d5c24fb18e40eff6ae3364988af"


class scrape_proxy:
    def pastebin():
        for x in tqdm(range(5)):
            time.sleep(0.1)
        urll = 'https://www.proxy-daily.com/'
        r = requests.get(urll).text
        soup = BeautifulSoup(r, features='html.parser')
        k = soup.find('div', {'class': 'centeredProxyList freeProxyStyle'})
        rep = str(k).replace('<div class="centeredProxyList freeProxyStyle">', '')
        rep = rep.replace('</div>', '')        
        source_code = rep
        data = {'api_dev_key':API_KEY, 
		'api_option':'paste', 
		'api_paste_code':source_code, 
		'api_paste_format':'python'} 
        r = requests.post(url = API_ENDPOINT, data = data) 
        pastebin_url = r.text 
        print("The pastebin URL is:%s"%pastebin_url) 

    def http():
        for x in tqdm(range(5)):
            time.sleep(0.1)
        urll = 'https://www.proxy-daily.com/'
        r = requests.get(urll).text
        soup = BeautifulSoup(r, features='html.parser')
        k = soup.find('div', {'class': 'centeredProxyList freeProxyStyle'})
        rep = str(k).replace('<div class="centeredProxyList freeProxyStyle">', '')
        rep = rep.replace('</div>', '')        
        with open('ProxyPy_http.txt', 'a') as ww:
            ww.writelines(rep)
            ww.close()
        #print(Back.BLUE+'\n\n.......')
        print(Fore.GREEN+ ' \nLeeching\'s Done Successfully')
        time.sleep(2)
        print('\nRemoving Duplicates...')
        time.sleep(1)
        
def main():
    print(Fore.YELLOW+'''
                         
                    |===============================================================================================================|
                    |                                                                                                               |
                    |                                                                                                               |
                    |            .|````,          `||                   `||````|             `||`                                   |
                    |            ||                ||                    ||   .          ``   ||                                    |
                    |            ||      `||  ||`  ||``|, .|``|, `||``|  ||```|  \\\  //  ||   ||                                    |
                    |            ||       `|..||   ||  || ||..||  ||     ||       \\\//   ||   ||                                    |
                    |            `|....`      ||  .||..|` `|...  .||.   .||....|   \/   .||. .||.                                   |
                    |                      ,  |`                                                                                    |
                    |                       ``                  DEVELOPED BY: CALLMEFINN#3111                                       |   
                    |                                           DISCORD SERVER: http://cyberevill.me/                               |
                    |                         `||```|,                                                                              |
                    |                          ||   ||                                                                              |
                    |                          ||...|` `||``| .|``|, \\\ // `||  ||`                                                 |
                    |                          ||       ||    ||  ||   ><   `|..||                                                  |
                    |                         .||      .||.   `|..|` //  \\\     ||                                                  |
                    |                                                        ,  |`                                                  |
                    |                                                         ``   v 1.0.0                                          |
                    |                                                                                                               |''')
    print("                    |        Congratulations!, now you can save proxies online/offline with our latest cyberevil proxy tool if you  |  ")  
    print("                    |        wish to save the proxy file in your system it will be saved as .txt file or if you wish to save in     |  ")
    print("                    |                    cloud you will get pastebin link. hope you will like this..                                |  ")
    print(Fore.GREEN+"                    |                                    .........................                                                  |  ")
    print(Fore.RED+"                    |              [Right now we are scraping only HTTP/S PROXIES soon we will be adding SOCKS4/5]                  |  ")
    print(Fore.YELLOW+"                    |===============================================================================================================|   ")
    
    print(Fore.GREEN+"\n")  

    onoff=input('''ENTER YOUR CHOICE TO SAVE YOUR FILE...
==> FOR OFFLINE PRESS (S)/ FOR ONLINE PRESS  (C)''')
    if onoff== "C" or onoff== "c":
        scrape_proxy.pastebin()
    elif onoff== "S" or onoff=="s":
        scrape_proxy.http()
    h=input('\nPress Enter To Continue...')
    if h == "x"or  h=='X':
        exit()
    elif h=='c' or h=='C':
        return main()
    else:
        exit()
main()











