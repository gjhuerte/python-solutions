#if statement 
#elif statement(shortcut for else-if)
#while and for loop

time = 0
while time < 12:
	time = int(input("ENTER TIME:"))
	if time < 12:
		print("ITS STILL DAY")
	elif time >= 12:
		print("GOOD NIGHT")
	if time == 0:
		print('time not valid')
		break
for time in range(1,time):
	print(time)
else:
	print('the time is over')