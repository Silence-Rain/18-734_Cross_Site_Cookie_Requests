import time
from selenium import webdriver

extensions = ["AdBlockPlus", "Adguard", "uBlockOrigin", "Ghostery", "PrivacyBadger"]
attacks = ["html", "redirect", "js", "pdf", "headers"]

# Chrome
options = webdriver.ChromeOptions()

# proxy settings
PROXY = "127.0.0.1:8080"
options.add_argument('--proxy-server=%s' % PROXY)

# browser settings
# options.add_argument("--enable-experimental-web-platform-features")
# prefs = {"block_third_party_cookies": True}
# options.add_experimental_option("prefs", prefs)

# extension settings
path = "extensions/chrome/%s.crx" % extensions[3]
options.add_extension(path)

driver = webdriver.Chrome(chrome_options=options)

# # Firefox
# profile = webdriver.FirefoxProfile()

# # proxy settings
# profile.set_preference("network.proxy.http", "localhost")
# profile.set_preference("network.proxy.http_port", 8080)
# profile.set_preference("network.proxy.type", 1)
# profile.set_preference("security.csp.enable", True)

# # browser settings
# # profile.set_preference("network.cookie.cookieBehavior", 1)
# # profile.set_preference("privacy.trackingprotection.enabled", 1)

# # extension settings
# path = "/Users/danielmo/学习/项目/Personal_Projects/18-734_Cross_Site_Cookie_Requests/extensions/firefox/%s.xpi" % extensions[3]
# # profile.add_extension(path)

# profile.update_preferences()

# driver = webdriver.Firefox(firefox_profile=profile)

# driver.install_addon(path)


# set cookie from 3rd party
driver.get("http://silence-rain.cn:9888")
# attack
for i in range(4):
	driver.get('http://45.77.79.119/%s/index.html' % attacks[i])	
	time.sleep(2)
driver.get("http://45.77.79.119:9777")
time.sleep(2)

driver.close()