from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pprint as pp
from selenium import webdriver



URL = "https://www.amazon.co.uk/gp/product/B086ZF2DVN/ref=ox_sc_act_title_1?smid=A6V038ILD1K3T&psc=1"

#functions
def parse(url):
    
    driver = webdriver.Chrome(r'C:\Users\antho\Downloads\chromedriver.exe')
    driver.get(url)
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR , "id"))) 

    except:
        pp.pprint("Exception")

    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
        driver.quit()


    return soup

soup = parse(URL)

# match_name = soup.find_all("ul", class_="runners")
# #team_name = match_name.find("ul", class_="title")   <-- cant run find on these since its returned a string, not html object
# match_container = soup.find_all("td", class_="coupon-runners")
# #match_bet = match_container.find("button", class_="bf-bet-button back-button back-selection-button")

print(soup.prettify())




#for price use [:-3] to get the value, remove the last three digits and strip any symbols. 

