#string and slising
string = "this is kind of long string you see"
print(string[14])
print(string[13:21])

#tuples - immutable, ordered
tuple1 = (2, 3, 4, "text")
print(tuple1)


#lists - mutable, ordered
listo = [34, 54,65, "listoto"]
print (listo + [12,])
listo.remove(34)
listo.remove("listoto")
print(listo * 2) #copy the lists twise

#dictionaries

dicto1 = {"pepo":"shosho",4:5}
dicto2 = dict(c=1,f=3)
#dicto3 = list(zip("Ivan",range(1, 5)))

print( len(dicto2), dicto1)
print(dicto2.items())
print(dicto1.keys(),dicto2.values() )
