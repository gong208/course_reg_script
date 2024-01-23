from time import sleep
from selenium import webdriver
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
section_open = False
driver.get("https://courses.illinois.edu/schedule/2024/spring/CS/357")
driver.refresh()
while not section_open:

    details = driver.find_element(By.ID, "section-dt").find_element(By.ID, "uid3A")
    for tr in details.find_elements(By.TAG_NAME, "tr"):
        if tr.find_element(By.TAG_NAME, "th").text == "Availability":
            #注意条件
            if tr.find_element(By.TAG_NAME, "td").text == "Closed":
                print("spot spoted")
                section_open = True
            break
    if section_open :
        break
    time.sleep(30)
    driver.refresh()
    
driver.get("https://login.uillinois.edu/auth/SystemLogin/sm_login.fcc?TYPE=33554433&REALMOID=06-a655cb7c-58d0-4028-b49f-79a4f5c6dd58&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-dr9Cn7JnD4pZ%2fX9Y7a9FAQedR3gjL8aBVPXnJiLeXLOpk38WGJuo%2fOQRlFkbatU7C%2b9kHQgeqhK7gmsMW81KnMmzfZ3v0paM&TARGET=-SM-HTTPS%3a%2f%2fwebprod%2eadmin%2euillinois%2eedu%2fssa%2fservlet%2fSelfServiceLogin%3fappName%3dedu%2euillinois%2eaits%2eSelfServiceLogin%26dad%3dBANPROD1")

wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle
driver.find_element(By.ID, "netid").send_keys("[netid]")
driver.find_element(By.ID, "easpass").send_keys("[pswd]")
driver.find_element(By.NAME , "BTN_LOGIN").click()
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT , "Registration & Records").click()
driver.find_element(By.LINK_TEXT , "Enhanced Registration").click()
wait.until(EC.number_of_windows_to_be(2))
# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

driver.find_element(By.ID , "registerLink").click()
wait.until(EC.title_is("Select a Term"))
driver.implicitly_wait(2)
driver.find_element(By.ID , "s2id_txt_term").click()
driver.implicitly_wait(2)
driver.find_element(By.ID , "120241").click()
driver.find_element(By.ID , "term-go").click()
wait.until(EC.title_is("Registration"))
search_subject = driver.find_element(By.ID , "s2id_txt_subject").find_element(By.TAG_NAME, "input")
search_subject.send_keys("Computer Science")
driver.find_element(By.ID , "CS").click()
search_subject = driver.find_element(By.ID , "txt_courseNumber")
search_subject.send_keys("357")
driver.find_element(By.ID , "search-go").click()
driver.find_element(By.ID , "addSection12024150106").click()
# driver.implicitly_wait(10)
# driver.find_element(By.CLASS_NAME , "schedule-class-pending").find_element(By.LINK_TEXT, "**Web Registered**").click()
# driver.find_element(By.ID , "select2-result-label-22").click()

for i in range(5):
    driver.find_element(By.ID, "saveButton").click()
    time.sleep(1)