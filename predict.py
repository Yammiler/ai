from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import createCSV
from selenium.common.exceptions import TimeoutException
import time



# craw data  
def getComment(driver):
    
    page_height = driver.execute_script("return document.body.scrollHeight")
    
    scroll_step = 800

    # scroll down the page in steps
    for i in range(0, page_height, scroll_step):
        # scroll down to the next step
        driver.execute_script(f"window.scrollTo(0, {i});")
        # wait for the page to load
        time.sleep(0.5)
    print()
    data = comments(driver)
    return data

def comments(driver):
    data_comment = []
    # lay ra cac comment ve san 
    wait1 = WebDriverWait(driver, 10)
    try:
        comments = wait1.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment')))
        #comments = driver.find_elements(By.XPATH,'/html/body/div[1]/div[1]/main/div[3]/div[4]/div/div[2]/div[3]')
        for comment in comments:
            name = comment.find_element(By.XPATH, './/div[@class="review-comment__user-name"]')
            content = comment.find_element(By.XPATH, './/div[@class="review-comment__content"]')
            if(content.text != ""):
                print(name.text + ': ' + content.text)
                time.sleep(2)   
                data_comment.append(content.text) 
        return data_comment
    except TimeoutException:
        driver.quit()
        
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


def list_data_comment(link):
    driver = open_driver()
    # chay den link 
    driver.get(link)
    # mo toan man hinh cua so
    driver.maximize_window()
    time.sleep(3)


    deals = driver.find_elements(By.XPATH, '//div[@data-view-id="deal_flashdeal_tab"]')
    data_comment = getComment(driver)
    # print('=================================')
    # print(data_comment)
    return data_comment


