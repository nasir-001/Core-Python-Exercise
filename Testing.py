def testit(func, *nkwargs, **kwargs):
	try:
		retval = func(*nkwargs, **kwargs)
		result = (True, retval)
	except Exception, diag:
		result =  (False, str(diag))
	return result

def test():
	funcs = (int, long, float)
	vals 