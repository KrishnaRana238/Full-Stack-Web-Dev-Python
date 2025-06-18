#ordered
#immutable
#allow dependency

fruits = tuple(("Apple", "Banana", "Cherry", "Date", "Elderberry"))

print(fruits)
print(type(fruits))
print(len(fruits))


newfruits = list(fruits)
newfruits[1] = "berry"
fruits = tuple(newfruits)
print(fruits)
print(type(fruits))
print(len(fruits))