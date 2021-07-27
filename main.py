from selenium import webdriver

driver = webdriver.Firefox(executable_path='driver\geckodriver.exe')
driver.get("https://google.com")