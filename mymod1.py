#mymod1.py
#__all__=[""]
print "I am:",__name__
xxx=101
_yyy=402
def printer():
    print xxx
def tester():print "Its christmas in Heaven..."

def minmax(test,*args):
    res=args[0]
    for arg in args[1:]:
        if test(arg,res):
            res=arg
    return res
def lessthan(x,y):return x<y
def grtrthan(x,y):return x>y

if __name__=='__main__':
    tester()
    print minmax(lessthan,4,3,2,1,6,5)
    print minmax(grtrthan,4,3,2,1,6,5)

