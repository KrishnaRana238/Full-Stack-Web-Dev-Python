n = 10
while True:
    k = int(input("Enter a number: "))
    if(n == k):
        print("You have entered the correct number")
        break
    else:
        print("You have entered the wrong number, try again")
        continue
print("End of the program")