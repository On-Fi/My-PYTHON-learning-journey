users = ["Ali", "Jan", "Alina", "Jana"]

data = ["Ali", 69, True]

emptylist = []

print("")
print("Jan" in users)
print("Jan" in data)
print("")

print(users[0])
print(users[-2])
print(users[-3:1])
print("")

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print("")
print("New List")
users.append("Elsa")
print(users)

print("")
users += ["Anna"]
print(users)

print("")
users.extend(["Onur", "Bruno"])
print(users)

print("")
users.insert(0, "Zeki")
print(users)

print("")
users[2:2] = ["Paul", "Jin"]
print(users)

print("")
users[1:3] = ["Robert", "Roberta"]
print(users)

print("")
users.remove ("Bruno")
print(users)

print("")
print(users.pop())
print(users)

print("")
del users[0]
print(users)

# del data
data.clear()
print(data)

print("")
users[1:2] = ["onur"]
users.sort(key=str.lower)
print(users)


nums = [69, 420, 13, 88, 30, 42]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "yomama", True])
print(mylist)

"""
---------------------------
-----------Tuples----------
---------------------------
"""

mytuple = (2,4,6,8,2,2,2)

anothertuple = ("Onur", "Zeki", 27 , False)

print("")
print("")
print("")
print("")
print("")
print("")
print(mytuple)
print(anothertuple)
print(type(anothertuple))


newlist = list(anothertuple)
newlist.append("Popo")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, heybro) = anothertuple
print(one)
print(two)
print(heybro)

print(mytuple.count(2))