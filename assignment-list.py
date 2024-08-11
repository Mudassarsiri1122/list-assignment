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
 guest:list[str]=['Saif','Ahad','Mubashir','Muzamil']
 for guests in guest:
  print(f"Dear {guests} please come my home and taste my food")
  print(f"\n {guest}can come to dinner")
  guest[1] = "Mudassar Hassan"
  for guest2 in guest:
   print(f"Dear {guest2} please come my home and taste my food")
#Question 6
guest:list[str]=['mudassar','don','ustaad','shanzia']
print(f"Dear {guest}, you are still invited to dinner at my place. Looking forward to having you")
guest.insert(0,"shahid")
print(guest)
middleindex = len(guest)
guest.insert(middleindex,"anwar")
guest.append("hassan")
print(guest)
#Question 7
guest:list[str]=['mudassar','don','ustaad','shanzia']
print("Unfortunately, I can invite only two people for dinner.\n")

remove= guest.pop()
remove= guest.pop()
print(f"Sorry, {remove}, I can't invite you to dinner.")
for guest1 in guest:
    print(f"{guest}, you're still invited to dinner")
    del[guest[0]]
    del[guest[0]]
#Question 8

places_to_visit = ["Kyoto", "lahore", "karachi", "islamabad", "pashawar"]

print("Original list:")
print(places_to_visit)

print("\nList in alphabetical order using sorted():")
print(sorted(places_to_visit))


print("\nList after using sorted() (original order):")
print(places_to_visit)

print("\nList in reverse-alphabetical order using sorted():")
print(sorted(places_to_visit, reverse=True))


print("\nList after using sorted() in reverse (original order):")
print(places_to_visit)


places_to_visit.reverse()
print("\nList after using reverse():")
print(places_to_visit)

places_to_visit.reverse()
print("\nList after using reverse() again (back to original order):")
print(places_to_visit)

places_to_visit.sort()
print("\nList after using sort() (alphabetical order):")
print(places_to_visit)

places_to_visit.sort(reverse=True)
print("\nList after using sort(reverse=True) (reverse-alphabetical order):")
print(places_to_visit)

#Question 9
cities = ["New York", "Tokyo", "Paris", "Sydney", "Cairo"]


print("Original list:")
print(cities)

print("\nList in alphabetical order using sorted():")
print(sorted(cities))

print("\nList after using sorted() (original order):")
print(cities)
print("\nList in reverse-alphabetical order using sorted():")
print(sorted(cities, reverse=True))


print("\nList after using sorted() in reverse (original order):")
print(cities)


cities.reverse()
print("\nList after using reverse():")
print(cities)


cities.reverse()
print("\nList after using reverse() again (back to original order):")
print(cities)

cities.append("Rio de Janeiro")
print("\nList after using append():")
print(cities)

cities.insert(2, "Berlin")
print("\nList after using insert() at position 2:")
print(cities)


popped_city = cities.pop()
print("\nCity removed using pop():", popped_city)
print("List after using pop():")
print(cities)

cities.remove("Paris")
print("\nList after using remove() to remove 'Paris':")
print(cities)

cities.sort()
print("\nList after using sort() (alphabetical order):")
print(cities)


cities.sort(reverse=True)
print("\nList after using sort(reverse=True) (reverse-alphabetical order):")
print(cities)

print("\nNumber of cities in the list:")
print(len(cities))

#Question 10

cities = ["New York", "Tokyo", "Paris", "Sydney", "Cairo"]


print("List of cities:")
print(cities)

print("\nAttempting to access an index that is out of range (index 5):")
try:
    print(cities[5])  
except IndexError as e:
    print(f"Error encountered: {e}")

print("\nCorrected access to the last element (index 4):")
print(cities[4])
