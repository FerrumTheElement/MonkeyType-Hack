from selenium import webdriver
from bs4 import BeautifulSoup
import time
import keyboard as kb
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--log-level=3') # prevents an overload of logs in the terminal
driver = webdriver.Chrome(options)
driver.get("https://monkeytype.com")
print("Connection Established...")

global h

def ask():
    
    global timedelay
    global timer
    timer = int(input("How long will this be running for?: "))
    timedelay = float(input("What will be the time interval for each letter?: "))

def again():
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
           
    s = soup.findAll("div", class_="word") # all letters are in a class "word"
   
    s = str(s)
    a = s.replace('<letter>', "")
    b = a.replace('</letter>', "")
    c = b.replace('<div class="word active">', "")
    d = c.replace('</div>', "")
    e = d.replace('<div class="word">', "")
    f = e.replace(',', "")
    g = f.replace('[', "")
    h = g.replace(']', "")
    return h

def function():
    while True:
        if kb.is_pressed("ctrl"):
            time.sleep(1)
            h = again()
            
            print("Typing...")

            lengthcheck = 0
            start_time = time.time()
            while True:
                    
                while lengthcheck <= len(h):
                    
                    if lengthcheck == len(h):
                        
                        h = again()
                        
                        while h.find('<letter class="correct">') != -1:
                            g = h.find('<letter class="correct">')
                            text1 = g+25
                            h = h.replace(h[0:text1], '')
                            lengthcheck = 0
                            
                            
                    elapsed_time = (time.time() - start_time)
                      
                    if elapsed_time > timer:
                        print("Typing has been finished")
                        function() 
                    
                    if lengthcheck < len(h):
                        kb.write(h[0+lengthcheck])
                        time.sleep(timedelay)
                        lengthcheck += 1
                break
            
        if kb.is_pressed("-"):
            ask()

ask()
function()
