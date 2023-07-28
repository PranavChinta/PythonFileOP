class File:
	contents = ""
	match = ""
	
	#method to check if string matches file
	
	def StringMatch(s):
		word = ""
		ret = ""
		arr = []
		status = 0
		ct = 0
		for x in s.contents:
				ct+=1
				if x == " ":
					#print("Word: " + word)
					if word == s.match:
						ret = word + " is a match"
						status = 1	
					word = ""
				else:	
					word += x
					if ct+1 == length:
						#print("Word: ", word)
						if word == s.match:
							ret = word + " is a match"
							status = 1	
		if(status == 0):
			ret = string+" doesn't exist in one.txt file"
		return ret	

obj1  = File()	#File object initialization

###########Step1##################
f = open('one.txt', 'a')
cont = (raw_input("Input data for one.txt: "))
f.write(cont)
f.close()
##########Step2#################
f = open('one.txt', 'r')
obj1.contents = f.read() #passing in contents to object, read bytes in form of a string
length = len(obj1.contents)
print(obj1.contents)

#########Step3#########


	
	
obj1.match = (raw_input("Input a string to see if it exists in one.txt: "))
print(obj1.StringMatch())	
#######################Step4##########################
f2 = open('two.txt', 'w')
f2.write(obj1.contents)
f2.close()
#f2 = open('two.txt', 'r')
#r = f2.read()
#print(r)


	

