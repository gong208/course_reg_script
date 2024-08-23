from time import sleep
from selenium import webdriver
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
success = False
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
while (not success):
    section_open = False
    driver.get("https://courses.illinois.edu/schedule/2024/fall/CS/446")
    driver.refresh()
    while not section_open:
        details = driver.find_element(By.ID, "section-dt").find_element(By.ID, "uid1A")
        for tr in details.find_elements(By.TAG_NAME, "tr"):
            if tr.find_element(By.TAG_NAME, "th").text == "Availability":
                #注意条件
                if tr.find_element(By.TAG_NAME, "td").text != "Closed" and tr.find_element(By.TAG_NAME, "td").text != "UNKNOWN":
                    print("spot spoted at" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    section_open = True
                else:
                    print("no spot at " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                break
        if section_open :
            break
        time.sleep(30)
        driver.refresh()
        
    driver.get("https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/registration?mepCode=1UIUC")

    wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    if EC.number_of_windows_to_be(2):
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                driver.close()
                break
    driver.switch_to.window(original_window)

    need_login = True
    
    # driver.find_element(By.LINK_TEXT , "Registration & Records").click()
    driver.find_element(By.ID , "registerLink").click()
    try:
        driver.find_element(By.ID, "netid").send_keys("[netid]")
        driver.find_element(By.ID, "easpass").send_keys("[password]")
        driver.find_element(By.NAME , "BTN_LOGIN").click()
        driver.implicitly_wait(15)
    except Exception as e:
        print("no login needed")
        need_login = False
    # driver.find_element(By.LINK_TEXT , "Enhanced Registration").click()
    if need_login:
        try:
            driver.find_element(By.ID , "trust-browser-button").click()
        except Exception as e:
            print("no trust browser")
            continue

    # wait.until(EC.number_of_windows_to_be(2))
    # Loop through until we find a new window handle
    for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
    driver.implicitly_wait(2)
    
    wait.until(EC.title_is("Select a Term"))

    driver.find_element(By.ID , "s2id_txt_term").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID , "120248").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID , "term-go").click()
    wait.until(EC.title_is("Registration"))
    registered_hours = driver.find_element(By.ID , "registeredHours").text
    print(registered_hours)
    search_subject = driver.find_element(By.ID , "s2id_txt_subject").find_element(By.TAG_NAME, "input")
    search_subject.send_keys("Computer Science")
    driver.find_element(By.ID , "CS").click()
    search_subject = driver.find_element(By.ID , "txt_courseNumber")
    search_subject.send_keys("446")
    driver.find_element(By.ID , "search-go").click()
    driver.find_element(By.ID , "addSection12024846792").click()
    # driver.implicitly_wait(10)
    # driver.find_element(By.CLASS_NAME , "schedule-class-pending").find_element(By.LINK_TEXT, "**Web Registered**").click()
    # driver.find_element(By.ID , "select2-result-label-22").click()
  
    for i in range(5):
        try:
            driver.find_element(By.ID, "saveButton").click()
        except Exception as e:
            print("registration attempted")
        time.sleep(1)
    

    attempted_hours = driver.find_element(By.ID , "registeredHours").text
    if (registered_hours != attempted_hours):
        print("registered")
        success = True
        driver.quit()
