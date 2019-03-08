#creating a function without parameter:
def func1():
	print("hii")
	print("hello")
func1()

#with parameter
def func2(a):
	print("helllooo\n",a)
func2("sbi")

#with 2/3 parameters
def func3(a,b,c):
	d=a*b*c
	print(a,b,c,d)
func3(2,5,9)

#with default parameter
def func4(university='CMR'):
	print("Hey,I study in " + "\n" + university)
func4("Anna university")
func4("GuruGobind University")
func4()			

#return statement
def func7(a,b,c):
	d=a-b-c
	return d
e=func7(2,5,6)
print (e)

#calling one function from other and statement
def func5(a,b):
	print("syntex error")
	c=a+b
	return c
def func6():
	print("there is a syntex error")
	s=func5(3,5)
	print("addition is ",s)
func6()		