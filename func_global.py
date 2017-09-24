#!/usr/bin/python3
#Filename: func_local.py
x=50

def func():
	global x
	print('x is ',x)
	x=2
	print('Changed global x to ', x)
func()
print ('value x is ',x)
