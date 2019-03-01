import random
x=["r","p","s"]
d={'r':"rock",'p':"paper",'s':"scissor"}
us=0
cs=0
while True:
	u=input("Please enter your choice, or press n to quit game..")
	if u in d:
		print("user choose",d[u])
	
	if u=='n':
		print("Thankyou for playing")
		print("user score is: ",us)
		print("computer score: ",cs)
		if us>cs:
			print("you won!!")
		else:
			print("you loose")	
		exit()
	
	c=random.choice(x)
	if c in d:

		print("computer chooses ",d[c])

	if (x.index(c)+1)%3==x.index(u):
		print("you won")
	else:
		print("computer won")	

	