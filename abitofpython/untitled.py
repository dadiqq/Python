class FirstClass:
	def setdata(self,value):
		self.data=value
	def display(self):
	    print(self.data)
x=FirstClass()
y=FirstClass()
x.setdata('king Artuhr')
y.setdata(3.14159)
x.display()
y.display()

x.data="new value"
x.display()
x.anthername='spam'
x.display()
