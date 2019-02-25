import random
x=["r","p","s"]
while True:
	u=input("Please enter your choice, or press n to quit game..")
	
	if u=='n':
		print("Thankyou for playing")
		exit()
	
	c=random.choice(x)
	print("computer chooses ",c)
	
	if u==c:
		print("same pinch")
	
	elif u=="r" and c=="p":
		print("Oops!!..you loose")

	elif u=="p" and c=="s":
		print("Oops!!..you loose")

	elif u=="s" and c=="r":
		print("Oops!!..you loose")
	
	elif u=="r" and c=="s":
		print("Congratulations,you win!!..")
	
	elif u=="p" and c=="s":
		print("Congratulations,you win!!..")
	
	elif u=="s" and c=="p":
		print("Congratulations,you win!!..")



