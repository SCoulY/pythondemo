from selenium import webdriver  #导入Selenium的webdriver
from selenium.webdriver.common.keys import Keys  #导入Keys
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
prefs = {"profile.managed_default_content_settings.images":2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(executable_path=r'D:\CHROME DOWNLOAD\chromedriver_win32\chromedriver.exe')  #指定使用的浏览器，初始化webdriver
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://translate.google.cn/m/translate#en/zh-CN/you")  #请求网页地址
time.sleep(3)
# try:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'translation').text))
# finally:
#     driver.quit()
print(driver.find_element(By.CLASS_NAME,'translation').text)
driver.close()  #关闭webdriver
