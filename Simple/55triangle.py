#runs on Python3.*

n = input("Please enter side lenth: ")
n = int(n)
a = input("Please enter sumbol: ")

for i in range(0, n):
    print(i * a )

print (n * a)
#Prints n-rows triangle with asterics
for j in range(n, 0,-1):
    print(j * a )
