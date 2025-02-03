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

def ask():
    #global declartaions
    global timedelay
    global timer
    timer = int(input("How long will this be running for?: "))
    timedelay = float(input("What will be the time interval for each letter?: "))
    print("Press ctrl to start the program\n")
    

def format():
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
           
    s = soup.findAll("div", class_="word") # all letters are in a class "word"
    s = str(s)
    s = s.replace('<letter>', "")
    s = s.replace('</letter>', "")
    s = s.replace('<div class="word active">', "")
    s = s.replace('</div>', "")
    s = s.replace('<div class="word">', "")
    s = s.replace(',', "")
    s = s.replace('''[''', "")
    s = s.replace(''']''', "")
    
    return s
 
def main():
        time.sleep(1)
        h = format()
        start_time = time.time()
        #declarations
        lengthcheck = 0
        elapsed_time = 0

        while elapsed_time < timer:
            elapsed_time = (time.time() - start_time)
            if lengthcheck == len(h):          
                h = format()
                #corrects for the offset <letter> makes
                while h.find('<letter class="correct">') != -1:
                    g = h.find('<letter class="correct">')
                    text1 = g+25
                    h = h.replace(h[0:text1], '')
                    lengthcheck = 0
                        
            if lengthcheck < len(h):
                kb.write(h[0+lengthcheck]) #writes letter by letter
                time.sleep(timedelay)
                lengthcheck += 1
            
           
while True:

    if kb.is_pressed("-"): #press '-' to change typer settings
        ask()
    if kb.is_pressed("ctrl"):
        main()
    
    
         
     
            
            


