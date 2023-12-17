import requests, sys, bs4, os
from selenium import webdriver
import ssl
import time
from urllib3.exceptions import InsecureRequestWarning
import warnings

#warnings.simplefilter('ignore',InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

epro = requests.get('https://hldme.tzuchi-healthcare.org.tw/', verify=False)

#啟動chrome
browser = webdriver.Chrome()
browser.get('https://hldme.tzuchi-healthcare.org.tw/')
os.system('pause')

#按按鈕
def click_xpath(buttom):
    ele_c=''
    while ele_c == '':
        try:
            ele_c = browser.find_element_by_xpath(buttom)
            ele_c.click()
            print(str(buttom)+'  preesed')
            time.sleep(0.5)
            break
        except:
            print("oops")
            time.sleep(3)
            continue
    
def find_xpath(text):
    ele_f=''
    while ele_f == '':
        try:
            ele_f = browser.find_element_by_xpath(text)
            ele_f.click()
            print(str(text)+'  preesed')
            return 1
            break
        except:
            print("oops")
            return 0
            break

#按登入紐
click_xpath('/html/body/div[1]/section[1]/div/div/div[2]/div/div[2]/form/div[3]/button/h5')
#找到80項技能
click_xpath('/html/body/main/header/nav[2]/div/div[2]/ul/li[8]/a')
click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/table/tbody/tr/td[3]/input')
click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div')

#尋找開頭點
global op
for op in range(1,80):
    i = find_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div['+str(op+1)+']/div/div/div/div[2]/p')
    if i == 1:
        print('從第 '+str(op)+'份開始填寫')
        break
#/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[2]/p
#/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div/div/div[2]/p
#/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div[4]/div/div/div/div[2]/p

#填寫表單
wr = op
for i in range(wr, 80):
    print('開始填寫第'+str(i)+'份')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div['+str(i+1)+']/div/div/div/div[3]/input[2]')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[2]/div[1]/input')
    click_xpath('/html/body/div[3]/div/div/div[3]/div/div/button')
    click_xpath('/html/body/div[5]/div/div/div[3]/div/div/button')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[2]/table/tbody/tr/td[3]/a')
    #勾選四項
    #click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[1]/select')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[1]/select/option[1]')
    #click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[2]/select')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[2]/select/option[2]')
    #click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[3]/select')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[3]/select/option[3]')
    #click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[4]/select')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[4]/select/option[5]')
    #送出
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[3]/input[1]')
    click_xpath('/html/body/div[3]/div/div/div[3]/div/div/button')
    click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[3]/input')
    print('第 '+str(op)+'份填寫完成')
    time.sleep(3)

#/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div/div/div[3]/input[2]
#/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div/div[3]/div/div/div/div[3]/input[2]


os.system('pause')
print('end')

