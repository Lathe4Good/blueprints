new = ""
end = 0



def length(x):
	x = str(x)
	def calc():
		if len(x) == 2:
			first = new[0]
			second = new[1]
			first = int(first)
			second = int(second)
			end = first + second
			#print(end)
			special(end)
		elif len(x) == 3:
			first = new[0]
			second = new[1]
			third = new[2]
			first = int(first)
			second = int(second)
			third = int(third)
			end = first + second + third
			print(end)
			special(end)

	def special(end):
		if (end == 11):
			print("It makes 11")
		elif (end == 22):
			print("It makes 22")
		elif (end > 9):
			length(end)
		else:
			print(end)
	
	if len(x) == 2:
		new = [x[i:i+1] for i in range(0,len(x),1)]
		#print(new)
		calc()

	elif len(x) == 3:
		new = [x[i:i+1] for i in range(0,len(x))]
		#print(new)
		calc()

	else:
		print(x)

y = input("Please type a number: ")

def check():
	if (y == "11") or (y == "22"):
		print("11 or 22 detected.")
	else:
		length(y)

check()

#Make it less hard coded so it'll work beyond numbers of >3 digits?
#Possibly add in numerology info if it interests you