import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()


# proxy settings
PROXY = "127.0.0.1:8080"
options.add_argument('--proxy-server=%s' % PROXY)

# browser settings
# options.add_argument("--enable-experimental-web-platform-features")
# prefs = {"block_third_party_cookies": True}
# options.add_experimental_option("prefs", prefs)

# extension settings
# path = "extensions/%s.crx" % "Ghostery"
# options.add_extension(path)


driver = webdriver.Chrome(chrome_options=options)

try:
	# set cookie from 3rd party
	driver.get("http://silence-rain.cn:9888")
	# attack
	driver.get('http://localhost:8888/html/index.html')
	time.sleep(1)

finally:
	driver.close()