import random
x=["r","p","s"]
us=0
cs=0
while True:
	u=input("Please enter your choice, or press n to quit game..")
	
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
	print("computer chooses ",c)
	
	if u==c:
		print("same pinch")
	
	elif u=="r" and c=="p":
		print("Oops!!..you loose")
		cs=cs+1


	elif u=="p" and c=="s":
		print("Oops!!..you loose")
		cs=cs+1

	elif u=="s" and c=="r":
		print("Oops!!..you loose")
		cs=cs+1

	elif u=="r" and c=="s":
		print("Congratulations,you win!!..")
		us=us+1
	
	elif u=="p" and c=="s":
		print("Congratulations,you win!!..")
		us=us+1

	elif u=="s" and c=="p":
		print("Congratulations,you win!!..")
		us=us+1


