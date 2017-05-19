# -*- coding: utf-8 -*-
#Using Python3
#Drowing dynamic table 

rows = input("Enter the number of rows: ")
columns = input("Enter the number of columns: ")
celNum = input("Enter number in cells: ")

rows = int(rows)
columns = int(columns)
celNum = int(celNum)

#Labels
print("Table", end = " ") #print on the same line
for i in range(0,columns):
    print("T", end = " ")
print("Total")

#Body
for j in range(0, rows, 1 ):
    print(" row" + str(j+1).zfill(1), end = " ")  #formats int to string
    for j in range(0, columns,1):
        print(celNum, end = " ")
    print("Suma")

#Totals
print("Total", end = " ") #print on the same line
for i in range(0,columns):
    print("S", end = " ")
print("Vsi4ko")
