# -*- coding: utf-8 -*-
terminal = ''
import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options 
options = Options()
options.headless = True 
driver = selenium.webdriver.Firefox(options=options)
import time
import datetime
import numpy as np
import requests
import os
os.environ['TZ'] = 'UTC'

login_url='http://vip1.jygj682.com/login.html'
driver.get(login_url)
time.sleep(1)
driver.set_window_size(400,800)
#driver.maximize_window()       # 全屏
print (driver.get_window_size())
    
username= driver.find_element_by_id('j_username')
password= driver.find_element_by_id('j_password')
username.clear()
password.clear()
username.send_keys("7ZC007")
password.send_keys("zczc507206")
WebDriverWait(driver,60).until(EC.visibility_of(driver.find_element(by=By.ID,value='j_captcha_img')))
"""
while driver.find_element_by_css_selector('#j_captcha'):
        
    driver.get_screenshot_as_file('验证码.png') 
    driver.find_element_by_css_selector('#j_captcha').clear()
    input_solution = input('请输入验证码 :') 
    driver.find_element_by_id('j_captcha').send_keys(input_solution)
    driver.find_element_by_css_selector('#j_button').click()
    time.sleep(2)
    if driver.current_url != login_url:
        print('验证成功，登录中')
        break
    else:
        print('验证中……',end = ',')
        time.sleep(2)
        continue
"""
while True:
    driver.get_screenshot_as_file('code.png')
    driver.find_element_by_css_selector('#j_captcha').clear()
    input_solution = input('Verificaction Code:')  #手工打码
    driver.find_element_by_id('j_captcha').send_keys(input_solution)
    driver.find_element_by_css_selector('#j_button').click()
    time.sleep(5)     
    if driver.current_url != login_url:
        print ('Logged,Continue!')
        break
    else:        
        print ('Verification Code')
        continue
time.sleep(3)

"""    
WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tips_xtgg"]/div/div/div[1]/button'))).click()
time.sleep(2)
#WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#body > div.fd_lxkf > em"))).click()
driver.execute_script('''document.querySelector('#tips_szsy > div > div > div.modal-body > ul > li:nth-child(4) > div > input[type="checkbox"]').click();''')
#driver.find_element_by_css_selector('#h_n_login > div.pull-left > a:nth-child(3) > i').click()
time.sleep(0.5)
#driver.find_element_by_css_selector('#tips_szsy > div > div > div.modal-body > ul > li:nth-child(4) > div > input[type="checkbox"]').click()
#driver.find_element_by_css_selector('#tips_szsy > div > div > div.modal-footer > button').click()
"""                                    
homepage = driver.current_window_handle                                  
ifttt_webhook_url = 'https://maker.ifttt.com/trigger/lottery/with/key/bCG0kCWl8aoNUwJ2ZpBxNz'#d7JFjrAtlKe7ii8-_sQGik
showNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

time.sleep(1)


			


def miandian():
    
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=mdssmpks')")         
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def feilvbin():
            
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=flbssmpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()
    
def jianpuzai():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=jpzyfpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()
    
def xindeli():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=xdlpk10')")
    
def jizhoudao():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=jzdpk10')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def london():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=ldpk10')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def xinbeijing():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=bjpk10')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()
    
def laobeijing():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=lbjpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def xingyunfeiting():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=xxyftpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def xingyunkuaiting():
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=xyktpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()
def xindeliwufencai():
                 
    driver.execute_script("window.open('http://vip1.jygj682.com/trend.html?code=xdlwfpks')")
    #WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()

