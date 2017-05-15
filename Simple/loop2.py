# -*- coding: utf-8 -*-

#WhileLoop
counter = 5;

while counter > 0:
    print ("Broiach = ", counter)
    counter = counter - 1

#Break and continue
j = 0;

for i in range(5):  #range (start, end, step)
    j = j + 2
    print ('i = ', i, ', j = ', j)
    if j == 4:
        continue
    print("I will be skipped over if j = 4")
    if j == 6:
        break

#Use try to display errors
