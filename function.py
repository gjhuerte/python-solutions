#global and local function
exit = 1
z = 1

def globalnumber():
	global z

def number_compare(a):
	if a % 2 == 0:
		print('even')
	else:
		print('odd')
	
def enter_number(exit):
	while exit != 0:
		x = int(input('Enter a number: '))
		number_compare(x)
		exit = int(input('Exit status = '))
		
def printProgramName():
	print("Hello! This program is from function")

print('z is ',z)
enter_number(exit)
z = 2
globalnumber()
print('global z is now ',z)



	