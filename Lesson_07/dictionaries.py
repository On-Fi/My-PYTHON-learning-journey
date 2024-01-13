# Dictionaries
band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print("")
print(band2)

print(type(band))
print(len(band))

# Access items 
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all vaules
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("piano" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band["drums"] = "Bonham"
band.clear()
print(band)

# Looping
band = {
    "vocals" : "Plant",
    "guitar" : "Page",
    "bass" : "JPJ",
    "drums" : "Bonham"
}

for key in band:
    print(key, band[key])

for key, value in band.items():
    print(key, value)

# Copying   
band2 = band.copy() # shallow copy                                      
band3 = dict(band) # shallow copy   
band4 = band # shallow copy

print(band2)
print(band3)
print(band4)

print(id(band))