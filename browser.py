import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = webdriver.ChromeOptions()

chromeOptions.add_argument("--enable-experimental-web-platform-features")
prefs = {"block_third_party_cookies": True}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

try:
	driver.get('https://www.cnn.com')
	time.sleep(5)
	cookies = driver.get_cookies()
	for i in cookies:
		print(i)
finally:
	driver.close()

