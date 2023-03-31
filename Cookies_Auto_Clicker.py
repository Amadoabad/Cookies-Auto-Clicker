PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)


driver.get("https://orteil.dashnet.org/cookieclicker/")
try:
    cookie = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "bigCookie")))
    buff0 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "productPrice0")))
    buff1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "productPrice1")))
    buffs = [buff1, buff0]
    for _ in range(2000):
        cookie.click()
        num_of_cookies = int(driver.find_element_by_id("cookies").text.split(" ")[0])
        for buff in buffs:
            if int(buff.text) <= num_of_cookies:
                actions = ActionChains(driver)
                actions.move_to_element(buff).click().perform()
                break
                
finally:
    driver.quit()
