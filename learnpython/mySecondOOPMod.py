#mySecondOOPMod.py
from myFirstOOPMod import FirstClass

class SecondClass(FirstClass):
    def display(self):
        print 'Current Vlaue = "%s" ' % self.data
x=FirstClass()
y=FirstClass()
print "x.a=",x.a
print "y.a=",y.a
x.a=45
print "x.a=",x.a
print "y.a",y.a
x.setdata("king arthur")
y.setdata(3.14258)
x.display()
y.display()
x.anothername='spam'
print "x.anothername=",x.anothername
z=SecondClass()
z.setdata(42)
z.display()
class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data=value
    def __add__(self,other):
        return ThirdClass(self.data+other)
    def __mul__(self,other):
        self.data=self.data*other
a=ThirdClass("abc")
print 'a.display()'
a.display()
b=a+'xyz'
print 'b.display()'
b.display()
a*3
a.display()
