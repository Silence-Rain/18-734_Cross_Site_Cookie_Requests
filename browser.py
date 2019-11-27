import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()

PROXY = "127.0.0.1:8080"

options.add_argument('--proxy-server=%s' % PROXY)
options.add_argument("--enable-experimental-web-platform-features")
prefs = {"block_third_party_cookies": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)

try:
	driver.get('http://localhost:8888/set_cookie.html')
	#driver.add_cookie({"name": "test", "value": "haha", "domain": "www.google.com"})
	driver.get('http://localhost:8888/html/index.html')
	time.sleep(5)
	print(driver.get_cookies())

finally:
	driver.close()