
# n = int(input("Enter the number of rows: "))
# row = 1
# count =1
# while row <= n:
#     col = 1
#     while col <= row:
#         print(row-col + 1, end=' ')
#         col += 1
#     print()  
#     row += 1


# n = int(input("Enter the number of rows: "))
# row = 1
# count =1
# while row <= n:
#     col = 1
#     while col <= row:
#         ch = 'A' + col -1
#         print(ch, end=' ')
#         col += 1
#     print()  
#     row += 




n = int(input("Enter the number of rows: "))
row = 1

while row <= n:
    # Print spaces
    space = n - row
    while space > 0:
        print(" ", end=' ')
        space -= 1
    
    # Print characters
    count = 1
    while count <= row:
        ch = chr(ord('A') + count - 1)
        print(ch, end=' ')
        count += 1
    
    # Move to the next line
    print()
    row += 1