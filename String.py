#-*- coding:utf-8 -*-
# gaoyiping (iam@gaoyiping.com)
# http://www.gaoyiping.com/
# https://github.com/gaoyiping
# https://gitee.com/Naff

def encode(s):
	if s is None:
		return None
	elif isinstance(s, dict):
		return {encode(k): encode(v) for k, v in s.iteritems()}
	elif isinstance(s, list):
		return [encode(v) for v in s]
	elif isinstance(s, unicode):
		return s.encode('utf-8')
	elif not isinstance(s, str):
		return str(s)
	else:
		return s