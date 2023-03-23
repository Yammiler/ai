# AI_HUS_2023_EEI
First time to use

<h1> demo lấy dữ liệu bằng selenium</h1>
https://user-images.githubusercontent.com/92799704/226243896-b7ec4d18-8eaa-4099-81fa-f291f846b76c.mp4

<h2>Đoạn code lấy comment về</h2>
```python
   ```
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
    data_header.append(brand)
    print("Thuong Hieu: "+brand+" - "+brand_title)
    print()


    # lay ra cac comment ve san pham
    comments = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.review-comment')))

    for comment in comments:
        name = comment.find_element(By.XPATH, './/div[@class="review-comment__user-name"]')
        content = comment.find_element(By.XPATH, './/div[@class="review-comment__content"]')
        data.append(content.text)
        print(name.text + ': ' + content.text)
        print()
        time.sleep(2)
    data_comment.append(data)
    return data_header,data_comment
    ```
```
