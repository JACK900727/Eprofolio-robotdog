import os
import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import threading
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

path = os.getcwd()
print(path)

        
#啟動chrome 
def browse(): 
    global browser
    browser = webdriver.Chrome()
    browser.get('https://hldme.tzuchi-healthcare.org.tw/')
    
#按按鈕
def click_xpath(buttom):
    ele_c=''
    while ele_c == '':
        try:
            ele_c = browser.find_element(By.XPATH, buttom)
            ele_c.click()
            print(str(buttom)+'  preesed')
            time.sleep(0.5)
            break
        except Exception as e:
            print(e)
            time.sleep(1)
            continue
def key_xpath(key,num):
    ele_k=''
    while ele_k == '':
        try:
            ele_k = browser.find_element(By.XPATH, key)
            ele_k.send_keys(num)
            print(str(key)+'  preesed')
            return 1
            break
        except:
            print("oops")
            return 0
            break
def find_xpath(text):
    ele_f=''
    while ele_f == '':
        try:
            ele_f = browser.find_element(By.XPATH, text)
            ele_f.click()
            print(str(text)+'  preesed')
            return 1
            break
        except:
            print("oops")
            return 0
            break


def win():
    #建立視窗
    global root
    root = tk.Tk()
    font = tkFont.Font(family="Microsoft JhengHei", size=14)
    root.geometry("600x600")
    root.resizable(False, False)
    root.iconbitmap('paw.ico')
    root.title("幾田的機器狗")

    label1 = tk.Label(root, text="輸入帳號")
    label1.place(x=85, y=100, anchor='center')
    label2 = tk.Label(root, text="輸入密碼")
    label2.place(x=85, y=150, anchor='center')
    global pro_num
    global pro
    pro_num = 0
    pro = tk.StringVar()
    pro.set('當前進度: '+str(pro_num)+'/80')
    label3 = tk.Label(root, textvariable=pro)
    label3.place(x=100, y=200, anchor='center')
   
    global bar
    bar = ttk.Progressbar(root, mode='determinate', phase=20)
    bar.place(x=300, y=200, anchor='center')
    bar['length']=300
    bar['maximum']=80
    bar['value']=pro_num
    global entry1
    global entry2
    entry1 = tk.Entry(root)
    entry1.place(x=200, y=100, anchor='center')
    entry2 = tk.Entry(root)
    entry2.place(x=200, y=150, anchor='center')

        
    button1 = tk.Button(root, text='80項技能',font = font, command = bb.start)
    button1.place(x=100, y=500, anchor='center')
    #button2 = tk.Button(root, text='E-profolio',font = font)
    #button2.place(x=300, y=500, anchor='center')


    root.mainloop()
def skill_80():
    browse()
    
    #登入
    acc = str()
    pas = str()
    acc = entry1.get()
    pas = entry2.get()
    key_xpath('/html/body/div[1]/section[1]/div/div/div[2]/div/div[2]/form/div[1]/input', acc)
    key_xpath('/html/body/div[1]/section[1]/div/div/div[2]/div/div[2]/form/div[2]/input', pas)
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
            pro_num = op
            pro.set('當前進度: '+str(pro_num)+'/80')
            bar['value']=pro_num
            root.update()
            break
    
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
       
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[1]/select/option[1]')
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[2]/select/option[2]')
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[3]/select/option[3]')
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[2]/div[4]/select/option[5]')
        #送出
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div/div[3]/input[1]')
        click_xpath('/html/body/div[3]/div/div/div[3]/div/div/button')
        click_xpath('/html/body/main/div[1]/div/div/div[1]/div/div[1]/div[3]/input')
        print('第 '+str(i)+'份填寫完成')
        pro_num = i
        pro.set('當前進度: '+str(pro_num)+'/80')
        bar['value']=pro_num
        root.update()
        time.sleep(2)

    


    
    print('end')
    os.system('pause')
 
def main():    
    a = threading.Thread(target=win)
    a.start()
    global bb
    bb = threading.Thread(target=skill_80)
if __name__ == '__main__':
    main()
os.system("pause")





