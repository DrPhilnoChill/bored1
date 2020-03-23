#Author: Phil

#Title
print("This is the bored machine 9000")

#Input stuff
a= int(input("Please insert your boredom level: "))
d= int(input("How many oscillations d of your boredom level " + str(a) + " do you want?: d= "))

#Set values for loops
i=0
b= " "
#Counts down and stops when d=0
while d!=0:
	d-=1
	c=1
	for i in range(a):
# Line goes till the middle of the levels
		if i<(a/2):
			print( str(b)*i + "I am bored")
			i+=1
# Line goes gradually to its original place back 
		else:
			print((str(b)*(int(a/2)-c))+ "I am bored")
			c+=1
			

