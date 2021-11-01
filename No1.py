from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(r'F:\test1904A\gao5\chromedriver.exe')
driver.get("https://www.baidu.com/")
sleep(2)
driver.find_element_by_id('s-top-loginbtn').click()
# driver.find_element_by_id("kw").send_keys("Linux及MySQL")
# sleep(2)
# driver.find_element_by_id("su").click()
sleep(2)
driver.quit()