def choose_code(): 
    windows = driver.window_handles
    for handle in windows:
        if handle != homepage:
            driver.switch_to.window(handle)
               
            #WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#codeList > td:nth-child(2)')))
            #codes_ = driver.find_element_by_css_selector('#codeList > td:nth-child(2)').text
            
            dt3 = datetime.datetime.now()    
            while datetime.datetime.now() - dt3 < datetime.timedelta(seconds=10):
                if driver.find_element_by_css_selector("#body > div.gameCP.game-zs-cen > div.ym-gr > div.xxzs-top > ul > li").text == '重庆时时彩':
                		time.sleep(2)
                		continue                   
                else:
                    break
            
            name = driver.find_element_by_css_selector("#body > div.gameCP.game-zs-cen > div.ym-gr > div.xxzs-top > ul > li").text
            #print(name)   
                                                         
                                                   
            if name == '老北京PK拾':                
                WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()                
                WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="codeList"]/td[1]/table/tbody/tr[50]')))                
                codes_ = driver.find_element_by_css_selector('#codeList > td:nth-child(2)').text
                codes_2 = []
                for i in codes_.split('\n'):
                    codes_2.append(i.split(','))
                lok = np.zeros((50,10),dtype = int)
                for i in range(50):
                    lok[i] = codes_2[i]
                for i in range(0,10):
                    j = 1
                    while j < 51:
                        if lok.T[i][-j] > 5:
                            j += 1
                        else:
                            break
                    if j >= 15:
                        
                        value = ('%s,第%d名,大数连续超过%d轮'%(name,i+1,j-1))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)

                    j = 1
                    while j < 51:
                        if lok.T[i][-j] < 6:
                            j += 1
                        else:
                            break
                    if j >= 15:
                        
                        value = ('%s,第%d名,小数连续超过%d轮'%(name,i+1,j-1))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)

                    j = 1
                    while j < 48:
                        if lok.T[i][-j] != lok.T[i][-j-1] and lok.T[i][-j] != lok.T[i][-j-2] and lok.T[i][-j] != lok.T[i][-j-3]:
                            j += 1
                        else:
                            break
                    if j >= 21:
                        value = ('%s,第%d名,连续%d轮与前三把不重复'%(name,i+1,j-1))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
                    j = 1
                    while j < 50:
                        if lok.T[i][-j] != lok.T[i][-j-1]:
                            j += 1
                            
                        else:
                            key = (name,i+1)
                            if dic.get(key):
                                dic.pop(key)
                                lenth = []
                            break
                                            
                    if j == 50:
                        key = (name,i+1)
                        q = list(driver.find_element_by_xpath('//*[@id="codeList"]/td[1]/table/tbody/tr[50]').text.split())                       
                        dic_b = {key:q}
                        for key in dic_b:
                            if dic.get(key):
                                dic[key] = dic[key] + dic_b[key]
                            else:
                                dic[key] = dic_b[key]
                        lenth_ = len(set(dic[key]))
                        if lenth_ > lenth[-1]:
                            lenth.append(lenth_)                                                                
                            value = ('%s,第%d名,连续%d轮不连出'%(name,i+1,lenth_+49))                        
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    for j in range(19,39):
                        if lok.T[i][-j] not in lok.T[i][-j+1:] and lok.T[i][-j+1] not in lok.T[i][-j+2:] and lok.T[i][-j+2] not in lok.T[i][-j+3:]:
                            key = name,i+1,(lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2])	
                            if key in dic.keys() and j > dic[key]:
                                dic[key] = j	
                                value = ('%s,第%d名,%d轮:%s'%(name,i+1,j-3,[lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2]]))
                                data = {'value1':value}
                                requests.post(ifttt_webhook_url,data)
                            elif key not in dic.keys():
                                dic[key] = j
                        elif (name,i+1,(lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2])) in dic.keys():
                            dic.pop((name,i+1,(lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2])))
                            print(dic)
                                             
                    count_2 = 0
                    count_j = []
                    for j in range(18,51):
                        if lok.T[i][-j] not in lok.T[i][-j+1:]:
                            count_2 += 1
                            count_j.append(j)
                            
                    if count_2 >= 5:
                        value = ('%s,第%d名,已有%d个数遗漏%d轮以上'%(name,i+1,count_2,min(count_j)))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
			
                    for ball in showNumbers:
                        if ball not in lok[i].T:
                            key = (name,i+1,ball)
                            q = driver.find_element_by_xpath('//*[@id="codeList"]/td[1]/table/tbody/tr[50]').text                       
                            if key in dic.keys() and q not in dic[key]:
                                dic[key] = dic[key] + [q]
                                lenth_ = len(dic[key]) 
                                if lenth_ >= 40:                                                             
                                    value = ('%s,第%d名,%s号连续%d轮不出'%(name,i+1,ball,lenth_+50))                       
                                    data = {'value1':value}
                                    requests.post(ifttt_webhook_url,data)
                            elif key not in dic.keys():
                                dic[key] = [q]
			    

                results_ = np.zeros((10,50),dtype = int)
                for i in range(10):
                    results_[i] = (lok.T[i] > 5).astype(int)
                
                for i in range(0,10):
                    j = 1
                    while j < 50 :
                        if results_[i][-j]+results_[i][-j-1] == 1:
                            j += 1
                        else:
                            break
                    if j >= 14:
                        
                        value = ('%s,第%d名,大小相间超过%d轮'%(name,i+1,j))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
                    
                results = np.zeros((10,50),dtype = int)
                for i in range(10):
                    results[i] = (lok.T[i]%2==0).astype(int)
                
                for i in range(0,10):
                    j = 1
                    while j < 50 :
                        if results[i][-j]+results[i][-j-1] == 1:
                            j += 1
                        else:
                            break
                    if j >= 14:
                        
                        value = ('%s,第%d名,单双相间超过%d轮'%(name,i+1,j))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
                        
                    j = 1    
                    while j < 51:
                        if results[i][-j] == 1:
                            j += 1
                        else:
                            break
                    if j >= 15: 
                        
                        value = ('%s,第%d名,双号连续超过%d轮'%(name,i+1,j-1))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
                        
                    j = 1    
                    while j < 51:
                        if results[i][-j] == 0:
                            j += 1
                        else:
                            break
                    if j >= 15:
                                   
                        value = ('%s,第%d名,单号连续超过%d轮'%(name,i+1,j-1))
                        data = {'value1':value}
                        requests.post(ifttt_webhook_url,data)
                                                                                
                driver.close()               
                
            else:
                WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#fifty"))).click()                
                WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="codeList"]/td[1]/table/tbody/tr[50]')))                
                codes_ = driver.find_element_by_css_selector('#codeList > td:nth-child(2)').text
                                               
                codes_2 = []
                for i in codes_.split('\n'):
                    codes_2.append(i.split(','))
                lok = np.zeros((50,10),dtype = int)
                for i in range(50):
                    lok[i] = codes_2[i]
                for i in range(0,10):
                    key = (name,i+1,'big')
                    j = 1
                    while j < 51:
                        if lok.T[i][-j] > 5:
                            j += 1
                        else:	
                            break
                    if j >= 17:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,大数连续超过%d轮'%(name,i+1,j-1))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif key in dic.keys():
                        dic.pop(key)
                        	
                    key = (name,i+1,'small')
                    j = 1
                    while j < 51:
                        if lok.T[i][-j] < 6:
                            j += 1
                        else:
                            break
                    if j >= 17:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,小数连续超过%d轮'%(name,i+1,j-1))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif key in dic.keys():
                        dic.pop(key)

                    key = (name,i+1,'qs')
                    j = 1
                    while j < 48:
                        if lok.T[i][-j] != lok.T[i][-j-1] and lok.T[i][-j] != lok.T[i][-j-2] and lok.T[i][-j] != lok.T[i][-j-3]:
                            j += 1
                        else:
                            break
                    if j >= 20:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,连续%d轮与前三把不重复'%(name,i+1,j-1))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)
                        
                    key = (name,i+1,'lc')
                    j = 1
                    while j < 50:
                        if lok.T[i][-j] != lok.T[i][-j-1]:
                            j += 1
                        else:
                            if dic.get(key):
                                dic.pop(key)
                            break
                    if j == 50:
                        q = driver.find_element_by_xpath('//*[@id="codeList"]/td[1]/table/tbody/tr[50]').text                       
                        if key in dic.keys() and q not in dic[key]:
                            dic[key] = dic[key] + [q]
                            lenth_ = len(dic[key]) 
                            if lenth_ >= 21:                                                             
                                value = ('%s,第%d名,连续%d轮不连出'%(name,i+1,lenth_+49))                        
                                data = {'value1':value}
                                requests.post(ifttt_webhook_url,data)
                        elif key not in dic.keys():
                            dic[key] = [q]
                            lenth_ = len(dic[key])                                                              
                            #value = ('%s,第%d名,连续%d轮不连出'%(name,i+1,lenth_+49))                        
                            #data = {'value1':value}
                            #requests.post(ifttt_webhook_url,data)
                                                                                                       
                    for j in range(25,51):
                        key = name,i+1,(lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2])	
                        if lok.T[i][-j] not in lok.T[i][-j+1:] and lok.T[i][-j+1] not in lok.T[i][-j+2:] and lok.T[i][-j+2] not in lok.T[i][-j+3:]:
                            	
                            if key not in dic.keys():
                                dic[key] = j
                            elif key in dic.keys() and j > dic[key]:
                                dic[key] = j
                                value = ('%s,第%d名,%d轮:%s'%(name,i+1,j-3,[lok.T[i][-j],lok.T[i][-j+1],lok.T[i][-j+2]]))
                                data = {'value1':value}
                                requests.post(ifttt_webhook_url,data)
                                #print(value)
                        elif key in dic.keys():	
                            dic.pop(key)
                            
                    key = (name,i+1,'yl')
                    count_2 = 0
                    count_j = []
                    
                    for j in range(24,51):
                        if lok.T[i][-j] not in lok.T[i][-j+1:]:
                            count_2 += 1
                            count_j.append(j)
                    if count_2 >= 5:
                        if key not in dic.keys():
                            dic[key] = min(count_j)
                        elif key in dic.keys() and min(count_j) > dic[key]:
                            dic[key] = min(count_j)
                            value = ('%s,第%d名,已有%d个数遗漏%d轮以上'%(name,i+1,count_2,min(count_j)))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)
			
                    for ball in showNumbers:
                        if ball not in lok[i].T:
                            key = (name,i+1,ball)
                            q = driver.find_element_by_xpath('//*[@id="codeList"]/td[1]/table/tbody/tr[50]').text                       
                            if key in dic.keys() and q not in dic[key]:
                                dic[key] = dic[key] + [q]
                                lenth_ = len(dic[key]) 
                                if lenth_ >= 40:                                                             
                                    value = ('%s,第%d名,%s号连续%d轮不出'%(name,i+1,ball,lenth_+50))                       
                                    data = {'value1':value}
                                    requests.post(ifttt_webhook_url,data)
                            elif key not in dic.keys():
                                dic[key] = [q]
      
                results_ = np.zeros((10,50),dtype = int)
                for i in range(10):
                    results_[i] = (lok.T[i] > 5).astype(int)
                
                for i in range(0,10):
                    key = (name,i+1,'dx')
                    j = 1
                    while j < 50 :
                        if results_[i][-j]+results_[i][-j-1] == 1:
                            j += 1
                        else:
                            break
                    if j >= 17:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,大小相间超过%d轮'%(name,i+1,j))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)

                results = np.zeros((10,50),dtype = int)
                for i in range(10):
                    results[i] = (lok.T[i]%2==0).astype(int)
                
                for i in range(0,10):
                    key = (name,i+1,'ds')
                    j = 1
                    while j < 50:
                        if results[i][-j]+results[i][-j-1] == 1:
                            j += 1
                        else:
                            break
                    if j >= 16:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,单双相间超过%d轮'%(name,i+1,j))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)	

                    key = (name,i+1,'sh')
                    j = 1
                    while j < 51:
                        if results[i][-j] == 1:
                            j += 1
                        else:
                            break
                    if j >= 17:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,双号连续超过%d轮'%(name,i+1,j-1))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)

                    key = (name,i+1,'dh')
                    j = 1
                    while j < 51:
                        if results[i][-j] == 0:
                            j += 1
                        else:
                            break
                    if j >= 17:
                        if key not in dic.keys():
                            dic[key] = j
                        elif key in dic.keys() and j > dic[key]:
                            dic[key] = j
                            value = ('%s,第%d名,单号连续超过%d轮'%(name,i+1,j-1))
                            data = {'value1':value}
                            requests.post(ifttt_webhook_url,data)
                    elif dic.get(key):
                        dic.pop(key)
                driver.close() 
                                
    driver.switch_to.window(homepage)

