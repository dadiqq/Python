#!/usr/bin/python
#Filename while.py
number = 23
running = True
while running:
	guess=int(input("Enter an interger:"))
	if guess == number:
		print("Congratulation,you guessed it.")
		running=False#this causes the while loop to stop
	elif guess < number:
		print("No,it is a little higher.")
	else:
		print("No, it is a little lower.")
else:
	print("the while loop is over.")
	#Do anything else you want to deo here
print("done")
