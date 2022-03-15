from selenium import webdriver
import requests
if __name__ == '__main__':
    driver = webdriver.Ie()
　　  page_text=driver.get('http://www.baidu.com')
　　 print(driver.title)
　　  driver.quit()
