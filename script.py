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
driver.get("https://courses.illinois.edu/schedule/2024/spring/CS/222")
driver.refresh()
while not section_open:

    details = driver.find_element(By.ID, "section-dt").find_element(By.ID, "uid1A")
    for tr in details.find_elements(By.TAG_NAME, "tr"):
        if tr.find_element(By.TAG_NAME, "th").text == "Availability":
            #注意条件
            if tr.find_element(By.TAG_NAME, "td").text != "Closed":
                print("success")
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
driver.find_element(By.ID, "easpass").send_keys("[password]")
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
search_subject = driver.find_element(By.ID , "s2id_autogen7")
search_subject.send_keys("Computer Science")
driver.find_element(By.ID , "CS").click()
search_subject = driver.find_element(By.ID , "txt_courseNumber")
search_subject.send_keys("222")
driver.find_element(By.ID , "search-go").click()
driver.find_element(By.ID , "addSection12024171617").click()
# driver.implicitly_wait(10)
# driver.find_element(By.CLASS_NAME , "schedule-class-pending").find_element(By.LINK_TEXT, "**Web Registered**").click()
# driver.find_element(By.ID , "select2-result-label-22").click()
for i in range(10):
    driver.find_element(By.ID, "saveButton").click()
    time.sleep(1)
# search_subject = driver.find_element(By.CLASS_NAME, "odd")
# # 添加UA
# chrome_options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')

# # 指定浏览器分辨率
# chrome_options.add_argument('window-size=480, 800') 

# # 谷歌文档提到需要加上这个属性来规避bug
# chrome_options.add_argument('--disable-gpu') 

#  # 隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('--hide-scrollbars')

# # 不加载图片, 提升速度
# chrome_options.add_argument('blink-settings=imagesEnabled=false') 

# # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# chrome_options.add_argument('--headless') 

# # 以最高权限运行
# chrome_options.add_argument('--no-sandbox')

# # 手动指定使用的浏览器位置
# chrome_options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" 

# #添加crx插件
# chrome_options.add_extension('d:\crx\AdBlock_v2.17.crx') 

# # 禁用JavaScript
# chrome_options.add_argument("--disable-javascript") 

# # 设置开发者模式启动，该模式下webdriver属性为正常值
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) 

# # 禁用浏览器弹窗
# prefs = {  
#     'profile.default_content_setting_values' :  {  
#         'notifications' : 2  
#      }  
# }  
# chrome_options.add_experimental_option('prefs',prefs)


# driver=webdriver.Chrome(chrome_options=chrome_options)
