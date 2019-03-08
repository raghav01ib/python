q=[12,3,4,22,654,7,1,0]
def func1(a,b,c):
	d=a+b+c
	print(d)
func1(7,8,9)

def func2(a,b,c):
	if a<=b and b<c:
		print("max",c)
	elif a>b and b>=c:
		print("max",a)
	elif a<b and a==c:
		print("max",b)
	else:
		print("more than one values are equal")				

func2(1,2,3)


