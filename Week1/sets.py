#unordered
#unchangeable
#no duplicates

data = {1,2,43,54, "Krishna", "Rana", "Lovely Professional University", "B.Tech", "CSE", 2022, 12212054}

data1 = [43,54,65]
print(data)
print(type(data))
print(len(data))    

#accessing data
for i in data:
    print(i)    

data.add("New Item")  # Adding a new item
print(data)     
data.remove(43)  # Removing an item
print(data)
data.discard("cheery")  # Discarding an item (does not raise an error if not found)
print(data)
data.pop()
print(data)  # Removes and returns an arbitrary element from the set
# data.clear()  # Clears the set
# print(data)  # Now the set is empty


data2 = {1, 2, 3, 4, 5}
data4 = {6, 7, 8, 9, 10}
data5 = data | data2 | data4
print(data5)  # Union of multiple sets
update = data2.union(data)  # Union of two sets
print(update)  # Combines elements from both sets, removing duplicates

data6 = data.intersection(data2)  # Intersection of two sets
print(data6)  # Elements common to both sets

data7 = data & data2
print(data7)  # Another way to find intersection using '&'
data8 = data.symmetric_difference(data2)  # Symmetric difference of two sets
print(data8)  # Elements in either set but not in both