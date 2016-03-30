import Exercise3mod

st = "this is one string."

def stri(st):
    ss = {}
    for i in st:
	    c = st.count(i)
	    ss.update({i: c})
    print (len(st), ss)
    return (len(st), ss)

stri(st)
Exercise3mod.stri(st)
