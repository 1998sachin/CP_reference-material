def myfunction(string,top):
	if string==[]:
		 if top=='bb' or top=='a':
		 	return True
	else:
		if top=='a':
			if string[0]=='a' or string[0]=='b':
				top=string[0]
				string.remove(string[0])
				return myfunction(string,top)
		elif top=='b':
			if string[0]=='b':
				top='bb'
				string.remove(string[0])
				return myfunction(string,top)
		elif top=='bb':
			if string[0]=='a':
				top='a'
				string.remove(string[0])
				return myfunction(string,top)
		
	return False

def before(string):
	if string[0]=='a':
		string.remove(string[0])
		return myfunction(string,'a')
	else:
		return False

print(before(['a','b','b','a','b']))


