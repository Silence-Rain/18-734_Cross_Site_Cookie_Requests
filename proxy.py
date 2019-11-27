import mitmproxy.http
from mitmproxy import ctx

def request(flow: mitmproxy.http.HTTPFlow):
	ctx.log.info(flow)