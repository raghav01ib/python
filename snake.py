import random

d = 0
p = 0
snl={8:37,13:34,38:9,11:2,28:4,40:68,52:81,76:97,65:46,93:64,89:70}
def rolldice():
	return random.randint(1,6)

while True:
	r = input("press r to roll, q to quit : ")
	
	if r == 'r':
		d = rolldice()
		
		print("you got: ",d)
		
		if d == 6:
			print("congratulations!!,you can play now.")
			break
		else:
	
			print("roll again, till you get 6.")
	elif r == 'q':
		exit()			
while True:
	r = input("press r to roll, q to quit: ")

	if r == 'r':
		d = rolldice()
		print("you got : ",d)

		p = p+d
		if p > 100:
			p = p-d
			print("wait till you get", 100-p)

		print("your new position is: ",p)

		if p in snl:
			if p < snl[p]:
				print("wow, you got a lader ")
			else:
				print("oops,you got swallowed by a snake.")

			p = snl[p]
			print("move to ",p)
					
		
		if p == 100:
			print("you won!!!")
			exit()
		
	





	elif r == 'q':
		print("bye!")
		exit()	