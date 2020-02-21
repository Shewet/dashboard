from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/installed firefox binary')

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title, "Browser title was " + browser.title
browser.quit()