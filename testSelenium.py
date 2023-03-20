from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def getComment(driver):

    height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, " + str(i+2300) + ");")
    
    wait = WebDriverWait(driver, 15)
    comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment')))

    for comment in comments:
        name = comment.find_element(By.XPATH, './/div[@class="review-comment__user-name"]')
        content = comment.find_element(By.XPATH, './/div[@class="review-comment__content"]')
        print(name.text + ': ' + content.text)
        print()
        time.sleep(2)

def start_page(driver):
    driver.get('https://tiki.vn/deal-hot?tab=now&from_item=191808923')
    time.sleep(5)

    deal_49k = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[3]/div/div/div/div/div[5]/div/div')
    deal_49k.click()
    time.sleep(5)

driver = webdriver.Chrome()
start_page(driver)

# danh sach cac item
listofItems  = driver.find_elements(By.XPATH,'//div[@class="styles__Wrapper-sc-6jfdyd-0 iNsGak"]/a')
item_url = []


for item in listofItems:
    url = item.get_attribute("href")
    check_item = item.find_element(By.XPATH ,'//p[@class="text"]').text;
    time.sleep(0.5)
    if(check_item!="Vừa mở bán"):
        item_url.append(url)
        print(url + "\n\n")


for i in range(len(item_url)):
    if(i!=1):
        driver.get(item_url[i])
        getComment(driver)
        print("===================================================")


time.sleep(20)
# close the driver
driver.quit()
