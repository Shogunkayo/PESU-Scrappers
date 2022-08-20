from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import csv
import time


PATH = "/home/pyr0/Code/Python/Modules/chromedriver.exe"
driver = webdriver.Chrome(service=Service(PATH))
driver.implicitly_wait(15)


# CHOOSE WHICH BATCH TO SCRAPE HERE
campus = "1"
year = "21"
branch = "CS"


srn = []

if branch == "CS":
    size = 800
else:
    size = 400

for i in range(1,size):
    if i < 10:
        num = "00" + str(i)
    elif 9<i<10:
        num = "0" + str(i)
    else:
        num = str(i)
    srn.append("PES"+campus+"UG"+year+branch+num)

def open_info():
    driver.get("https://www.pesuacademy.com/")

def get_info(srn):    
    try: 
        button = driver.find_element(By.ID, "knowClsSection")
        button.click()
        
        textbox = driver.find_element(By.ID, "knowClsSectionModalLoginId")
        textbox.send_keys(srn)

        search_button = driver.find_element(By.ID, "knowClsSectionModalSearch")
        search_button.click()

        scrape =  driver.find_element(By.ID,"knowClsSectionModalTableDate") 
        details = scrape.text.split()
        prn = details[0]
        srn_verify = details[1]
        section = details[details.index("Section") + 1] + " Section"
        
        try:
            cycle = details[details.index("Cycle") - 1] + " Cycle"
        except:
            cycle = "NA"

        name = []
        b = False

        for i in range(2,len(details)):
            for j in range(1,9):
                if details[i] == "Sem-" + str(j):
                    b = True
                    sem = details[i]
            if(b):
                break   
            name.append(details[i])
    except:
        prn = name = sem = section = cycle = "NA"
        srn_verify = srn
    
    textbox.send_keys(Keys.ESCAPE)
    
    print(prn,srn_verify,name,sem,section,cycle)
    return prn,srn_verify,name,sem,section,cycle

def store_info(branch,campus):
    with open(branch+"-"+campus+".csv", "a+") as file:
        for i in srn:
            details = get_info(i)
            writer = csv.writer(file)
            writer.writerow(details)
            time.sleep(10)

open_info()
store_info(branch,campus)


