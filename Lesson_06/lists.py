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