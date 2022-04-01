from selenium import webdriver

chrome_browser = webdriver.Chrome('/Users/jmichalek/Downloads/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

print('Selenium Easy Demo - Simple Form to Automate using Selenium' in chrome_browser.title)