#you need to converter from kilometers to miles
# 1km = 0.621371 miles
kilimetertomiles = float(input("Enter distance in kilometers: "))
def kilotomiles(kilometers):
    if kilometers < 0:
        return "Distance cannot be negative."
    miles = kilometers * 0.621371
    return miles
print("Distance in miles:", kilotomiles(kilimetertomiles))  