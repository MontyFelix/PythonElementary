string = "this is one string."
ss = {}
for i in string:
	c = string.count(i)
	ss.update({i: c})
print (len(string), ss)
