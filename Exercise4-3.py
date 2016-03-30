
def fistat(name):
	string = open(name, "r")
	filee = string.read().lower().replace(",", "")
	char = len(filee)
	words = ""
	ssss = {}
	print (filee)
	words = filee.split()
	for i in words:
		c = words.count(i)
		ssss.update({c: i})
	print (ssss[max(ssss.keys())], len(words), char)
	string.close()

fistat("text.txt")
