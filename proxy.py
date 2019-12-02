import mitmproxy.http

res = []

def request(flow: mitmproxy.http.HTTPFlow):
	# request has been initiated
	if "http://silence-rain.cn:9888/?ad_type=1" in flow.request.url:
		t = flow.request.query["type"]
		# cookie is attached
		if "leak_test" in flow.request.cookies:
			print("%s: cookie is attached" % t)
		# cookie is not attached
		else:
			print("%s: cookie is not attached" % t)
	# # request has not been initiated
	# else:
	# 	print("request has not been initiated")

def clientconnect(layer: mitmproxy.proxy.protocol.Layer):
	pass

def clientdisconnect(layer: mitmproxy.proxy.protocol.Layer):
	pass