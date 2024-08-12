#Question 1
name:list[str]=['Saif','Ahad','Mubashir','Muzamil']
print(name[0])
print(name[1])
print(name[2])
print(name[3])




#Question 2
names:list[str]=['Saif','Ahad','Mubashir','Muzamil']
for name in names:
 print(f"maira name {name} hai")
 
 
 
 
 #Question 3
 cars:list[str]=['Corolla','Elantra','Honda Civic','Honda City']
for car in cars:
 print(f"I would like to own a {car}")
 
 
 
 
 
 #Question 4
 guest:list[str]=['Saif','Ahad','Mubashir','Muzamil']
 for guests in guest:
  print(f"Dear {guests} please come my home and taste my food")
  
  
  
  
#Question 5
guest:list[str]=['Ahad','Mubashir','Muzamil']

print(guest)
 
guest.insert(1,"Saif")

print(guest)

for guest2 in guest:
   print(f"Dear {guest2} please come my home and taste my food")
   
   
   
   
   
   
#Question 6
guest:list[str]=['Ahad','Mubashir','Muzamil']

print(guest)

guest.insert(0,"Saif")

print(guest)

guest.insert(2,"Abdullah")

print(guest)

guest.append("Ali")

print(guest)

for guest1 in guest:

 print(f"{guest1} i invite you tonight dinner")
 
 
 
 
 
#Question 7
guest:list[str]=['Ahad','Mubashir','Muzamil','Abdullah','Arslan']

print(guest)

print("I can invite only two people of the dinner")

guest1 = guest.pop()
guest2 = guest.pop()
guest3 = guest.pop()


print(f"sorry {guest1,guest2,guest3} i can not invited them into the dinner")

print(f"{guest} they still invited")

del guest[0]
del guest[0]

print(f"{guest} they have an empty list at the end of your program")






#Question 8
places:list[str]=['lahore','karachi','multan','brooklyne','newyork']
print("Original list :")
print(places)
print("By using sorted method :")
print(sorted(places))
print("By using reverse sorted method")
print(sorted(places ,reverse=True))
print("list is still in its original order :")
print(places)
print("using reverse method :")
places.reverse()
print(places)
print("using reverse method again :")
places.reverse()
print(places)
print("original list print again:")
print(places)
print("sorted list : ")
print(sorted(places))







#Question 9
cities:list[str]=['lahore','karachi','multan','akbar chonk','bdami bagh','multan','sahiwal','azaad kashmir','jamo kashmir']
cities1:list[str]=['america','china','russia','ireland']
print("Original list :")
print(cities)
print("1 sorted method :")
print(sorted(cities))
print("2 reverse sorted method")
print(sorted(cities ,reverse=True))
print("3 reverse method :")
cities.reverse()
print(cities)
print("4 appened method")
cities.append("jallo moor")
print(cities)
print("5 insert method")
cities.insert(1,"Daroghawala")
print(cities)
print("6 pop method")
cities.pop()
print(cities)
print("7 pop method with indexing")
cities.pop(4)
print(cities)
print("8 remove method")
cities.remove("Daroghawala")
print(cities)
print("9 del method")
del cities[2]
print(cities)
print("10 count method")
cities.count(3)
print(cities)
print("11 index method")
cities.index("multan")
print(cities)
print("12 copy method")
cities.copy()
print(cities)
print("13 clear method")
cities.clear()
print(cities)
print("extend method")
cities.extend(cities1)
print(cities)






#Question 10

city:list[str]=['lahore','sahiwal','badami bagh','jallo moor']

#print(city[4])


