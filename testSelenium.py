from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import createCSV 
import time


# craw data  
def getComment(driver,data_comment):

    # do dai cua trang
    page_height = driver.execute_script("return document.body.scrollHeight")
    data = []
    # set the scroll step
    scroll_step = 800

    # scroll down the page in steps
    for i in range(0, page_height, scroll_step):
        # scroll down to the next step
        driver.execute_script(f"window.scrollTo(0, {i});")
        # wait for the page to load
        time.sleep(0.5)
    
    wait = WebDriverWait(driver, 15)

    # lay ten thuong hieu + san pham
    brand = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[1]/div[1]/span/h6/a').text
    brand_title = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div[1]/div[3]/div[1]/h1').text
    print("Thuong Hieu: "+brand+" - "+brand_title)
    print()


    # lay ra cac comment ve san pham
    comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment')))

    for comment in comments:
        data = []
        name = comment.find_element(By.XPATH, './/div[@class="review-comment__user-name"]')
        content = comment.find_element(By.XPATH, './/div[@class="review-comment__content"]')
        if(content.text != ""):
            data.append(content.text)
            print(name.text + ': ' + content.text)
            time.sleep(2)
            data_comment.append(data)
    return data_comment

def item_list(data_comment):
    # danh sach cac item
    listofItems  = driver.find_elements(By.XPATH,'//div[@class="styles__Wrapper-sc-6jfdyd-0 iNsGak"]/a')
    item_url = []

    count_item = 0;
    for item in listofItems:
        if count_item == 5:
            break
        url = item.get_attribute("href")
        check_item = item.find_element(By.XPATH ,'//p[@class="text"]').text;
        time.sleep(0.5)
        #if(check_item!="Vừa mở bán"):
        item_url.append(url)
        count_item+=1
        print(url + "\n\n")

    for i in range(len(item_url)):
        if(i!=1):
            driver.get(item_url[i])
            data_comment=getComment(driver ,data_comment)
            print("===================================================")
    return data_comment


# Chay chuong trinh
driver = webdriver.Chrome()

# chay den link 
driver.get('https://tiki.vn/deal-hot?tab=now&from_item=55506687')
# mo toan man hinh cua so
driver.maximize_window()
time.sleep(5)


deals = driver.find_elements(By.XPATH, '//div[@data-view-id="deal_flashdeal_tab"]')

page_height = driver.execute_script("return document.body.scrollHeight")

# set the scroll step
scroll_step = 500

# scroll down the page in steps
for i in range(0, page_height, scroll_step):
    # scroll down to the next step
    driver.execute_script(f"window.scrollTo(0, {i});")
    # wait for the page to load
    time.sleep(0.5)


data_comment = []
data_comment = item_list(data_comment)

createCSV.write_data(data_comment)

time.sleep(20)
# close the driver
driver.quit()
