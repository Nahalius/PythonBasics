city = input("Enter city name = ")
sales = int(input("Enter sales volume = "))
cities = ["Sofia", "Varna", "Plovdiv"]
index = 4

#Discounts by cities
if 0 <= sales and sales <= 500:
    comision = [0.05,0.045,0.055]
elif 500 < sales and sales <= 1000:
    comision = [0.07,0.075,0.08]
elif 1000 < sales and sales <= 10001:
    comision = [0.08,0.1,0.12]
else:
    comision = [0.12,0.13,0.145]

#Indexing
if city in cities:
    index = cities.index(city)

discount = sales * comision[index]
print("{0:.2f}".format(discount)) #rounding
