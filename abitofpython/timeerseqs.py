#! /usr/bin/python3
#file timeerseqs.py
import time,sys
reps=10000
size=100000
def tester(func,*args):
    startTime=time.time()
    for i in range(reps):
        func(*args);
    elapsed=time.time()-startTime
    return elapsed
def forStatement():
    res=[]
    for x in range(size):
        res.append(x)

def listComprehension():
    res=[abs(x) for x in range(size)]

def mapFunction():
    res=map(abs,range(size))

def generatorExpression():
    res=list(abs(x) for x in range(size))

print sys.version
tests=(forStatement,listComprehension,mapFunction,generatorExpression)
for testfunc in tests:
    print testfunc.__name__.ljust(20),'=>',tester(testfunc)
