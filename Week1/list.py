#list
#ordered
#mutable
#iterable

# data = ["Krishna", "Rana", "Lovely Professional University", "B.Tech", "CSE", 2022, 12212054]
# print(data)
# print(len(data))
# print(type(data))


fruits = list(("Apple", "Banana", "Cherry", "Date", "Elderberry"))
# print(fruits)
# #update value
# fruits[2] = "Coconut"
# print(fruits)

# #acces list
# print(fruits[0:5])
# print(fruits[:3])
# print(fruits[2:])
# print(fruits[-3,-1])  # Last item


# fruits[1:4]=["apple","cranberry"]
# print(fruits)
# quantity=[10, 20, 30, 40, 50]
# print(quantity)
# fruits.extend(quantity)
# print(fruits)
# fruits.remove("Banana")  # Remove first occurrence of "Banana"

# print(fruits)
# fruits.pop(3)  # Remove item at index 2
# print(fruits)






# fruits.sort(reverse=True)  # Sort the list in descending order
# print(fruits)

# fruits.reverse()  # Reverse the order of the list
# print(fruits)

#copy
newfruits = fruits.copy()
print(newfruits)

newfruits1 = list(fruits)  # Another way to copy
print(newfruits1)

newfruits2 = fruits[:]  # Slicing to copy
print(newfruits2)

for i in range(len(fruits)):
    print(fruits[i])


data = [i for i in fruits if i=="kiwi" or i=="Apple"]
print(data)
