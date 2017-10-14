#! /usr/bin/python3
Python 2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> x=99
>>> print x
99
>>> def func:
	
SyntaxError: invalid syntax
>>> def func:
	
SyntaxError: invalid syntax
>>> def func():
	x=88
	print(x)

	
>>> func()
88
>>> func(9)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    func(9)
TypeError: func() takes no arguments (1 given)
>>> def func(x):
	print (x**2)

	
>>> func(8)
64
>>> exec func

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    exec func
TypeError: exec: arg 1 must be a string, file, or code object
>>> ================================ RESTART ================================
>>> 
>>> func(99)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    func(99)
TypeError: func() takes no arguments (1 given)
>>> func
<function func at 0x7fb53162b6e0>
>>> ================================ RESTART ================================
>>> 
>>> func(1)
100
>>> ================================ RESTART ================================
>>> 
>>> func(9)
108
>>> TypeError: func() takes no arguments (1 given)
SyntaxError: invalid syntax
>>> 
>>> ================================ RESTART ================================
>>> 
>>> func(100)
199
>>> ================================ RESTART ================================
>>> 
>>> func(1000)
1099
>>> import __builtin__
>>> dir(__builtin__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
>>> zip
<built-in function zip>
>>> set (a,b,c)

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set (a,b,c)
NameError: name 'a' is not defined
>>> b=set(1,3)

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    b=set(1,3)
TypeError: set expected at most 1 arguments, got 2
>>> help(set)
Help on class set in module __builtin__:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
 |  
 |  Build an unordered collection of unique elements.
 |  
 |  Methods defined here:
 |  
 |  __and__(...)
 |      x.__and__(y) <==> x&y
 |  
 |  __cmp__(...)
 |      x.__cmp__(y) <==> cmp(x,y)
 |  
 |  __contains__(...)
 |      x.__contains__(y) <==> y in x.
 |  
 |  __eq__(...)
 |      x.__eq__(y) <==> x==y
 |  
 |  __ge__(...)
 |      x.__ge__(y) <==> x>=y
 |  
 |  __getattribute__(...)
 |      x.__getattribute__('name') <==> x.name
 |  
 |  __gt__(...)
 |      x.__gt__(y) <==> x>y
 |  
 |  __iand__(...)
 |      x.__iand__(y) <==> x&=y
 |  
 |  __init__(...)
 |      x.__init__(...) initializes x; see help(type(x)) for signature
 |  
 |  __ior__(...)
 |      x.__ior__(y) <==> x|=y
 |  
 |  __isub__(...)
 |      x.__isub__(y) <==> x-=y
 |  
 |  __iter__(...)
 |      x.__iter__() <==> iter(x)
 |  
 |  __ixor__(...)
 |      x.__ixor__(y) <==> x^=y
 |  
 |  __le__(...)
 |      x.__le__(y) <==> x<=y
 |  
 |  __len__(...)
 |      x.__len__() <==> len(x)
 |  
 |  __lt__(...)
 |      x.__lt__(y) <==> x<y
 |  
 |  __ne__(...)
 |      x.__ne__(y) <==> x!=y
 |  
 |  __or__(...)
 |      x.__or__(y) <==> x|y
 |  
 |  __rand__(...)
 |      x.__rand__(y) <==> y&x
 |  
 |  __reduce__(...)
 |      Return state information for pickling.
 |  
 |  __repr__(...)
 |      x.__repr__() <==> repr(x)
 |  
 |  __ror__(...)
 |      x.__ror__(y) <==> y|x
 |  
 |  __rsub__(...)
 |      x.__rsub__(y) <==> y-x
 |  
 |  __rxor__(...)
 |      x.__rxor__(y) <==> y^x
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __sub__(...)
 |      x.__sub__(y) <==> x-y
 |  
 |  __xor__(...)
 |      x.__xor__(y) <==> x^y
 |  
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two or more sets as a new set.
 |      
 |      (i.e. elements that are common to all of the sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None
 |  
 |  __new__ = <built-in method __new__ of type object>
 |      T.__new__(S, ...) -> a new object with type S, a subtype of T

>>> ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
>>> 
>>> def hider():
	open='spam'
	open('data.txt')

	
>>> hider()

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    hider()
  File "<pyshell#34>", line 3, in hider
    open('data.txt')
TypeError: 'str' object is not callable
>>> hider()

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    hider()
  File "<pyshell#34>", line 3, in hider
    open('data.txt')
TypeError: 'str' object is not callable
>>> open('limq.txt',w)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    open('limq.txt',w)
NameError: name 'w' is not defined
>>> open('limq.txt',r)

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    open('limq.txt',r)
NameError: name 'r' is not defined
>>> x=88
>>> def func1():
	x=99

	
>>> func1()
>>> print(x)
88
>>> def func2():
	global x
	x=99

	
>>> print x
88
>>> func2()
>>> x
99
>>> print x
99
>>> y,z=1,2
>>> del all_global():
	
SyntaxError: invalid syntax
>>> del all_global():
	
SyntaxError: invalid syntax
>>> def all_global():
	global x
	x=y+z

	
>>> all_gloabal()

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    all_gloabal()
NameError: name 'all_gloabal' is not defined
>>> all_glbal()

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    all_glbal()
NameError: name 'all_glbal' is not defined
>>> all_global()
>>> x
3
>>> x=99
>>> def func11():
	global x
	x=111

	
>>> def func12():
	global x
	x=67

	
>>> func11()
>>> func12()
>>> x
67
>>> ================================ RESTART ================================
>>> 
>>> func6(6)

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    func6(6)
NameError: name 'func6' is not defined
>>> func(6)
105
>>> ================================ RESTART ================================
>>> 
>>> func(90)
189
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
>>> test()
99

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    test()
  File "/home/limq/thismod.py", line 19, in test
    local();glob1();glob2();glob3()
  File "/home/limq/thismod.py", line 15, in glob3
    glob=sys.modules('thismod')
TypeError: 'dict' object is not callable
>>> ================================ RESTART ================================
>>> 
>>> test()
99

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    test()
  File "/home/limq/thismod.py", line 19, in test
    local();glob1();glob2();glob3()
  File "/home/limq/thismod.py", line 15, in glob3
    glob=sys.modules('thismod')
TypeError: 'dict' object is not callable
>>> ================================ RESTART ================================
>>> 
>>> test()
99
100
>>> test()
100
101
>>> def f1():
	x=88
	def f2():
		print x

		
>>> f1()
>>> f2()

Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    f2()
NameError: name 'f2' is not defined
>>> f1()
>>> def f1():
	x=88
	def f2():
		print x
	f2()

	
>>> f1()
88
>>> f2

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    f2
NameError: name 'f2' is not defined
>>> f2()

Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    f2()
NameError: name 'f2' is not defined
>>> f1.f2

Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    f1.f2
AttributeError: 'function' object has no attribute 'f2'
>>> def f3:
	
SyntaxError: invalid syntax
>>> def f3():
	x=99
	def f4():
		print x
	return f4

>>> f3()
<function f4 at 0x7f9c4be47cf8>
>>> action=f3()
>>> action()
99
>>> 
>>> def maker(N):
	def action():
		return x**N
	return action

>>> zz=maker()

Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    zz=maker()
TypeError: maker() takes exactly 1 argument (0 given)
>>> zz=maker(2)
>>> zz
<function action at 0x7f9c4be47e60>
>>> zz()

Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    zz()
  File "<pyshell#116>", line 3, in action
    return x**N
NameError: global name 'x' is not defined
>>> zz(2)

Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    zz(2)
TypeError: action() takes no arguments (1 given)
>>> zz(3)

Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    zz(3)
TypeError: action() takes no arguments (1 given)
>>> def maker(N):
	def action(x):
		return x**N
	return action

>>> f=maker(2)
>>> f(3)
9
>>> g=maker(3)
>>> g(3)
27
>>> f(10)
100
>>> def ff1():
	x=108
	def ff2(x=x):
		print x
	ff2()

	
>>> ff1()
108
>>> d=ff1()
108
>>> d()

Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    d()
TypeError: 'NoneType' object is not callable
>>> d(9)

Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    d(9)
TypeError: 'NoneType' object is not callable
>>> def ff1():
	x=108
	def ff2(x=x):
		print x
	ff2()

	
>>> 
>>> def func1():
	x=208
	func2(x)

	
>>> def func2(x):
	print x

	
>>> func1()
208
>>> 
>>> def func(): 
	x=4
	action=(lambda n: x**n)
	return action

>>> x(2)

Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    x(2)
NameError: name 'x' is not defined
>>> x=func()
>>> x(2)
16
>>> x(3)
64
>>> def func(): 
	x=4
	action=(lambda n ,x=x: x**n)
	return action

>>> x=func()
>>> x(3)
64
>>> x(3,4)
64
>>> x(3,3)
27
>>> 
>>> 
>>> 
>>> 
def makeActions():
	acts=[]
	for i in range(5):
		acts.append(lambda x:i**x)
	return acts

>>> acts=makeActions()
>>> acts[0]
<function <lambda> at 0x7f9c4be592a8>
>>> acts[0]
<function <lambda> at 0x7f9c4be592a8>
>>> acts[0](2)
16
>>> acts[1](2)
16
>>> def makeActions():
	acts=[]
	for i in range(5):
		acts.append(lambda x,i=i:i**x)
	return acts

>>> acts=makeActions()
>>> acts[0](2)
0
>>> acts[1](2)
1
>>> acts[2](2)
4
>>> acts[4](2)
16
>>> acts[4](4)
256
>>> def fc1():
	x=99
	def fc2():
		def fc3():
			print x
		fc3()
	fc2()

	
>>> fc1()
99
>>> def changer()
SyntaxError: invalid syntax
>>> def changer(a,b):
	a=2
	b[0]='spam'

	
>>> x=1;L=[1,2]
>>> changer(x,L)
>>> L
['spam', 2]
>>> x
1
>>> x,L
(1, ['spam', 2])
>>> a=x
>>> a=2
>>> x
1
>>> L
['spam', 2]
>>> b=L
>>> b[0]='A'
>>> L
['A', 2]
>>> changer(x,L[:])
>>> L
['A', 2]
>>> b
['A', 2]
>>> def changer(a,b):
	b=b[:]
	a=2
	b[0]='Spam'

	
>>> L
['A', 2]
>>> changer(x,L)
>>> L
['A', 2]
>>> L[0]=1
>>> L
[1, 2]
>>> changer(x,L)
>>> L
[1, 2]
>>> def changer(a,b):
	#b=b[:]
	a=2
	b[0]='Spam'

	
>>> changer(x,L)
>>> L
['Spam', 2]
>>> L[0]=1
>>> changer(x,tuple(L))

Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    changer(x,tuple(L))
  File "<pyshell#232>", line 4, in changer
    b[0]='Spam'
TypeError: 'tuple' object does not support item assignment
>>> changer(x,tuple(L))

Traceback (most recent call last):
  File "<pyshell#237>", line 1, in <module>
    changer(x,tuple(L))
  File "<pyshell#232>", line 4, in changer
    b[0]='Spam'
TypeError: 'tuple' object does not support item assignment
>>> def multiple(x,y):
	x=2
	y=[3,4]
	return x,y

>>> x=1
>>> L=[1,2]
>>> x,L=multiple(x,L)
>>> x,L
(2, [3, 4])
>>> L
[3, 4]
>>> z=multiple(x,L)
>>> z
(2, [3, 4])
>>> def f(a,b,c):
	print a,b,c

	
>>> f(1,2,3)
1 2 3
>>> f(4,5,'z')
4 5 z
>>> f(c=100,b=50,a=111)
111 50 100
>>> f(12,c=5,b=33)
12 33 5
>>> def f(a,b=2,c=3):print a,b,c

>>> f(4)
4 2 3
>>> f(a=9,b=34)
9 34 3
>>> f(1,c=6)
1 2 6
>>> def f1(*args):
	print args

	
>>> f1()
()
>>> f1(1)
(1,)
>>> f1(1,3,4,'a')
(1, 3, 4, 'a')
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> dir
<built-in function dir>
>>> pwd

Traceback (most recent call last):
  File "<pyshell#269>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> f2()

Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    f2()
NameError: name 'f2' is not defined
>>> NameError: name 'f2' is not defined
SyntaxError: invalid syntax
>>> 
>>> def f2(**args):print args

>>> f2(s)

Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    f2(s)
NameError: name 's' is not defined
>>> f2(s=2)
{'s': 2}
>>> f2()
{}
>>> f2(a=1,b=2)
{'a': 1, 'b': 2}
>>> def f3(a,*pargs,**kargs):print a,pargs,kargs

>>> f3(1,2,3,4,x=11,y=12)
1 (2, 3, 4) {'y': 12, 'x': 11}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ================================ RESTART ================================
>>> def func(a,b,c,d):print a,b,c,d

>>> args=(1,2)
>>> args+=(3,4)
>>> func(*args)
1 2 3 4
>>> args={'a':1,'b':3,'c':3,'d':4}
>>> args{}
SyntaxError: invalid syntax
>>> args
{'a': 1, 'c': 3, 'b': 3, 'd': 4}
>>> ================================ RESTART ================================
>>> func(**args)

Traceback (most recent call last):
  File "<pyshell#297>", line 1, in <module>
    func(**args)
NameError: name 'func' is not defined
>>> func(**args)

Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    func(**args)
NameError: name 'func' is not defined
>>> args

Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    args
NameError: name 'args' is not defined
>>> args

Traceback (most recent call last):
  File "<pyshell#300>", line 1, in <module>
    args
NameError: name 'args' is not defined
>>> args={'a':1,'b':3,'c':3,'d':4}
>>> func(**args)

Traceback (most recent call last):
  File "<pyshell#302>", line 1, in <module>
    func(**args)
NameError: name 'func' is not defined
>>> func()

Traceback (most recent call last):
  File "<pyshell#303>", line 1, in <module>
    func()
NameError: name 'func' is not defined
>>> def func(a,b,c,d):print a,b,c,d

>>> args={'a':1,'b':3,'c':3,'d':4}
>>> func(**args)
1 3 3 4
>>> func(10,*(6,9),**{'d':7})
10 6 9 7
>>> func(1,c=3,*(2),**{'d':4})

Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    func(1,c=3,*(2),**{'d':4})
TypeError: func() argument after * must be a sequence, not int
>>> func(1,c=3,*(2,),**{'d':4})
1 2 3 4
>>> ================================ RESTART ================================
>>> 
1

Traceback (most recent call last):
  File "/home/limq/mins.py", line 18, in <module>
    print min2("bb","aa")
  File "/home/limq/mins.py", line 11, in min2
    first=args
NameError: global name 'args' is not defined
>>> ================================ RESTART ================================
>>> 
1
aa
[1, 2]
>>> ================================ RESTART ================================
>>> 
4
22
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> x=1
>>> L=[1,2]
>>> changer(x,L)

Traceback (most recent call last):
  File "<pyshell#314>", line 1, in <module>
    changer(x,L)
NameError: name 'changer' is not defined
>>> 
>>> def intersect(*args):
	res=[]
	for x in args[0]:
		for other in args[1:]
		
SyntaxError: invalid syntax
>>> def intersect(*args):
	res=[]
	for x in args[0]:
		for other in args[1:]:
			if x not in other:break
		else:
			res.append(x)
	return res

>>> def union(*args):
	res=[]
	for seq in args:
		for x in seq:
			if not x in res:
				res.append(x)
	return res

>>> s1,s2,s3='SPAM','SCAM','SLAM'
>>> intersect(s1,s2)
['S', 'A', 'M']
>>> union(s1,s2)
['S', 'P', 'A', 'M', 'C']
>>> intersect([1,2,3],(1,4))
[1]
>>> intersect(s1,s2,sa)

Traceback (most recent call last):
  File "<pyshell#338>", line 1, in <module>
    intersect(s1,s2,sa)
NameError: name 'sa' is not defined
>>> intersect(s1,s2,s3)
['S', 'A', 'M']
>>> union(s1,s2,s3)
['S', 'P', 'A', 'M', 'C', 'L']
>>> 
>>> lambda 参数一，参数二:表达式
SyntaxError: invalid syntax
>>> f=lambda x,y,z:x+y+z
>>> f(3,4,5)
12
>>> def func(x,y,z):return x+y+z

>>> func(3,4,5)
12
>>> x=(lambda a='fee',b='file',c='foe':a+b+c)
>>> x()
'feefilefoe'
>>> x()
'feefilefoe'
>>> x('wee')
'weefilefoe'
>>> def knights():
	title='sir'
	action=(lambda x:title+' '+x)
	return action

>>> act=knights()
>>> act
<function <lambda> at 0x7f5020cfeaa0>
>>> act()

Traceback (most recent call last):
  File "<pyshell#359>", line 1, in <module>
    act()
TypeError: <lambda>() takes exactly 1 argument (0 given)
>>> act(x)

Traceback (most recent call last):
  File "<pyshell#360>", line 1, in <module>
    act(x)
  File "<pyshell#356>", line 3, in <lambda>
    action=(lambda x:title+' '+x)
TypeError: cannot concatenate 'str' and 'function' objects
>>> act('x')
'sir x'
>>> act('robin')
'sir robin'
>>> L=[(lambda x:x**2),(lambda x:x**3),(lambda x :x**4) ]
>>> for f lin L:
	
SyntaxError: invalid syntax
>>> for f in L:
	print f(2)

	
4
8
16
>>> L
[<function <lambda> at 0x7f5020cfeb18>, <function <lambda> at 0x7f5020cfeb90>, <function <lambda> at 0x7f5020cfec08>]
>>> L()

Traceback (most recent call last):
  File "<pyshell#369>", line 1, in <module>
    L()
TypeError: 'list' object is not callable
>>> L(3)

Traceback (most recent call last):
  File "<pyshell#370>", line 1, in <module>
    L(3)
TypeError: 'list' object is not callable
>>> key='got'
>>> {'already':(lambda:2+2),'got':(lambda:2**4),'one':(lambda :2**6)}[key]()
16
>>> b if a else c

Traceback (most recent call last):
  File "<pyshell#373>", line 1, in <module>
    b if a else c
NameError: name 'a' is not defined
>>> a=1
>>> b=3
>>> c=5
>>> b if a else c
3
>>> lower=(lambda x,y:x if x<y else y)
>>> lower(3,5)
3
>>> lower(b,a)
1
>>> lower('b','a')
'a'
>>> lower('b','az')
'az'
>>> lower('ab','az')
'ab'
>>> import sys
>>> showall=(lambda x:map(sys.stdout.write,x))
>>> t=showall(['apam\n','toast\n','eggs\n'])
apam
toast
eggs
>>> showall=lambda x:[sys.stdout.write(line)for line in x]
>>> t=showall(('bright\n','of\n','life\n'))
bright
of
life
>>> def action(x):
	return (lambda y:x+y)

>>> act=action(99)
>>> act(2)
101
>>> action=(lambda x:(lambda y:x+y))
>>> act=action(99)
>>> act(3)
102
>>> ((lambda x:(lambda y:x+y))(99))(4)
103
>>> def func(x,y,z):
	return x+y+z

>>> apply(func,(2,3,4))
9
>>> func(3,4,5)
12
>>> f=lambda x,y,x:x+y+z
SyntaxError: duplicate argument 'x' in function definition (<pyshell#403>, line 1)
>>> f=lambda x,y,z:x+y+z
>>> apply(f,(3,4,5))
12
>>> args=(2,3)+(4,)
>>> apply(func,args)
9
>>> def dcho(*args,**kwargs):print args,kwargs

>>> def echo(*args,**kwargs):print args,kwargs

>>> echo(1,2,a=3,b=4)
(1, 2) {'a': 3, 'b': 4}
>>> apply(echo.pargs,kargs)

Traceback (most recent call last):
  File "<pyshell#413>", line 1, in <module>
    apply(echo.pargs,kargs)
AttributeError: 'function' object has no attribute 'pargs'
>>> pargs=(1,2)
>>> kargs={'a':3,'b':5}
>>> apply(echo.pargs,kargs)

Traceback (most recent call last):
  File "<pyshell#416>", line 1, in <module>
    apply(echo.pargs,kargs)
AttributeError: 'function' object has no attribute 'pargs'
>>> apply(echo,pargs,kargs)
(1, 2) {'a': 3, 'b': 5}
>>> echo(*pargs,**kargs)
(1, 2) {'a': 3, 'b': 5}
>>> echo(pargs,kargs)
((1, 2), {'a': 3, 'b': 5}) {}
>>> counters=[1,2,3,4]
>>> update=[]
>>> for x in conterr:
	update.append(x+10)

	

Traceback (most recent call last):
  File "<pyshell#424>", line 1, in <module>
    for x in conterr:
NameError: name 'conterr' is not defined
>>> for x in counter:
	update.append(x+10)

	

Traceback (most recent call last):
  File "<pyshell#426>", line 1, in <module>
    for x in counter:
NameError: name 'counter' is not defined
>>> for x in counters:
	update.append(x+10)

	
>>> update
[11, 12, 13, 14]
>>> def inc(x):return x+10

>>> map(inc,counters)
[11, 12, 13, 14]
>>> map(lambda x:x+3,counters)
[4, 5, 6, 7]
>>> def  mymap(func,seq):
	res=[]
	for x in seq:
		res.append(func(x))
	return res

>>> map(inc,[1,2,3])
[11, 12, 13]
>>> mymap(inc,[1,2,3])
[11, 12, 13]
>>> pow(3,4)
81
>>> map(pow,[1,2,3],[4,5,6])
[1, 32, 729]
>>> range(-5,5)
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
>>> range(-5,5,2)
[-5, -3, -1, 1, 3]
>>> range(5,-5,-2)
[5, 3, 1, -1, -3]
>>> filter((lambda x:x>0),range(-5,5))
[1, 2, 3, 4]
>>> res=[]
>>> for x in range(-5,5)：
SyntaxError: invalid syntax
>>> for x in range(-5,5):
	if x>0:
		res.append(x)

		
>>> res
[1, 2, 3, 4]
>>> reduce((lambda x,y:x+y),[1,2,3,4])
10
>>> L=[1,2,3,4]
>>> res=L[]
SyntaxError: invalid syntax
>>> res=L[0]
>>> for x in L[1:]:
	res=res+x

	
>>> res
10
>>> reduce((lambda x,y:x*y),[1,2,3,4])
24
>>> for x in L[1:]:
	res=res*x

	
>>> res
240
>>> res
240
>>> def myreduce(function,sequence):
	tally=sequence[0]
	for n in sequence[1:]:
		tally=function(ally,n)
	return tally

>>> myreduce((lambda x,y:x+y),[1,2,3,4,5])

Traceback (most recent call last):
  File "<pyshell#474>", line 1, in <module>
    myreduce((lambda x,y:x+y),[1,2,3,4,5])
  File "<pyshell#473>", line 4, in myreduce
    tally=function(ally,n)
NameError: global name 'ally' is not defined
>>> def myreduce(function,sequence):
	tally=sequence[0]
	for n in sequence[1:]:
		tally=function(tally,n)
	return tally

>>> myreduce((lambda x,y:x+y),[1,2,3,4,5])
15
>>> ord('s')
115
>>> res[]
SyntaxError: invalid syntax
>>> res=[]
>>> for x in 'spam':
	res.append(ord(x))

	
>>> res
[115, 112, 97, 109]
>>> res=map(ord,'spam')
>>> res\

     
[115, 112, 97, 109]
>>> reduce((lambda x ,y:x+y),[1,2,3,4])
10
>>> L=[1,2,3,4]
>>> res=L[0]
>>> for x in L[1:]:
	res=res+x

	
>>> res
10
>>> reduce((lambda x,y:x*y),[1,2,3,4])
24
>>> for x in L[1:]:
	res=res*x

	
>>> res
240
>>> L
[1, 2, 3, 4]
>>> res
240
>>> for x in L[1:]:
	res=res*x

	
>>> res
5760
>>> res=[]
>>> for x in L[1:]:
	res=res*x

	
>>> res
[]
>>> res=L[0]
>>> for x in L[1:]:
	res=res*x

	
>>> res
24
>>> def myreduce(function,sequence):
	tally=sequence[0]
	for n in sequence[1:]:
		tally=function(tally,n)
	return tally

>>> myreduce((lambda x,y:x+y),[1,2,3,4,5])
15
>>> myreduce((lambda x,y:x*y),[1,2,3,4,5])
120
>>> import operator
>>> reduce(operator.add.[2,3,6])
SyntaxError: invalid syntax
>>> reduce(operator.add,[2,3,6])
11
>>> reduce((lambda x,y:x+y),[2,3,6])
11
>>> ord('s')
115
>>> for z in ['dsddddd']:print z

dsddddd
>>> for z in ['dsddddd']:print z\n
SyntaxError: unexpected character after line continuation character
>>> for z in ['dsddddd']:print "z\n"

z

>>> for z in ['dsddddd']:
	res.append(ord(x))

	

Traceback (most recent call last):
  File "<pyshell#532>", line 2, in <module>
    res.append(ord(x))
AttributeError: 'int' object has no attribute 'append'
>>> for z in 'dsddddd':
	res.append(ord(x))

	

Traceback (most recent call last):
  File "<pyshell#534>", line 2, in <module>
    res.append(ord(x))
AttributeError: 'int' object has no attribute 'append'
>>> for z in 'dsddddd':
	res.append(ord(z))

	

Traceback (most recent call last):
  File "<pyshell#536>", line 2, in <module>
    res.append(ord(z))
AttributeError: 'int' object has no attribute 'append'
>>> for z in 'dsddddd':
	res.append(ord(z))

	

Traceback (most recent call last):
  File "<pyshell#538>", line 2, in <module>
    res.append(ord(z))
AttributeError: 'int' object has no attribute 'append'
>>> res
24
>>> res=[]
>>> for z in 'dsddddd':
	res.append(ord(z))

	
>>> res
[100, 115, 100, 100, 100, 100, 100]
>>> rres=map(ord,'spam')
>>> 
>>> rres
[115, 112, 97, 109]
>>> res=[]
>>> for x in 'spam':
	res.append(ord(x))

	
>>> res
[115, 112, 97, 109]
>>> for x in 'spam':
	ress.append(ord(x))

	

Traceback (most recent call last):
  File "<pyshell#553>", line 2, in <module>
    ress.append(ord(x))
NameError: name 'ress' is not defined
>>> for x in 'spam':
	rres.append(ord(x))

	
>>> rres
[115, 112, 97, 109, 115, 112, 97, 109]
>>> res=[ord(x) for x in 'spam']
>>> 
>>> res
[115, 112, 97, 109]
>>> res=[x**x for x in range(10)]
>>> res
[1, 1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]
>>> res=[x**2 for x in range(10)]
>>> res
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> map((lambda x:x**2),range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> map((lambda x:x**2),range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> map((lambda x:x**2),range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> map((lambda x:x**2),range(100))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801]
>>> filter((lambda x:x%2==0),range(5))
[0, 2, 4]
>>> [x for x in range(5) if x%2==0]
[0, 2, 4]
>>> ================================ RESTART ================================
>>> res=[]
>>> for x in range(5):
	if x%2==0:
		res.append(x)

		
>>> res
[0, 2, 4]
>>> [x**2 for x in range(10) if x%2==0]
[0, 4, 16, 36, 64]
>>> [x**4 for x in range(10) if x%2==0]
[0, 16, 256, 1296, 4096]
>>> map((lambda x:x**2),filter((lambda x:x%2++0),range(10)))
[1, 9, 25, 49, 81]
>>> ================================ RESTART ================================
>>> res=[]
>>> res=[x+y for x in [0,1,2] for y in [100,200,300]]
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]
>>> for x in [0,1,2]:
	for y in [100,200,300]:
		res.append(x+y)

		
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302, 100, 200, 300, 101, 201, 301, 102, 202, 302]
>>> res[]
SyntaxError: invalid syntax
>>> res=[]
>>> for x in [0,1,2]:
	for y in [100,200,300]:
		res.append(x+y)

		
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]
>>> [x+y for x in 'spam' for y in 'SPAM']
['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM', 'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']
>>> [(x+y) for x in range(5)if x%2==0 for y in range(5) if y%2==1]
[1, 3, 3, 5, 5, 7]
>>> [(x,y) for x in range(5)if x%2==0 for y in range(5) if y%2==1]
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
>>> res=[]
\
>>> for x in range(5)
SyntaxError: invalid syntax
>>> for x in range(5):
	if x%2==0:
		for y in range(5):
			if y%2==1：
			
SyntaxError: invalid syntax
>>> for x in range(5):
	if x%2==0:
		for y in range(5):
			if y%2==1:
				res.append(x,y)

				

Traceback (most recent call last):
  File "<pyshell#603>", line 5, in <module>
    res.append(x,y)
TypeError: append() takes exactly one argument (2 given)
>>> for x in range(5):
	if x%2==0:
		for y in range(5):
			if y%2==1:
				res.append((x,y))

				
>>> res
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
>>> res
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]
>>> M=[[1,2,3],[4,5,6],[7,8,9]]
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> N=[[2,2,2][3,3,3][4,4,4]]

Traceback (most recent call last):
  File "<pyshell#610>", line 1, in <module>
    N=[[2,2,2][3,3,3][4,4,4]]
TypeError: list indices must be integers, not tuple
>>> N=[[2,2,2][3,3,3],[4,4,4]]

Traceback (most recent call last):
  File "<pyshell#611>", line 1, in <module>
    N=[[2,2,2][3,3,3],[4,4,4]]
TypeError: list indices must be integers, not tuple
>>> N=[[2,2,2],[3,3,3],[4,4,4]]
>>> M[1][2]
6
>>> M[1]
[4, 5, 6]
>>> [row[1]for row in M]
[2, 5, 8]
>>> [M[row][1]for row in (0,1,2)]
[2, 5, 8]
>>> [M[i][i] for i in range(len(M))]
[1, 5, 9]
>>> [ M[row][col]*N for row in range(3) for col in range(3)]
[[[2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]], [[2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4], [2, 2, 2], [3, 3, 3], [4, 4, 4]]]
>>> [ M[row][col]*N[row][col] for row in range(3) for col in range(3)]
[2, 4, 6, 12, 15, 18, 28, 32, 36]
>>> [[for col in range(3)]for row in range (3)]
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> def gensquares(N)：
SyntaxError: invalid syntax
>>> def gensquares(N):
	for i in range(N):
		yield i**2

		
>>> gensquares(5)
<generator object gensquares at 0x7f1c80b895a0>
>>> x=gensquares(5)
>>> x
<generator object gensquares at 0x7f1c80b1ea00>
>>> x(2)

Traceback (most recent call last):
  File "<pyshell#629>", line 1, in <module>
    x(2)
TypeError: 'generator' object is not callable
>>> x.next
<method-wrapper 'next' of generator object at 0x7f1c80b1ea00>
>>> x.next()
0
>>> x.next()
1
>>> x.next()
4
>>> x.next()
9
>>> x.next()
16
>>> x.next()

Traceback (most recent call last):
  File "<pyshell#636>", line 1, in <module>
    x.next()
StopIteration
>>> range(6)
[0, 1, 2, 3, 4, 5]
>>> x.next()

Traceback (most recent call last):
  File "<pyshell#638>", line 1, in <module>
    x.next()
StopIteration
>>> for i in gensquares(5):
	print i,":"

	
0 :
1 :
4 :
9 :
16 :
>>> for i in gensquares(5):
	print i,":",

	
0 : 1 : 4 : 9 : 16 :
>>> for i in x:
	print i,":",

	
>>> for i in gensquares(10):
	print i,":",

	
0 : 1 : 4 : 9 : 16 : 25 : 36 : 49 : 64 : 81 :
>>> def buildsquares(n):
	res=[]
	for i in range(n):res.append(i**2)
	return res

>>> for x in buildsquares(5):print x,":",

0 : 1 : 4 : 9 : 16 :
>>> res

Traceback (most recent call last):
  File "<pyshell#655>", line 1, in <module>
    res
NameError: name 'res' is not defined
>>> for x in [n**2 for n in range(5)]:print x,'
SyntaxError: EOL while scanning string literal
'
>>> for x in [n**2 for n in range(5)]:print x,':',

0 : 1 : 4 : 9 : 16 :
>>> for x in map((lambda x:x**2),range(5)):print x,':',

0 : 1 : 4 : 9 : 16 :
\
>>> D=iter(D)

Traceback (most recent call last):
  File "<pyshell#661>", line 1, in <module>
    D=iter(D)
NameError: name 'D' is not defined
>>> D={'a':1,'b':2,'c':3}
>>> D=iter(D)
>>> x.next()

Traceback (most recent call last):
  File "<pyshell#664>", line 1, in <module>
    x.next()
AttributeError: 'int' object has no attribute 'next'
>>> D={'a':1,'b':2,'c':3}
>>> x=iter(D)
>>> x.next()
'a'
>>> for key in D:
	print key,D[key]

	
a 1
c 3
b 2
>>> g=(x**2 for x in range(4))
>>> g.next()
0
>>> g.next()
1
>>> g.next()
4
>>> g.next()
9
>>> g.next()

Traceback (most recent call last):
  File "<pyshell#676>", line 1, in <module>
    g.next()
StopIteration
>>> for num in (x**2 for in range(4)):print '%s,%s' %(num,num/2.0)
SyntaxError: invalid syntax
>>> for num in (x**2 for x in range(4)):print '%s,%s' %(num,num/2.0)

0,0.0
1,0.5
4,2.0
9,4.5
>>> sum(x**2 for x in range(4))
14
>>> sum(x**2 for x in range(100))
328350
>>> sum(x for x in range(100))
4950
>>> sorted(x**2 for x in range(4),reverse=True)
SyntaxError: Generator expression must be parenthesized if not sole argument
>>> sorted((x**2 for x in range(4),reverse=True))
SyntaxError: invalid syntax
>>> sorted((x**2 for x in range(4)),reverse=True)
[9, 4, 1, 0]
>>> import math
>>> map(math.sqrt,(x**2 for x in range(4))


    p
    
SyntaxError: invalid syntax
>>> 
>>> map(math.sqrt,(x**2 for x in range(4))


    p
    
SyntaxError: invalid syntax
>>> sorted((x**2 for x in range(4)),reverse=True)
[9, 4, 1, 0]
>>> map(math.sqrt,(x**2 for x in range(4)))
[0.0, 1.0, 2.0, 3.0]
>>> ================================ RESTART ================================
>>> 
2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2]
forStatement         => 0.815583944321
listComprehension    => 0.593605041504
mapFunction          => 0.428925037384
generatorExpression  => 0.786180973053
>>> ================================ RESTART ================================
>>> 
2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2]
forStatement         => 0.742423057556
listComprehension    => 0.634648084641
mapFunction          => 0.424096822739
generatorExpression  => 0.851665973663
>>> ================================ RESTART ================================
>>> 
2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2]
forStatement         => 0.853139162064
listComprehension    => 0.65331697464
mapFunction          => 0.444695949554
generatorExpression  => 0.941188812256
>>> ================================ RESTART ================================
>>> 
2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2]
forStatement         => 0.74938416481
listComprehension    => 0.638173103333
mapFunction          => 0.436340093613
generatorExpression  => 0.779726982117
>>> ================================ RESTART ================================
>>> 
2.7.9 (default, Jun 29 2016, 13:08:31) 
[GCC 4.9.2]
forStatement         => 91.0315480232
listComprehension    => 77.0384349823
mapFunction          => 58.7156720161
generatorExpression  => 95.6496560574
>>> x=echo

Traceback (most recent call last):
  File "<pyshell#695>", line 1, in <module>
    x=echo
NameError: name 'echo' is not defined
>>> def echo(message):
	print message

	
>>> x=echo
>>> x('hello world')
hello world
>>> def indirect(func,arg):
	func(arg)

	
>>> indirect(echo,'hello jelloI')
hello jelloI
>>> 