parsetimes = 0
dt1 = datetime.datetime.now()-datetime.timedelta(hours=1)
timex = [dt1] 
timel = [dt1]
timew = [dt1]
timef = [dt1]
timek = [dt1]
start_time_bj = datetime.datetime.strptime(str(datetime.datetime.now().date())+'01:25', '%Y-%m-%d%H:%M')
end_time_bj = start_time_bj + datetime.timedelta(hours=14.5)
start_time_f = datetime.datetime.strptime(str(datetime.datetime.now().date())+'5:05', '%Y-%m-%d%H:%M')
end_time_f =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'20:05', '%Y-%m-%d%H:%M')
dic = {}
lenth = []

              
while True:
    parsetimes += 1
    dt2 = datetime.datetime.now()
    print(parsetimes,dt2) 
    if dt2 - timex[-1] > datetime.timedelta(minutes = 5):
        timex.append(dt2)
        requests.get(terminal)       
    try:
        xindeli()
    except:
        print('Exception,pass to next')
        #driver.close()
    try:
        jizhoudao()
    except:
        print('Exception,pass to next')
        driver.close()    
    try:
        london()
    except:
        print('Exception,pass to next')
        driver.close()    
   
    dt2 = datetime.datetime.now()
    if dt2 - timew[-1] > datetime.timedelta(minutes = 2):
        timew[-1] = dt2        
        try:
            xindeliwufencai() 
        except:
            print('Exception,pass to next')
            driver.close()
    dt2 = datetime.datetime.now()
    if dt2 > start_time_f and dt2 < end_time_f or (dt2 > start_time_f + datetime.timedelta(hours=24) and dt2 < end_time_f + datetime.timedelta(hours=24)):
        if dt2 - timek[-1] > datetime.timedelta(minutes = 2):
            timek[-1] = dt2
            try:
                xingyunkuaiting()        
            except:
                print('Exception,pass to next')
                driver.close()
    
    #start_time_bj = datetime.datetime.strptime(str(datetime.datetime.now().date())+'01:25', '%Y-%m-%d%H:%M')                                                    
    dt2 = datetime.datetime.now()
    if dt2 > start_time_bj and dt2 < end_time_bj or (dt2 > start_time_bj + datetime.timedelta(hours=24) and dt2 < end_time_bj + datetime.timedelta(hours=24)):    
        if dt2 - timex[-1] > datetime.timedelta(minutes = 2):
            try:
                xinbeijing()
            except:
                print('Exception,pass to next')
                driver.close()
            try:
                laobeijing()
            except:
                print('Exception,pass to next')
                driver.close()
    time.sleep(3)
                
    try:
        choose_code()
    except:
        print('Exception,pass to next')        
        windows = driver.window_handles
        for handle in windows:
            if handle != homepage:
                driver.switch_to.window(handle)
                driver.close()
                driver.switch_to.window(homepage)
