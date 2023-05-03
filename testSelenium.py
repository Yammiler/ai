from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import createCSV
from selenium.common.exceptions import TimeoutException
import time


# craw data  
def getComment(newdriver):
    
    page_height = newdriver.execute_script("return document.body.scrollHeight")
    
    scroll_step = 800

    # scroll down the page in steps
    for i in range(0, page_height, scroll_step):
        # scroll down to the next step
        newdriver.execute_script(f"window.scrollTo(0, {i});")
        # wait for the page to load
        time.sleep(0.5)
    print()
    comments(newdriver)

def comments(newdriver):
    # lay ra cac comment ve san 
    wait1 = WebDriverWait(newdriver, 10)
    try:
        comments = wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment')))
        #comments = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/main/div[3]/div[4]/div/div[2]/div[3]')
        for comment in comments:
            data = []
            text_data =[]
            name = comment.find_element(By.XPATH, './/div[@class="review-comment__user-name"]')
            content = comment.find_element(By.XPATH, './/div[@class="review-comment__content"]')
            if(content.text != ""):
                data.append(content.text)
                print(name.text + ': ' + content.text)
                time.sleep(2)
                text_data.append(data)
                createCSV.add_data(text_data)      
                data_comment.append(data)               
    except TimeoutException:
        driver.quit()

def item_list(data_comment):
    # danh sach cac item
    listofItems  = driver.find_elements(By.XPATH,'//div[@class="styles__Wrapper-sc-6jfdyd-0 iNsGak"]/a')
    item_url = []

    count_item = 0
    for item in listofItems:
        if count_item == 5:
            break
        url = item.get_attribute("href")        
        item_url.append(url)
        count_item+=1
        print(count_item)
        print(url + "\n\n")
    
    driver.quit()

    for i in range(len(item_url)):
        newdriver = open_driver()
        newdriver.maximize_window()
        newdriver.get(item_url[i])
        print()
        print(item_url[i])
        print()
        time.sleep(1)
        
        getComment(newdriver)
        newdriver.quit()
        
        print(f"san pham {i+1}")
        print("===================================================")

def open_driver():
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    print(driver.execute_script("return navigator.userAgent;"))
    return driver

# Chay chuong trinh
driver = open_driver()

# chay den link 
driver.get('https://tiki.vn/deal-hot?tab=now&from_item=51520770')
# mo toan man hinh cua so
driver.maximize_window()
time.sleep(3)


deals = driver.find_elements(By.XPATH, '//div[@data-view-id="deal_flashdeal_tab"]')

page_height = driver.execute_script("return document.body.scrollHeight")

# set the scroll step
scroll_step = 1000

# scroll down the page in steps
for i in range(0, page_height*12, scroll_step):
    # scroll down to the next step
    driver.execute_script(f"window.scrollTo(0, {i});")
    # wait for the page to load
    time.sleep(1)


data_comment = []
item_list(data_comment)
#data_log = [[s.strim().replace('\n','') for s in sub_list] for sub_list in data_comment]
#createCSV.write_data(data_comment)

