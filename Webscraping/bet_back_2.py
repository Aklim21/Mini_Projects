'''
akj betfair session token: Eb+29d6GXZpmuVEWX/UQWxYZy3My7JCsae4bwNqSZnk=

'''
#####################################################


#bet backing

################  Background ########################
'''
- Bookie provides back odds
- Exchange provides lay odds 

- Backing bet is via bookie
- Lay is through exchange

- Winning the back is more optimal since you dont pay commision

- If the lay wins you pay commision to the exchange
  
  '''
############### Components  ##################
'''
- Web scraper component for data

- Registered list of bookies to scrape for back:
    - betfred 
    - future  functionality will be to be able to add or remove bookies.

    ############## Achieved #################
- Registered list of exchanges to scrape for lay
(betfair provides best functionality. Stick with this one) 


'''
############### Tasks  ##################

'''

- Locate most profitable exchange rate across bet exchanges
    ---> define bet threshold variable
    --> back/ lay % --> favour higher percentage 


- Review bet odds across number of bookies to locate best return rate on back bet
    ---> define comparison function 
    

- - Review bet odds across number of exchanges to locate best lay rate
    ---> recycle comparison function above
    NOTE: sceptical on this step since this requires 



- Manual confirmation to accept/ reject bet

'''


#####################  Setting up the exchange requests  ###############################
'''

info link: https://docs.developer.betfair.com/visualisers/api-ng-account-operations/

akj betfair session token: Eb+29d6GXZpmuVEWX/UQWxYZy3My7JCsae4bwNqSZnk=

app name: bfx_demo
app id: 90060


delay request:
version id: 84164
1.0-DELAY
app key: estob1vxvcr0eWYM
owner: anthonyjim@live.co.uk
active: Yes

 
 
demo request:
version id: 84163 
1.0
app key: aERcuMG6e8kfyQGy
owner: anthonyjim@live.co.uk
active: No


'''

##########################################################################################

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pprint as pp
from selenium import webdriver



BETFAIR_URL = "https://www.betfair.com/exchange/plus/en/football-betting-1"

#functions
def parse(url):
    
    driver = webdriver.Chrome(r'C:\Users\antho\Downloads\chromedriver.exe')
    driver.get(url)
    try:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR ,"span.bet-button-price"))) 

    except:
        pp.pprint("Exception")

    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
        driver.quit()


    return soup

soup = parse(BETFAIR_URL)

match_name = soup.find_all("ul", class_="runners")
#team_name = match_name.find("ul", class_="title")   <-- cant run find on these since its returned a string, not html object
match_container = soup.find_all("td", class_="coupon-runners")
#match_bet = match_container.find("button", class_="bf-bet-button back-button back-selection-button")

print(team_name[0],match_bet[0])