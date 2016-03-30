def stri(st):
    ss = {}
    for i in st:
	    c = st.count(i)
	    ss.update({i: c})
    print (len(st), ss)
    return (len(st), ss)
