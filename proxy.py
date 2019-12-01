import mitmproxy.http

res = []

def request(flow: mitmproxy.http.HTTPFlow):
	# request has been initiated
	if "http://silence-rain.cn:9888/?actual=1" in flow.request.url:
		# cookie is attached
		if "leak_test" in flow.request.cookies:
			print("cookie is attached")
		# cookie is not attached
		else:
			print("cookie is not attached")
	# # request has not been initiated
	# else:
	# 	print("request has not been initiated")