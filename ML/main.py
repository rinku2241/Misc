import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import pandas as pd
import json

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

page = "https://collegedunia.com/usa/college/1090-harvard-university-cambridge"


# driver = webdriver.Chrome('C:/Users/DaeMon/Downloads/chromedriver_win32/chromedriver.exe')
response= requests.get(page, headers=headers)
html= response.content

# driver.get(page) 
# pagecontent= driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#Title of what we looking for 
Kind= soup.find('h1', class_="jsx-4139948154 text-white font-weight-bolder mt-0 mb-1 text-lg").text

#Harvard University fees and Deadlines
Fee_Dates= soup.find("tbody", class_="jsx-4276038191").find_all("tr", class_="jsx-4276038191")
list_of_Programs= []  
for fd in Fee_Dates:
    Programs= fd.find("a", class_="jsx-4276038191").get_text()
    AppDeadline= fd.find("div", class_="jsx-4276038191 mb-1").get_text()
    Fees= fd.find('div', class_="jsx-4276038191 text-secondary text-sm mt-1 text-silver").get_text()
    ProgramDetail={
      "Program Nmae":Programs,
      "Deadline For the Programa":AppDeadline,
      "Fees of The Program":Fees
    }
    list_of_Programs.append(ProgramDetail)
      # convert it to a json add it to a file
    with open('data.json', 'w') as f:     
        json.dump(list_of_Programs, f)
# print(list_of_Programs)

    

   
    









