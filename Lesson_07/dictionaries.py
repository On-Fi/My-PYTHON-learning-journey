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
