from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
import math
import sys

def find_first():
    sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    Box_First1 = soup.find("li", id="episode_1")
    Box_First2 = soup.find("li", id="episode_2")
    pages = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="paginate"]/a')))
    len_pages = len(pages)
    #print(len_pages)
    pages[len_pages-1].click()
    if(Box_First1 or Box_First2):
        return 0
    else:
        find_first()


options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_driver_path = '/usr/local/bin/chromedriver' 
# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get('https://www.webtoons.com/en/originals#completed')
wait = WebDriverWait(driver, 10)  # 10 seconds timeout

toons = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="daily_lst comp"]/div/ul/li')))
sleep(2)

toons_Category = []
toons_Name = []
toons_Author = []
toons_Synopsis = []

toons_Read_Number = []
toons_Subscribe_Number = []
toons_Rate_Number = []

toons_Date_First = []
toons_Like_First = []
loop = 0

for i in range((math.floor(len(toons)/10)) * int (sys.argv[1]) , len(toons)-(math.floor(len(toons)/10)) * int (sys.argv[2]) ):

    driver.execute_script("arguments[0].scrollIntoView(true);", toons[i])  # **Scroll into view**
    WebDriverWait(driver, 10).until(EC.visibility_of(toons[i]))  # **Wait for visibility**

    toons[i].click()  # **Normal click**
  
  
    find_first()

    Category = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="info"]/h2')))
    Name = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="info"]/h1')))
    Author = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="info"]/div')))
    Synopsis = wait.until(EC.presence_of_element_located((By.XPATH,'//p[@class="summary"]')))

    Read_Number = wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="grade_area"]/li[1]')))
    Subscribe_Number = wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="grade_area"]/li[2]')))
    Rate_Number = wait.until(EC.presence_of_element_located((By.XPATH,'//ul[@class="grade_area"]/li[3]')))

    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    Date_First_Check = soup.find("li", id="episode_1")
    if(Date_First_Check):
        Date_First = wait.until(EC.presence_of_element_located((By.XPATH,'//li[@id="episode_1"]/a/span[4 ]')))
        Like_First = wait.until(EC.presence_of_element_located((By.XPATH,'//li[@id="episode_1"]/a/span[5]')))
    else:
        Date_First = wait.until(EC.presence_of_element_located((By.XPATH,'//li[@id="episode_2"]/a/span[4]')))
        Like_First = wait.until(EC.presence_of_element_located((By.XPATH,'//li[@id="episode_2"]/a/span[5]')))

    #print(Category.text)
    toons_Category.append(Category.text)
    #print(Name.text)
    toons_Name.append(Name.text)
    #print(Author.text)
    toons_Author.append(Author.text)
    #print(Synopsis.text)
    toons_Synopsis.append(Synopsis.text)

    #print(Read_Number.text)
    toons_Read_Number.append(Read_Number.text)
    #print(Subscribe_Number.text)
    toons_Subscribe_Number.append(Subscribe_Number.text)
    #print(Rate_Number.text)
    toons_Rate_Number.append(Rate_Number.text)

    #print(Date_First.text)
    toons_Date_First.append(Date_First.text)
    #print(Like_First.text)
    toons_Like_First.append(Like_First.text)
    # driver.back()
    driver.get('https://www.webtoons.com/en/originals#completed')
    wait = WebDriverWait(driver, 2) 
    toons = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="daily_lst comp"]/div/ul/li')))
    loop+=1
    # print("{}...".format(loop))

driver.quit()
print("End of process...")

column_values = ['Category','Name','Author','Synopsis','Read_Number','Subscribe_Number','Rate_Number','Date_First','Like_First']

data = {
    'Category':toons_Category,
    'Name':toons_Name,
    'Author':toons_Author,
    'Synopsis':toons_Synopsis,
    'Read_Number':toons_Read_Number,
    'Subscribe_Number':toons_Subscribe_Number,
    'Rate_Number':toons_Rate_Number,
    'Date_First':toons_Date_First,
    'Like_First':toons_Like_First
}

df= pd.DataFrame(data)
# pd.set_option('display.max_columns', None)
print(df)
df.to_csv(f'data{sys.argv[1]}.csv', index=False)  # Save to the mounted directory

