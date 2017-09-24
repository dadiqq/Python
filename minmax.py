#!/usr/bin/python
#minmax.py
def minmax(test,*args):
    res=args[0]
    for arg in args[1:]:
        if test(arg,res):
            res=arg
    return res
def lessthan(x,y):return x<y
def grtrthan(x,y):return x>y

print minmax(lessthan,4,7,9,22,18)
print minmax(grtrthan,4,7,9,22,18)
