import time
from selenium import webdriver


# Chrome
# options = webdriver.ChromeOptions()

# # proxy settings
# PROXY = "127.0.0.1:8080"
# options.add_argument('--proxy-server=%s' % PROXY)

# # browser settings
# # options.add_argument("--enable-experimental-web-platform-features")
# # prefs = {"block_third_party_cookies": True}
# # options.add_experimental_option("prefs", prefs)

# # extension settings
# # path = "extensions/%s.crx" % "Ghostery"
# # options.add_extension(path)

# driver = webdriver.Chrome(chrome_options=options)


# Firefox
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.http", "localhost")
profile.set_preference("network.proxy.http_port", 8080)
profile.set_preference("network.proxy.type", 1)
profile.set_preference("security.csp.enable", True)

# profile.set_preference("network.cookie.cookieBehavior", 1)

profile.update_preferences()

driver = webdriver.Firefox(firefox_profile=profile)




# set cookie from 3rd party
driver.get("http://silence-rain.cn:9888")
# attack
driver.get('http://localhost:8888/html/index.html')
time.sleep(1)


driver.close()