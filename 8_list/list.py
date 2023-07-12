# -----------List (Lists are used to store multiple items in a single variable)------
fruitsList = ["apple", "banana", "cherry"]
print(fruitsList)

# --------Lists allow duplicate values-----------
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruits)

# -------A list with strings, integers and boolean values-----
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# -------------Append (to add somthing in a list from last)------------------
listFriends = ["Sruthi", "Anil", "Preethi", "Shiva"]
listFriends.append("vamshi")
print(listFriends)

# -------------Extend (to add bulk data into a list)------------------------
listEnemies = ["balaladeva", "Rolex"]
listEnemies.extend(["vinnu", "Raju", "Shiva"])
print(listEnemies)

# -----------Remove (to remove an element from list)-----------------------
unitedBuddies = ["Vamshi", "Sandeep", "Rajesh", "Sampath", "sravan", "vinnu", "bittu", "bablu"]
unitedBuddies.remove("vinnu")
print(unitedBuddies)
