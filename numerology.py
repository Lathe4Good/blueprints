import re

set1 = ['A', 'J', 'S']
set2 = ['B', 'K', 'T']
set3 = ['C', 'L','U']
set4 = ['D', 'M',  'V']
set5 = ['E', 'N', 'W']
set6 = ['F', 'O', 'X']
set7 = ['G', 'P', 'Y']
set8 = ['H', 'Q', 'Z']
set9 = ['I', 'R']


def yes():
	x = 0
	for each in y:
		each = each.upper()
		if each in set1:
			x += 1
		elif each in set2:
			x += 2
		elif each in set3:
			x += 3
		elif each in set4:
			x += 4
		elif each in set5:
			x += 5
		elif each in set6:
			x += 6
		elif each in set7:
			x += 7
		elif each in set8:
			x += 8
		elif each in set9:
			x += 9

	def check():
		if (x == "11") or (x == "22"):
			print("11 or 22 detected.")
		else:
			length(x)

	length(x)



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



question = input("Would you like to enter a name? ")
if re.match('^Y', question, re.IGNORECASE):
	y = input("Enter name: ")
	yes()
elif re.match('^N', question, re.IGNORECASE):
	n = input("Enter number: ")
	length(n)
else:
	quit()

#Make it less hard coded so it'll work beyond numbers of >3 digits?
#Possibly add in numerology info if it interests you
