#ordered
#chageable
#no duplicate


data = {
    "name" : "Krishna Rana",
    "age" : 22,
    "university" : "Lovely Professional University",
    "course" : "B.Tech",
    "major": "CSE",
    "year_of_passing" : 2022,
    "student_id" : 12212054,
    "hobbies" : ["Reading", "Coding", "Traveling"],
    "skills" : {"Python", "Java", "C++"}
}
# print(data)
# print(type(data))
# print(len(data))

#update_data

# data["year_of_passing"] = 2026
# print(data)

#another way to update data

# data.update({"year_of_passing": 2026, "hobbies": ["Reading", "Coding", "Traveling", "Gaming"]})
# print(data)

# data["weight"] = 83.5
# # print(data)
# data["height"] = 5.10
# print(data)


#using loop accesing dictionary

# for i in data:
#     print(i, ":", data[i])
    
# key = data.keys()
# print(key)

# value = data.values()
# print(value)

# item = data.items()
# print(item)   


#another method to copy data
# newdata2 = dict(data)
# print(newdata2)     

# x = data.pop("height")
# print(x)
# print(data)

# data.popitem() 
# print(data)

# data.clear()  # Clears the dictionary
# print(data)  # Now the dictionary is empty



myfamily = {
    "child1" : {
        "name" : "child1_name",
        "age" : 5
    },
    "child2" : {
        "name" : "child2_name",
        "age" : 7
    },
    
}
# print(myfamily)
#access child1 name
# print(myfamily["child1"]["name"])  
# print(myfamily)

#access this dictionary with the help of nested loop
for i, obj in myfamily.items():
    print(i)
    for j in obj:
        print(j, ":", obj[j])   