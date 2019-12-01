import mitmproxy.http
from mitmproxy import ctx

def request(flow: mitmproxy.http.HTTPFlow):
	# request has been initiated
	if "http://silence-rain.cn:9888/?actual=1" in flow.request.url:
		print(flow.request.cookies)
	# request has not been initiated
	else:
		pass