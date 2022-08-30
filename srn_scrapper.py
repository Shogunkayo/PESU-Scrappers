import sys
import csv
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
driver.get("https://www.pesuacademy.com/Academy/")

driver.implicitly_wait(15)
os.system('cls' if os.name == 'nt' else 'clear')


def process(data):
    data = data.split()

    info = [data[0],data[1],data[1][8]+data[1][9]]

    if(data[1][3] == "1"):
        info.append("RR")
    else:
        info.append("EC")
     
    info.append("".join(([i for i in data if i.startswith("Sem")])))
    info.append(data[data.index("Section") + 1])

    name = []
    for i in data[2:]:
        if(i.startswith("Sem")):
            break
        name.append(i)
    info.append("-".join(name))
    
    return info
    
def scrape(srn):
    know_button = driver.find_element(By.XPATH, "//a[@id='knowClsSection']")
    know_button.click()
    
    text_box = driver.find_element(By.XPATH, "//input[@id='knowClsSectionModalLoginId']")
    text_box.send_keys(srn)

    search_button = driver.find_element(By.XPATH, "//button[@id='knowClsSectionModalSearch']")
    search_button.click()

    try:
        data = driver.find_element(By.XPATH, "//tbody[@id='knowClsSectionModalTableDate']/tr").text
        info = process(data)
    except Exception as e:
        print(e)
        info = ["NA",srn,"NA","NA","NA","NA","NA"]

    close_button = driver.find_element(By.XPATH, "//div[@id='knowClsSectionModal']//button[@class='btn btn-default']")
    close_button.click()
    
    return info

def return_srn_num(i):
    if i < 10:
        num = "00" + str(i)
    elif 9<i<100:
        num = "0" + str(i)
    else:
        num = str(i)
    
    return num

def return_prn_num(i):
    if i < 10:
        num = "0000" + str(i)
    elif 9<i<100:
        num = "000" + str(i)
    elif 99<i<1000:
        num = "00" + str(i)
    else:
        num = "0" + str(i)

    return num


if(sys.argv[1] == "1"):
    print(scrape(sys.argv[2]))

elif(sys.argv[1] == "2"):
    with open(sys.argv[2]+"_"+sys.argv[3], "w") as file:
        csv_writer = csv.writer(file)
        
        size = 400;
        ended = 0;
        if(sys.argv[2] == "CS" and sys.argv[3] == "1"):
            size = 800;
        
        for i in range(1,size):
            srn = "PES"+sys.argv[4]+"UG"+sys.argv[3]+sys.argv[2]+return_srn_num(i)
            print("Scraping ",srn)
            
            details = scrape(srn)
            if(details[0]=="NA"):
                ended += 1
            else:
                ended = 0
            if(ended == 15):
                break
            
            csv_writer.writerow(details)
            sleep(10)

elif(sys.argv[1] == "3"):
    with open("Year_"+sys.argv[2]+"_"+sys.argv[3], "w") as file:
        csv_writer = csv.writer(file)
        
        size = 3500
        ended = 0;
        
        for i in range(1,size):
            prn = "PES"+sys.argv[3]+sys.argv[2]+return_prn_num(i)
            print("Scraping ",prn)
            
            details = scrape(prn)
            if(details[0]=="NA"):
                ended += 1
            else:
                ended = 0
            if(ended == 30):
                break

            csv_writer.writerow(details)
            sleep(20)

else:
    print("Invalid arugements. Please see the readme.md file")


#--------------- ARGUEMENTS
#
#   1 - Scrape a single srn and print the details, 
#       python3 file.py 1 [srn]
#   
#   2 - Scrape a branch and write the details to a csv file,
#       python3 file.py 2 [branch] [year in YY format] [campus_code]
#       
#   3 - Scrape a particular year,
#       python3 file.py 3 [year in YYYY format] [campus_code]
#   
#   Campus Code-
#   1 - RR Campus
#   2 - EC Campus
#   
#   Branches- 
#   CS - Computer Science 
#   EC - Electronics 
#   EE - Electrical 
#   ME - Mechanical 
#   BT - Biotech
#   BB - BBA
#   AL - BBA-LLB
#   BL - BBA-LLB
#   BA - Architecture
#   BD - Design
#   MB - MBA
