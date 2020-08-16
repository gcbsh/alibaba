from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

time.sleep(3)
#单元素定位
# driver.find_element_by_id("")
# driver.find_element_by_name("")
# driver.find_element_by_class_name("")
# driver.find_element_by_tag_name("")#标签名称
# driver.find_element_by_link_text()#链接标签全部
# driver.find_element_by_partial_link_text("")#链接标签包含
# driver.find_element_by_xpath("//name[@id='']")#相对路径
# driver.find_element_by_css_selector("")
# 多元素定位
#driver.find_elements


driver.quit()