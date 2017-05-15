# -*- coding: utf-8 -*-
userInput = input('Enter 1 or 2: ')

if userInput == "1":
    print ("Ama zdrasti")
elif userInput == "2":
    print ("Python Rocks!")
else:
    print ("You did not enter a valid number")

print ("This is task A"  if userInput == "1" else "This is task B")

#for Loop
message = "forLoop";

for i in message:
    print (i)
